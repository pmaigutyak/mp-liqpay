
import base64
import hashlib
import json

from urlparse import urljoin

from liqpay.settings import LIQPAY_PUBLIC_KEY, LIQPAY_PRIVATE_KEY
from liqpay.forms import ApiForm, CheckoutForm
from liqpay.exceptions import LiqPayValidationError


def to_unicode(s):
    """
    :param s:
    :return: unicode value (decoded utf-8)
    """
    if isinstance(s, unicode):
        return s

    if isinstance(s, basestring):
        return s.decode('utf-8', 'strict')

    if hasattr(s, '__unicode__'):
        return s.__unicode__()

    return unicode(bytes(s), 'utf-8', 'strict')


class LiqPay(object):

    host = 'https://www.liqpay.ua/api/'

    checkout_url = urljoin(host, '3/checkout/')

    def __init__(self, public_key, private_key):
        self._public_key = public_key
        self._private_key = private_key

    def get_checkout_form(self, **kwargs):

        params = self._clean_api_params(**kwargs)

        data = base64.b64encode(json.dumps(params))

        return CheckoutForm(self.checkout_url, data={
            'data': data,
            'signature': self._make_signature(data)
        })

    def str_to_sign(self, str):
        return base64.b64encode(hashlib.sha1(str).digest())

    def _clean_api_params(self, **kwargs):

        params = {
            'version': 3,
            'currency': settings.LIQPAY_DEFAULT_CURRENCY,
            'language': settings.LIQPAY_DEFAULT_LANGUAGE,
            'action': settings.LIQPAY_DEFAULT_ACTION,
            'public_key': self._public_key
        }

        params.update(kwargs)

        form = ApiForm(data=params)

        if not form.is_valid():
            raise LiqPayValidationError(
                'Invalid params: %s' % ', '.join(form.errors.keys()))

        return form.cleaned_data

    def _make_signature(self, data):

        params = [self._private_key, data, self._private_key]

        def smart_str(x): return to_unicode(x).encode('utf-8')

        joined_fields = ''.join(smart_str(x) for x in params)

        return base64.b64encode(hashlib.sha1(joined_fields).digest())


liqpay = LiqPay(settings.LIQPAY_PUBLIC_KEY, settings.LIQPAY_PRIVATE_KEY)
