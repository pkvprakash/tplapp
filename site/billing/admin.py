from django.contrib import admin

from .models import Offer, OfferType, God

# Register your models here.

class OfferAdmin(admin.ModelAdmin):
    list_display = ('offer_name', 'offer_god', 'offer_price', 'last_updated')

class OfferTypeAdmin(admin.ModelAdmin):
    list_display = ('type_name', 'type_short')

admin.site.register(Offer, OfferAdmin)
admin.site.register(OfferType, OfferTypeAdmin)
admin.site.register(God)
