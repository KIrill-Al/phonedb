from django.db.models import Q
from django.shortcuts import render

from choose_phone.models import Phone

METAL_DICT = {'simple': 'Простые', 'silver': 'Серебрянные',
              'platinum': 'Платиновые'}


def index(request):
    count = Phone.objects.all().count()
    template = 'choose_phone/index.html'
    context = {'count': count}
    return render(request, template, context)


def all_numbers(request):
    text = "Полный список номеров, имеющихся в продаже в интернет-магазине."
    phones = Phone.objects.all()
    return phones, text


def favorite_number(request):
    number = request.POST['favorite_number']
    text = "Воспользовавшись данным способом, вы можете подобрать номер, в " \
           "котором содержится ваше любимое число."
    regex = r'({})'.format(number)
    phones = Phone.objects.filter(Q(number__iregex=regex)).all()
    return phones, text


def beautiful_tail(request):
    token, number1, number2, number3, number4 = request.POST.values()
    number1 = number1 if number1 else '.'
    number2 = number2 if number2 else '.'
    number3 = number3 if number3 else '.'
    number4 = number4 if number4 else '.'
    regex = r'{}{}{}{}$'.format(number1, number2, number3, number4)
    text = "При помощи этого способа вы можете подобрать номер по последним " \
           "четырем цифрам. Вы можете ввести от одной до четырех цифр. Если " \
           "цифра в каком-то поле не имеет для вас значения, оставьте поле " \
           "свободным. Укажите от одной до четырех цифр в окончании номера:"
    phones = Phone.objects.filter(Q(number__iregex=regex)).all()
    return phones, text


def selection_by_word(request):
    numpad = {2: ['а', 'б', 'в', 'г'], 3: ['д', 'e', 'ё', 'ж', 'з'],
              4: ['и', 'й', 'к', 'л'], 5: ['м', 'н', 'о', 'п'],
              6: ['р', 'с', 'т', 'у'], 7: ['ф', 'х', 'ц', 'ч'],
              8: ['ш', 'щ', 'ъ', 'ы'], 9: ['ь', 'э', 'ю', 'я']}
    word = tuple(request.POST['word'])
    number = ' '

    for char in word:
        for key, char_list in numpad.items():
            if char in char_list:
                number.join(str(key))
                print(number)

    print('this is number: {}'.format(number))

    regex = ''
    text = "Этот способ подбора поможет вам найти номер, который легко " \
           "запомнить в виде имени, названия или любого слова, подставляя " \
           "вместо цифр - буквы, расположенные на клавишах телефона " \
           "(у большинства современных аппаратов эта раскладка одинаковая, " \
           "пример справа). Например, набрав на клавиатуре телефона «МегаФон», " \
           "вы увидите номер 532-27-55. Удобно запоминать и сочетания букв и " \
           "цифр, например: 1-ТАКСИ-1 (1-62464-1)."
    pass


FILTERS_DICT = {1: all_numbers, 2: favorite_number, 3: beautiful_tail,
                4: selection_by_word}


def filter(request, id, metal_name=None):
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
                   'metal_name': METAL_DICT[metal_name],
                   'metal_class': metal_name}
        template = 'choose_phone/filter_metal.html'
    else:
        template = 'choose_phone/filter.html'
        context = {'simple': simple, 'count_simple': count_simple,
                   'silver': silver,
                   'count_silver': count_silver,
                   'platinum': platinum, 'count_platinum': count_platinum,
                   'count_all': count_all, 'text': text, 'id': id}
    return render(request, template, context)
