from django.contrib import admin
from .models import products,offer

class Productadmin(admin.ModelAdmin):
    list_display =('name','price','stock')
class offeradmin(admin.ModelAdmin):
    list_display =('code','discount')


# Register your models here.
admin.site.register(products,Productadmin)
admin.site.register(offer,offeradmin)