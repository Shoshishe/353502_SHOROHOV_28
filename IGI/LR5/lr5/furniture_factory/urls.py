from django.urls import path
from .views import SignUpView
from .views import signUpView
from .views import loginView
from django.contrib import admin
from django.urls import path, re_path, include
from furniture_factory import views

urlpatterns = [
    path("accounts/signup/", signUpView, name="signup"),
    path("accounts/login/", loginView, name="login"),
    path('admin/', admin.site.urls),
    re_path("^$", views.index, name="home"),
    path("accounts/", include("django.contrib.auth.urls")),
    # path("accounts/", include("furniture_factory.urls")),
    path("faqs/", views.faqs, name="faqs"),
    path("news/", views.news),
    re_path(r"^faqs/create_faq", views.create_faqs),
    path("faqs/edit/<str:id>/", views.edit, name="ed"),
    path("faqs/delete/<str:id>/", views.delete),
    path("personal_account/", views.personal_account),
    path("contacts/", views.contacts),
    path("policy/", views.policy),
    path("promocodes/", views.promocodes),
    path("about/", views.about),
    path("comments/", views.comments),
    re_path(r"^comments/create_comments", views.create_comments)
]
