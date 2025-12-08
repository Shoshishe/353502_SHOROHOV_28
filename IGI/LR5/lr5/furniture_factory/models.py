from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import PermissionsMixin
# Create your models here.
from django.contrib.auth.models import UserManager


class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
    date = models.DateField(default=timezone.now)


class FurnitureKind(models.Model):
    name = models.CharField(max_length=255)


class FurnitureModel(models.Model):
    name = models.CharField(max_length=255)


# TODOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
class Partner(models.Model):
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    logo = models.FileField()


class Client(models.Model):
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=58)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)


class News(models.Model):
    header = models.CharField(max_length=255)
    image_path = models.ImageField(blank=True)
    shorthand = models.CharField(max_length=255, default="")
    content = models.CharField(max_length=255, default="")


class Promocode(models.Model):
    name = models.CharField(max_length=255)
    discount = models.DecimalField(max_digits=5, decimal_places=5)
    is_archivated = models.BooleanField()


class Comment(models.Model):
    topic = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    rating = models.FloatField(default=5.0)
    text = models.CharField(max_length=255, default="")
    date = models.DateField(default=timezone.now)


class About(models.Model):
    text = models.TextField()
    video = models.FileField(upload_to='videos/')
    logo = models.FileField(upload_to='logos/')
    requisites = models.TextField()
    cert = models.TextField(default="rnd_name")


class Vacancy(models.Model):
    paycheck = models.DecimalField(max_digits=10, decimal_places=5)
    name = models.CharField(max_length=255)
    posted = models.DateField()


class Furniture(models.Model):
    name = models.CharField(max_length=255, unique=True)
    product_code = models.CharField(max_length=255)
    kind = models.ManyToManyField(FurnitureKind)
    is_made = models.BooleanField()
    price = models.DecimalField(max_digits=10, decimal_places=5)


class Order(models.Model):
    company_name = models.CharField(max_length=255)
    order_start_date = models.DateField()
    furniture = models.OneToOneField(Furniture, on_delete=models.CASCADE)
    furniture_count = models.IntegerField()
    order_end_date = models.DateField()

# class BoughtByCustomer(models.Model):
#     customer = models.ForeignKey(Client, on_delete=models.CASCADE)
#     bought_furnitures = models.ManyToManyRel(Furniture)


class PointsOfDelivery(models.Model):
    latitude = models.FloatField()
    longtitude = models.FloatField()
    name = models.CharField(max_length=255)


class Wholesalers(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, max_length=50)
    username = models.CharField(unique=True, max_length=20)
    age = models.IntegerField(default=18)
    phone = models.CharField(default="+375291435499", max_length=20)
    password = models.CharField(max_length=20)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []


class Contacts(models.Model):
    photo = models.ImageField()
    description = models.CharField(max_length=255)
    email = models.EmailField(default="rndemail@gmail.com")
    phone = models.TextField(default="+375382283711")
    username = models.TextField(default="labwc")


class BoughtFurniture(models.Model):
    owner = models.ForeignKey(User,
                              on_delete=models.CASCADE)
    furniture = models.ForeignKey(Furniture, on_delete=models.CASCADE)
    bought_at = models.DateField()


class CartItem(models.Model):
    furn = models.ForeignKey(Furniture, on_delete=models.CASCADE)
    count = models.IntegerField(auto_created=1)


class Cart(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    furnitures = models.ManyToManyField(CartItem)
