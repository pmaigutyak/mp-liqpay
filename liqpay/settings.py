
from django.conf import settings

from liqpay.constants import CURRENCY_UAH, ACTION_PAY


LIQPAY_PUBLIC_KEY = getattr(settings, 'LIQPAY_PUBLIC_KEY', '')

LIQPAY_PRIVATE_KEY = getattr(settings, 'LIQPAY_PRIVATE_KEY', '')

LIQPAY_DEFAULT_CURRENCY = getattr(
    settings, 'LIQPAY_DEFAULT_CURRENCY', CURRENCY_UAH)

LIQPAY_DEFAULT_LANGUAGE = getattr(settings, 'LIQPAY_DEFAULT_LANGUAGE', 'uk')

LIQPAY_DEFAULT_ACTION = getattr(settings, 'LIQPAY_DEFAULT_ACTION', ACTION_PAY)
