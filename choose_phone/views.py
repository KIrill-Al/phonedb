from django.db.models import Q
from django.shortcuts import render

from choose_phone.models import Phone

METAL_DICT = {'simple': 'Простые', 'silver': 'Серебрянные',
              'platinum': 'Платиновые'}


def index(request):
    count = Phone.objects.all().count()
    print(count)
    template = 'choose_phone/index.html'
    context = {'count': count}
    return render(request, template, context)


def all_numbers(request):
    text = "Полный список номеров, имеющихся в продаже в интернет-магазине."
    phones = Phone.objects.all()
    return phones, text


FILTERS_DICT = {1: all_numbers}


def filter(request, id, metal_name=None):
    all_numbers(request)
    filter = FILTERS_DICT[id]
    phones, text = filter(request)
    count_all = phones.count()
    simple = phones.filter(~Q(number__iregex=r'(\d{2,3})\1$')).filter(
        ~Q(number__iregex=r'0{3}$'))
    count_simple = simple.count()
    silver = phones.filter(number__iregex=r'(\d{2,3})\1$')
    count_silver = silver.count()
    platinum = phones.filter(number__iregex=r'0{3}$')
    count_platinum = platinum.count()
    metal_dict = {'simple': simple, 'silver': silver, 'platinum': platinum}
    if metal_name:
        metal = metal_dict[metal_name]
        context = {'metal': metal, 'metal_count': metal.count(), 'text': text,
                   'metal_name': METAL_DICT[metal_name], 'metal_class': metal_name}
        template = 'choose_phone/filter_metal.html'
    else:
        template = 'choose_phone/filter.html'
        context = {'simple': simple, 'count_simple': count_simple,
                   'silver': silver,
                   'count_silver': count_silver,
                   'platinum': platinum, 'count_platinum': count_platinum,
                   'count_all': count_all, 'text': text, 'id': id}
    return render(request, template, context)
