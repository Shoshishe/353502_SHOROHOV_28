from decimal import Decimal
from typing import List
import logging
import requests
from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound, HttpRequest, HttpResponseRedirect
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django import forms
from .models import FAQ, News, FurnitureKind, Furniture, User, Wholesalers, BoughtFurniture, PointsOfDelivery, Contacts, Comment
from django.http import HttpResponseForbidden
from django.contrib.auth.models import Group
from datetime import datetime, timezone
from django.core.validators import RegexValidator
from .models import Promocode
from django.db import IntegrityError
from django.contrib.auth import get_user_model
from django import template
from django.db.models import Max
from django.core.exceptions import ObjectDoesNotExist
import pytz
from django.contrib.auth import login
import matplotlib.pyplot as plt
import numpy as np


def role_based_access_required(role):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if request.user.groups.filter(name=role).exists():
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponseForbidden("Unauthorized access")
        return _wrapped_view
    return decorator


def role_based_access_denied(role):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.groups.filter(name=role).exists():
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponseForbidden("Unauthorized access")
        return _wrapped_view
    return decorator


class UserRegisterForm(forms.Form):
    phone_regex = RegexValidator(
        regex=r'^\+375\d{9}$', message="Phone number must be entered in the format: '+375XXXXXXXXX'")
    username = forms.CharField(
        help_text="Enter your username", min_length=5, max_length=20)
    email = forms.EmailField(
        help_text="Enter your email", min_length=3, max_length=50)
    age = forms.IntegerField(min_value=18, max_value=120)
    phone_number = forms.CharField(validators=[phone_regex], max_length=13)
    role = forms.ChoiceField(help_text="Choose your role for signing up", choices=(
        (1, "Customer"), (2, "Client"), (3, "Superuser")))
    password = forms.CharField(widget=forms.PasswordInput(
    ), help_text="Enter your password", min_length=3, max_length=20)


class SignUpView(FormView):
    form_class = UserRegisterForm
    success_url = reverse_lazy("login/")
    template_name = "registration/signup.html"


class ClientSignUpView(FormView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('login/')
    template_name = "registragtion/client_signup.html"


class UserLoginForm(forms.Form):
    username = forms.CharField(
        help_text="Enter your username", min_length=5, max_length=20)
    password = forms.CharField(widget=forms.PasswordInput(
    ), help_text="Enter your password", min_length=3, max_length=20)


def loginView(request: HttpRequest):
    user_form = UserLoginForm()
    if request.method == "POST":
        user_form = UserLoginForm(request.POST)
        if user_form.is_valid():
            username = user_form.cleaned_data["username"]
            password = user_form.cleaned_data["password"]
        try:
            user = get_user_model().objects.get(username=username, password=password)
        except ObjectDoesNotExist:
            user_form.add_error(
                error="No user with such credentials", field="username")
            return render(request, "registration/login.html", {"form": user_form})
        else:
            tz = request.session.get('django_timezone')
            login(request, user)
            request.session['django_timezone'] = tz
            return HttpResponseRedirect(reverse_lazy("home"))
    return render(request, "registration/login.html", {"form": user_form})


def signUpView(request: HttpRequest):
    if request.method == "POST":
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid():
            username = user_form.cleaned_data["username"]
            email = user_form.cleaned_data["email"]
            age = user_form.cleaned_data["age"]
            phone = user_form.cleaned_data["phone_number"]
            password = user_form.cleaned_data["password"]
            role = user_form.cleaned_data["role"]
            is_superuser = False
            is_staff = False
            if role == "3":
                is_superuser = True
                is_staff = True
            try:
                user = get_user_model().objects.create(
                    username=username,
                    email=email,
                    password=password,
                    phone=phone,
                    age=age,
                    is_superuser=is_superuser,
                    is_staff=is_staff,
                )
            except IntegrityError as e:
                print(e.args[0])
                if 'unique constraint' in e.args[0].lower():
                    for arg in e.args:
                        if 'furniture_factory_user.username' in arg.lower():
                            user_form.add_error(
                                error="Username has been already taken", field="username")
                        elif 'furniture_factory_user.email' in arg.lower():
                            user_form.add_error(
                                error="Email has been already taken", field="email")
                return render(request, "registration/signup.html", {"form": user_form})
            if role == "1":
                group = Group.objects.get(name='customers')
                user.groups.add(group)
            elif role == "2":
                group = Group.objects.get(name='clients')
                user.groups.add(group)
            user.save()
            return HttpResponseRedirect("/")
        else:
            print(user_form.errors)
    else:
        user_form = UserRegisterForm()
    return render(request, "registration/signup.html", {"form": user_form})


class Statistics:
    def __init__(self, Name: str, Value: str):
        self.name = Name,
        self.value = Value,


def gather_stats() -> List[Statistics]:
    stats = []
    dct = {}
    for fur in BoughtFurniture.objects.all():
        val = dct.get(fur.furniture.price)
        if val is None:
            dct[fur.furniture.price] = 1
        else:
            dct[fur.furniture.price] = dct[fur.furniture.price] + 1
    max_val = 0
    max_key = 0
    for key, val in dct.items():
        if val > max_val:
            max_val = val
            max_key = key

    stat = Statistics("Mode of the sales and the count of appearances",
                      f"{max_key} appeared {max_val} times")
    stats.append(stat)
    sum = 0
    for fur in BoughtFurniture.objects.all():
        sum += fur.furniture.price
    sum /= len(BoughtFurniture.objects.all())
    stats.append(Statistics(
        "Average price of the bought furniture", f"{sum}"))

    bought = BoughtFurniture.objects.order_by(('furniture__price'))
    median = bought[len(bought)//2]
    stats.append(Statistics("Median of the sales",
                 f"{median.furniture.price}"))
    most_profit_fur = None
    max = 0
    for fur in Furniture.objects.all():
        sum = fur.price * len(BoughtFurniture.objects.filter(furniture=fur))
        if sum > max:
            max = sum
            most_profit_fur = fur
    stats.append(Statistics(f"Most profitable furniture (total revenue is {max})",
                 f"{most_profit_fur.name}"))

    dct = {}
    for cust in User.objects.all():
        val = dct.get(cust.age)
        if val is None:
            dct[cust.age] = 1
        else:
            dct[cust.age] = dct[cust.age] + 1
    max_val = 0
    max_key = 0
    for key, val in dct.items():
        if val > max_val:
            max_val = val
            max_key = key

    stat = Statistics("Mode of the age of clients and the count of appearances",
                      f"{max_key} appeared {max_val} times")
    stats.append(stat)
    sum = 0
    for usr in User.objects.all():
        sum += usr.age
    sum /= len(BoughtFurniture.objects.all())
    stats.append(Statistics(
        "Average age of the clients", f"{sum}"))

    return stats


class Graphics:
    def __init__(self, name: str, file_path: str):
        self.file_path = file_path,
        self.name = name


def gather_graphics() -> List[Graphics]:
    graphics = []
    ages = []
    for usr in User.objects.all():
        ages.append(usr.age)
    plt.hist(ages)
    path = "/home/shosh/BSUIR projects/SCI/353502_SHOROHOV_28/IGI/LR5/lr5/media/age_distribution.png"
    plt.savefig(path)
    plt.close()
    gr = Graphics("Age distribution", path)
    gr.name = "Age distribution"
    gr.file_path = "media/age_distribution.png"
    graphics.append(gr)
    names = []
    profited = []
    for bought in BoughtFurniture.objects.values_list("furniture__name", flat=True).distinct():
        names.append(bought)
        sum = 0
        for profit in BoughtFurniture.objects.filter(furniture__name=bought):
            sum += profit.furniture.price
        profited.append(sum)

    plt.pie(profited, labels=names, startangle=90)
    path = "/home/shosh/BSUIR projects/SCI/353502_SHOROHOV_28/IGI/LR5/lr5/media/profit_distribution.png"
    plt.savefig(
        path)
    plt.close()

    gr = Graphics("Profit distribution", path)
    gr.name = "Profit distribution"
    gr.file_path = "media/profit_distribution.png"
    graphics.append(gr)
    return graphics


def index(request: HttpRequest):
    appid = '63026ab922acdc159af4d7d5c6adca54'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid
    city = 'Minsk'
    res = requests.get(url.format(city)).json()
    city_info = {
        'city': city,
        'temp': res["main"]["temp"],
        'icon': res["weather"][0]["icon"]
    }

    timezone_name = request.session['django_timezone']
    stats = []
    if not request.user.is_authenticated:
        coupons = Promocode.objects.all().filter(is_archivated=False)
        for coupon in coupons:
            coupon.discount = coupon.discount * 100
        furniture_kinds = FurnitureKind.objects.all()
        products = Furniture.objects.all()
        if 'min_price' in request.POST:
            sort = request.POST.get('sort')
            filter_price1 = request.POST.get('min_price')
            filter_price2 = request.POST.get('max_price')
            if filter_price1 == '':
                filter_price1 = 0
            else:
                try:
                    filter_price1 = Decimal(filter_price1)
                except ValueError:
                    filter_price1 = 0
                    logging.warning(
                        "Invalid price for a start of filtering range")
            if filter_price2 == '':
                filter_price2 = Furniture.objects.aggregate(Max('price'))[
                    'price__max']
            else:
                try:
                    filter_price2 = Decimal(filter_price2)
                except ValueError:
                    filter_price2 = Furniture.objects.aggregate(Max('price'))[
                        'price__max']
                    logging.warning(
                        "Invalid price for an end of filtering range")
            products = Furniture.objects.filter(
                price__range=(filter_price1, filter_price2))
            if sort:
                products = products.order_by("price")
        stats = gather_stats()
        graphics = gather_graphics()
        return render(request, "home.html", {"coupons": coupons, "kinds": furniture_kinds, "products": products, "tz": timezone_name + " date", "tz_date": datetime.now(pytz.timezone(timezone_name)).strftime("%d-%m-%Y"), "stats": stats, "graphics": graphics, "info": city_info})
    stats = gather_stats()
    graphics = gather_graphics()
    for stat in stats:
        stat.name = " ".join(stat.name)
        stat.value = " ".join(stat.value)
    return render(request, "home.html", {"tz": timezone_name + " date", "tz_date": datetime.now(pytz.timezone(timezone_name)).strftime("%d-%m-%Y"), "stats": stats, "graphics": graphics, "info": city_info})


@login_required
def create_faqs(request: HttpRequest):
    if request.method == "POST":
        faq = FAQ()
        faq.question = request.POST.get("question")
        faq.answer = request.POST.get("answer")
        faq.save()
    else:
        logging.ERROR(
            f"Invalid request method for create_faqs {request.method} desired one is POST")
    return HttpResponseRedirect("/faqs")


@login_required
def faqs(request: HttpRequest):
    user = request.user
    if user.is_authenticated:
        faqs = FAQ.objects.all()
        return render(request, "faq.html", {"faqs": faqs})


@login_required
def edit(request, id):
    try:
        faq = FAQ.objects.get(question=id)
        if request.method == "POST":
            faq.answer = request.POST.get("answer")
            faq.question = request.POST.get("question")
            faq.save()
            return redirect('/faqs/')
        else:
            faqs = FAQ.objects.all()
            return render(request, "edit_faq.html", {"faq": faq})
    except FAQ.DoesNotExist:
        return HttpResponseNotFound("<h2>FAQ not found</h2><a href='/faqs'><button>Return</button></a>")


@login_required
def delete(request, id):
    try:
        faq = FAQ.objects.get(question=id)
        faq.delete()
        return redirect('/faqs/')
    except FAQ.DoesNotExist:
        return HttpResponseNotFound("<h2>FAQ not found</h2><a href='/faqs'><button>Return</button></a>")


@login_required
def news(request: HttpRequest):
    news = News.objects.last()
    return render(request, "news.html", {"header": news.header, "image": news.image_path, "content": news.content})


class ProductBuyingForm(forms.Form):
    price = forms.FloatField(widget=forms.HiddenInput)
    name = forms.CharField(widget=forms.HiddenInput)


@login_required
@role_based_access_denied("admin")
def personal_account(request: HttpRequest):
    client = request.user.groups.filter(name="clients").exists()
    customer = request.user.groups.filter(name="customers").exists()
    admin = request.user.is_superuser

    context = {}
    if client:
        context["role"] = "client"
        wholesalers = Wholesalers.objects.all()
        bought = BoughtFurniture.objects.all()
        context["wholesalers"] = wholesalers
        context["bought"] = bought

    elif customer:
        context["role"] = "customer"
        points = PointsOfDelivery.objects.all()
        context["points"] = points
        bought = BoughtFurniture.objects.filter(owner=request.user)
        context["bought"] = bought
        furnitures = Furniture.objects.all()
        context["furnitures"] = furnitures
        coupons = Promocode.objects.all()
        for coupon in coupons:
            coupon.discount *= 100
        context["coupons"] = coupons
        if request.method == "POST":
            price = request.POST.get("price")
            name = request.POST.get("name")
            furniture = Furniture.objects.filter(name=name).first()
            BoughtFurniture.objects.create(
                furniture=furniture, bought_at=datetime.now().date(), owner=request.user)
    elif admin:
        context["role"] = "admin"
    else:
        logging.error(
            f"Invalid group of user logined")
        return HttpResponseForbidden("Unauthorized access")
    return render(request, "personal_account.html", context)


@login_required
def contacts(request: HttpRequest):
    contacts = Contacts.objects.all()
    return render(request, "contacts.html", {"contacts": contacts})


@login_required
def policy(request: HttpRequest):
    return render(request, "policy.html", {})


@login_required
def promocodes(request: HttpRequest):
    coupons = Promocode.objects.all().filter(is_archivated=False)
    return render(request, "promocodes.html", {"coupons": coupons})


@login_required
def about(request: HttpRequest):
    return render(request, "about.html", {})


@login_required
def comments(request: HttpRequest):
    comments = Comment.objects.all()
    create_form = CommentsCreateForm()
    return render(request, "comments.html", {"comments": comments, "form": create_form})


class CommentsCreateForm(forms.Form):
    text = forms.CharField(
        help_text="Enter comment text", max_length=255)
    rating = forms.FloatField(
        help_text="Enter your rating", min_value=1, max_value=5)
    name = forms.CharField(help_text="Enter comment rating", max_length=20)


@login_required
def create_comments(request: HttpRequest):
    comments = Comment.objects.all()
    if request.method == "POST":
        comment_create_form = CommentsCreateForm(request.POST)
        if comment_create_form.is_valid():
            comment = Comment()
            comment.date = datetime.now().date()
            comment.text = comment_create_form.cleaned_data["text"]
            comment.rating = comment_create_form.cleaned_data["rating"]
            comment.name = comment_create_form.cleaned_data["name"]
            comment.save()
            comments = Comment.objects.all()
            return render(request, "comments.html", {"form": comment_create_form, "comments": comments})
        else:
            return render(request, "comments.html", {"form": comment_create_form, "comments": comments})
    else:
        logging.ERROR(
            f"Invalid request method for create_comments {request.method} desired one is POST")
    return HttpResponseRedirect("/comments")
