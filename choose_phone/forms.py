from datetime import date

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_number(value):
    try:
        int(value)
    except ValueError:
        raise ValidationError(
            _('Введите целое число.'),
            params={'value': value},
        )


class BlankForm(forms.Form):
    pass


class FavoriteNumberForm(forms.Form):
    number = forms.CharField(label="Введите до 4-х цифр", max_length=4,
                             widget=forms.TextInput(
                                 attrs={'class': 'form-control onlyNumber'}),
                             validators=[validate_number])


class BeautifulTailForm(forms.Form):
    number1 = forms.CharField(label="Введите 4 цифры", max_length=1,
                              widget=forms.TextInput(
                                  attrs={'class': 'onlyNumber small-input'}),
                              validators=[validate_number], required=False)
    number2 = forms.CharField(max_length=1,
                              widget=forms.TextInput(
                                  attrs={'class': 'onlyNumber small-input'}),
                              validators=[validate_number], required=False)
    number3 = forms.CharField(max_length=1,
                              widget=forms.TextInput(
                                  attrs={'class': 'onlyNumber small-input'}),
                              validators=[validate_number], required=False)
    number4 = forms.CharField(max_length=1,
                              widget=forms.TextInput(
                                  attrs={'class': 'onlyNumber small-input'}),
                              validators=[validate_number], required=False)


class SelectionByWordForm(forms.Form):
    word = forms.CharField(label="Введите маску:", max_length=6,
                           widget=forms.TextInput(
                               attrs={'class': 'form-control'}))


class SelectionByDateForm(forms.Form):
    day_choices = [(day, day) for day in range(1, 32)]
    day_choices.insert(0, ('', 'День'))
    month_choices = [(day, day) for day in range(1, 13)]
    month_choices.insert(0, ('', 'Месяц'))
    current_year = date.today().year
    start_year = current_year - 100
    end_year = current_year + 1
    year_choices = [(day, day) for day in range(start_year, end_year)]
    year_choices.append(('', 'Год'))
    year_choices = reversed(year_choices)
    day = forms.ChoiceField(label="Укажите любимую дату:", widget=forms.Select(
        attrs={'class': 'small-select'}), choices=day_choices, required=False)
    month = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'small-select'}),
        choices=month_choices, required=False)
    year = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'small-select'}),
        choices=year_choices, required=False)


class AllExceptNumberForm(forms.Form):
    number = forms.CharField(label="Введите до 4-х цифр", max_length=4,
                             widget=forms.TextInput(
                                 attrs={'class': 'form-control onlyNumber'}),
                             validators=[validate_number])


class SimilarNumberForm(forms.Form):
    number1 = forms.CharField(label="Введите семь цифр номера:", max_length=1,
                              widget=forms.TextInput(
                                  attrs={'class': 'small-input onlyNumber'}),
                              validators=[validate_number])
    number2 = forms.CharField(max_length=1, widget=forms.TextInput(
        attrs={'class': 'small-input onlyNumber'}),
                              validators=[validate_number])
    number3 = forms.CharField(max_length=1, widget=forms.TextInput(
        attrs={'class': 'small-input onlyNumber'}),
                              validators=[validate_number])
    number4 = forms.CharField(max_length=1, widget=forms.TextInput(
        attrs={'class': 'small-input onlyNumber'}),
                              validators=[validate_number])
    number5 = forms.CharField(max_length=1, widget=forms.TextInput(
        attrs={'class': 'small-input onlyNumber'}),
                              validators=[validate_number])
    number6 = forms.CharField(max_length=1, widget=forms.TextInput(
        attrs={'class': 'small-input onlyNumber'}),
                              validators=[validate_number])
    number7 = forms.CharField(max_length=1, widget=forms.TextInput(
        attrs={'class': 'small-input onlyNumber'}),
                              validators=[validate_number])


class MagicNumberForm(forms.Form):
    day_choices = [(day, day) for day in range(1, 32)]
    day_choices.insert(0, ('', 'День'))
    month_choices = [(day, day) for day in range(1, 13)]
    month_choices.insert(0, ('', 'Месяц'))
    current_year = date.today().year
    start_year = current_year - 100
    end_year = current_year + 1
    year_choices = [(day, day) for day in range(start_year, end_year)]
    year_choices.append(('', 'Год'))
    year_choices = reversed(year_choices)
    magic_day = forms.ChoiceField(
        label="Укажите дату рождения и узнайте своё магическое число:",
        widget=forms.Select(
            attrs={'class': 'small-select magic'}), choices=day_choices,
        required=False)
    magic_month = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'small-select magic'}),
        choices=month_choices, required=False)
    magic_year = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'small-select magic'}),
        choices=year_choices, required=False)
    magic_number = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'small-input', 'readonly': 'readonly'}),
        required=False)


class MaskForm(forms.Form):
    pass
