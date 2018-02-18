from django.db.models import Q
from django.shortcuts import render

from choose_phone.models import Phone


def index(request):
    template = 'choose_phone/choose_phone.html'
    context = {'hello': 'hello'}
    return render(request, template, context)

def all_numbers(request):
    phones = Phone.objects.all()
    simple = phones.filter(~Q(number__iregex=r'(\d{2,3})\1$')).filter(~Q(number__iregex=r'0{3}$'))
    silver = phones.filter(number__iregex=r'(\d{2,3})\1$')
    platinum = phones.filter(number__iregex=r'0{3}$')
    print(simple)
    print(silver)
    print(platinum)
    pass

def filter(request):
    all_numbers(request)
    template = 'choose_phone/filter.html'
    context = {'hello': 'hello'}
    return render(request, template, context)
