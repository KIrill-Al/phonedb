from django.db.models import Q
from django.shortcuts import render

from choose_phone.forms import FavoriteNumberForm, BlankForm, BeautifulTailForm, \
    SelectionByWordForm, SelectionByDateForm, AllExceptNumberForm, \
    SimilarNumberForm, MagicNumberForm, MaskForm
from choose_phone.models import Phone

METAL_DICT = {'simple': 'Простые', 'silver': 'Серебрянные',
              'platinum': 'Платиновые'}
FORMS_DICT = {1: BlankForm, 2: FavoriteNumberForm, 3: BeautifulTailForm,
              4: SelectionByWordForm, 5: SelectionByDateForm,
              6: AllExceptNumberForm, 7: SimilarNumberForm, 8: MagicNumberForm,
              9: MaskForm}
TEMPLATES_DICT = {1: 'choose_phone/filters/inline/all.html',
                  2: 'choose_phone/filters/inline/favorite_number.html',
                  3: 'choose_phone/filters/inline/beautiful_tail.html',
                  4: 'choose_phone/filters/inline/selection_by_word.html',
                  5: 'choose_phone/filters/inline/selection_by_date.html',
                  6: 'choose_phone/filters/inline/favorite_number.html',
                  7: 'choose_phone/filters/inline/favorite_number.html',
                  8: 'choose_phone/filters/inline/favorite_number.html',
                  9: 'choose_phone/filters/inline/favorite_number.html'}


def index(request):
    count = Phone.objects.all().count()
    template = 'choose_phone/index.html'
    favorite_number_form = FavoriteNumberForm
    beautiful_tail_form = BeautifulTailForm
    selection_by_word_form = SelectionByWordForm
    selection_by_date_form = SelectionByDateForm
    context = {'count': count, 'favorite_number_form': favorite_number_form,
               'beautiful_tail_form': beautiful_tail_form,
               'selection_by_word_form': selection_by_word_form,
               'selection_by_date_form': selection_by_date_form}
    return render(request, template, context)


def all_numbers(request, form=None):
    text = "Полный список номеров, имеющихся в продаже в интернет-магазине."
    phones = Phone.objects.all()
    return phones, text


def favorite_number(request, number=None, negative=False, form=None):
    if form and form.is_valid():
        number = form.cleaned_data['number']
    text = "Воспользовавшись данным способом, вы можете подобрать номер, в " \
           "котором содержится ваше любимое число."
    regex = r'({})'.format(number)
    if negative:
        phones = Phone.objects.filter(~Q(number__iregex=regex)).all()
    else:
        phones = Phone.objects.filter(Q(number__iregex=regex)).all()

    return phones, text


def beautiful_tail(request, form=None):
    if form.is_valid():
        number1 = form.cleaned_data['number1']
        number2 = form.cleaned_data['number2']
        number3 = form.cleaned_data['number3']
        number4 = form.cleaned_data['number4']
    else:
        number1 = '.'
        number2 = '.'
        number3 = '.'
        number4 = '.'

    regex = r'{}{}{}{}$'.format(number1, number2, number3, number4)
    text = "При помощи этого способа вы можете подобрать номер по последним " \
           "четырем цифрам. Вы можете ввести от одной до четырех цифр. Если " \
           "цифра в каком-то поле не имеет для вас значения, оставьте поле " \
           "свободным. Укажите от одной до четырех цифр в окончании номера:"
    phones = Phone.objects.filter(Q(number__iregex=regex)).all()

    return phones, text


def selection_by_word(request, form=None):
    # Английский алфавит нужно?
    numpad = {2: ['а', 'б', 'в', 'г'], 3: ['д', 'e', 'ё', 'ж', 'з'],
              4: ['и', 'й', 'к', 'л'], 5: ['м', 'н', 'о', 'п'],
              6: ['р', 'с', 'т', 'у'], 7: ['ф', 'х', 'ц', 'ч'],
              8: ['ш', 'щ', 'ъ', 'ы'], 9: ['ь', 'э', 'ю', 'я']}
    if form.is_valid():
        word = tuple(form.cleaned_data['word'])
    else:
        word = ''
    number = ''

    for char in word:
        for key, char_list in numpad.items():
            if char in char_list:
                number += str(key)

    phone, text = favorite_number(request, number=number)

    text = "Этот способ подбора поможет вам найти номер, который легко " \
           "запомнить в виде имени, названия или любого слова, подставляя " \
           "вместо цифр - буквы, расположенные на клавишах телефона " \
           "(у большинства современных аппаратов эта раскладка одинаковая, " \
           "пример справа). Например, набрав на клавиатуре телефона «МегаФон», " \
           "вы увидите номер 532-27-55. Удобно запоминать и сочетания букв и " \
           "цифр, например: 1-ТАКСИ-1 (1-62464-1)."

    return phone, text


def selection_by_date(request, form):
    if form.is_valid():
        day = form.cleaned_data['day']
        month = form.cleaned_data['month']
        year = form.cleaned_data['year']
    else:
        day = ''
        month = ''
        year = ''

    print(day)
    print(month)
    print(year)
    regex1 = ''
    regex2 = ''
    regex_pattern1 = r'{:0>2}{:0>2}{}$'
    regex_pattern2 = r'{:0>2}{:0>2}'
    if day and month and year:
        print('first')
        regex1 = regex_pattern1.format(day, month, year[-2:])
    elif day and month:
        print('second')
        regex1 = regex_pattern2.format(day, month)
        regex2 = regex_pattern2.format(month, day)
        print(regex1)
        print(regex2)
    elif month and year:
        print('third')
        regex1 = regex_pattern2.format(month, year[:-2])
        regex2 = regex_pattern2.format(year[:-2], month)

    if regex2:
        print('regex2')
        phones = Phone.objects.filter(
            Q(number__iregex=regex1) | Q(number__iregex=regex2)).all()
    else:
        print('regex1')
        phones = Phone.objects.filter(Q(number__iregex=regex1)).all()
    print(phones)
    text = "Подберите номер, содержащий цифры важной для вас даты, например, " \
           "дня рождения или свадьбы. Просто укажите число, месяц, год и " \
           "выберите подходящий вам номер."

    return phones, text


def all_except_number(request, form):
    phone, text = favorite_number(request, negative=True)
    text = 'Европейцы избегают числа «13», японцы — «4», а у вас есть нелюбимая ' \
           'цифра или число? Введите его в форму и уберите из списка все номера, ' \
           'содержащие неприятные комбинации.'

    return phone, text


def similar_number(request, form):
    number1 = request.POST['number1']
    number2 = request.POST['number2']
    number3 = request.POST['number3']
    number4 = request.POST['number4']
    number5 = request.POST['number5']
    number6 = request.POST['number6']
    number7 = request.POST['number7']
    number1 = number1 if number1 else '.'
    number2 = number2 if number2 else '.'
    number3 = number3 if number3 else '.'
    number4 = number4 if number4 else '.'
    number5 = number5 if number5 else '.'
    number6 = number6 if number6 else '.'
    number7 = number7 if number7 else '.'
    regex = r'{}{}{}{}{}{}{}$'.format(number1, number2, number3, number4,
                                      number5, number6, number7)
    text = "Этот способ поможет вам подобрать один или несколько номеров, " \
           "похожих на тот, который вы укажете. Подобранные номера могут " \
           "содержать те же цифры, расположенные в другом порядке или отличаться " \
           "на несколько знаков. Впишите в поля семь цифр номера."
    phones = Phone.objects.filter(Q(number__iregex=regex)).all()

    return phones, text


def magic_number(request, form):
    pass


def mask(request, form):
    pass


FILTERS_DICT = {1: all_numbers, 2: favorite_number, 3: beautiful_tail,
                4: selection_by_word, 5: selection_by_date,
                6: all_except_number, 7: similar_number, 8: magic_number,
                9: mask}


def filter(request, id, metal_name=None):
    form = FORMS_DICT[id](request.POST)
    embedded_template = TEMPLATES_DICT[id]
    template = 'choose_phone/filter.html'

    filter = FILTERS_DICT[id]
    phones, text = filter(request, form=form)
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
        template = 'choose_phone/filter_metal.html'
        context = {'metal': metal, 'metal_count': metal.count(), 'text': text,
                   'metal_name': METAL_DICT[metal_name],
                   'metal_class': metal_name}
    else:
        context = {'simple': simple, 'count_simple': count_simple,
                   'silver': silver,
                   'count_silver': count_silver,
                   'platinum': platinum, 'count_platinum': count_platinum,
                   'count_all': count_all, 'text': text, 'form': form,
                   'embedded_template': embedded_template, 'id': id}
    return render(request, template, context)
