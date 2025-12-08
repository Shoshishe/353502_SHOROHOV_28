from django.contrib import admin

from .models import FAQ, Cart, Furniture, FurnitureKind, Client, News, Promocode, Comment, Contacts, About, Vacancy, FurnitureModel, Order, User, Wholesalers, BoughtFurniture, PointsOfDelivery, Partner

# Register your models here.


class PromocodesAdmin(admin.ModelAdmin):
    list_filter = ["discount",
                   "name", "is_archivated"]


class FAQsAdmin(admin.ModelAdmin):
    list_filter = ["question", "answer"]


class UserAdmin(admin.ModelAdmin):
    list_filter = ["email", "username"]


class ClientsAdmin(admin.ModelAdmin):
    list_filter = ["code", "name", "city", "address", "phone"]


admin.site.register(FAQ, FAQsAdmin)
admin.site.register(FurnitureKind)
admin.site.register(Client, ClientsAdmin)
admin.site.register(News)
admin.site.register(Promocode, PromocodesAdmin)
admin.site.register(Comment)
admin.site.register(Contacts)
admin.site.register(About)
admin.site.register(Vacancy)
admin.site.register(FurnitureModel)
admin.site.register(Order)
admin.site.register(Furniture)
admin.site.register(User, UserAdmin)
admin.site.register(Wholesalers)
admin.site.register(BoughtFurniture)
admin.site.register(PointsOfDelivery)
admin.site.register(Partner)
admin.site.register(Cart)
