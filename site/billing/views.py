from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import BillMeta,Bill

# Create your views here.

def index(request) :
    last_entries = BillMeta.objects.order_by('-billing_date')[:5]
    context = {'last_entries': last_entries}
    return render(request, 'billing/index.html', context) 

def new_entry(request):
    return HttpResponse("You are trying to create a new Bill")

def detail(request, billing_id):
    try:
        bill_meta = BillMeta.objects.get(pk=billing_id)    
        bill_entries = bill_meta.bill_set.all()
        total = 0
        for entry in bill_entries
            total = total + entry.bill_offer.offer_price 
    
    except BillMeta.DoesNotExist:
        raise Http404('Bill number {0} does not exist.'.format(billing_id))

    context = {'bill_meta' : bill_meta, 'bill_entries': bill_entries, 'total': total}
    return render(request, 'billing/detail.html', context)
        


