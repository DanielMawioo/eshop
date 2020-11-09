from .models import Product, Offer
from django.contrib import admin
admin.site.site_title = 'E-shop Admin.'
admin.site.site_header = 'E-shop .'


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'stock', 'price', 'thumbnail']


admin.site.register(Product, ProductAdmin)


class OfferAdmin(admin.ModelAdmin):
    list_display = ['code', 'description', 'discount']


admin.site.register(Offer, OfferAdmin)