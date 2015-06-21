from django.db import models
from datetime import datetime

# Create your models here.

class God(models.Model):
    god_name = models.CharField(max_length=100)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.god_name

class OfferType(models.Model):
    type_name = models.CharField(max_length=20)
    type_short = models.CharField(max_length=3)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self) :
        return "{0} ({1})".format(self.type_name, self.type_short)

class Offer(models.Model):
    offer_name = models.CharField(max_length=40)
    offer_price = models.DecimalField(max_digits=10, decimal_places=2)
    offer_god = models.ForeignKey(God)
    last_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self) :
        return "{0} ({1}) - {2}".format(self.offer_name, self.offer_god.god_name, self.offer_price)

class BillMeta(models.Model):
    billing_date = models.DateTimeField(auto_now=True)
    billing_type = models.ForeignKey(OfferType)
    last_updated = models.DateTimeField(auto_now=True)
    
    def __str__ (self):
        return str(self.id) 

class Bill(models.Model):
    bill_meta_id = models.ForeignKey(BillMeta)
    bill_name = models.CharField(max_length=100)
    bill_star = models.CharField(max_length=60)
    bill_offer = models.ForeignKey(Offer)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__ (self) :
        return "{0}\t{1}\t{2}".format(self.bill_name, self.bill_star, self.bill_offer.offer_name, self.bill_offer.offer_price)

