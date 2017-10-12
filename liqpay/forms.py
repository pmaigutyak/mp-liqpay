
from django import forms
from django.conf.global_settings import LANGUAGES

from liqpay.constants import CURRENCIES, ACTIONS


class ApiForm(forms.Form):

    version = forms.IntegerField()

    public_key = forms.CharField(max_length=20, min_length=5)

    action = forms.ChoiceField(choices=ACTIONS)

    amount = forms.FloatField()

    currency = forms.ChoiceField(choices=CURRENCIES)

    description = forms.CharField()

    order_id = forms.CharField(max_length=255)

    result_url = forms.URLField()

    server_url = forms.URLField()

    language = forms.ChoiceField(choices=LANGUAGES)


class CheckoutForm(forms.Form):

    method = 'POST'

    def __init__(self, action, *args, **kwargs):
        self.action = action
        super(CheckoutForm, self).__init__(*args, **kwargs)

    data = forms.CharField(widget=forms.HiddenInput)
    signature = forms.CharField(widget=forms.HiddenInput)
