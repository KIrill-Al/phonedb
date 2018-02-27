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


class TailForm(forms.Form):
    number1 = forms.CharField(label="Введите 4 цифры", max_length=1,
                              widget=forms.TextInput(
                                  attrs={'class': 'form-control onlyNumber'}),
                              validators=[validate_number])
    number2 = forms.CharField(label="Введите 4 цифры", max_length=1,
                              widget=forms.TextInput(
                                  attrs={'class': 'form-control onlyNumber'}),
                              validators=[validate_number])
    number3 = forms.CharField(label="Введите 4 цифры", max_length=1,
                              widget=forms.TextInput(
                                  attrs={'class': 'form-control onlyNumber'}),
                              validators=[validate_number])
    number4 = forms.CharField(label="Введите 4 цифры", max_length=1,
                              widget=forms.TextInput(
                                  attrs={'class': 'form-control onlyNumber'}),
                              validators=[validate_number])
    number5 = forms.CharField(label="Введите 4 цифры", max_length=1,
                              widget=forms.TextInput(
                                  attrs={'class': 'form-control onlyNumber'}),
                              validators=[validate_number])
    number6 = forms.CharField(max_length=1,
                              widget=forms.TextInput(
                                  attrs={'class': 'form-control onlyNumber'}),
                              validators=[validate_number])
    number7 = forms.CharField(max_length=1,
                              widget=forms.TextInput(
                                  attrs={'class': 'form-control onlyNumber'}),
                              validators=[validate_number])
    number8 = forms.CharField(max_length=1,
                              widget=forms.TextInput(
                                  attrs={'class': 'form-control onlyNumber'}),
                              validators=[validate_number])
