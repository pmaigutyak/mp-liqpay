# MP-LiqPay

Django liqpay integration app.

### Installation

Install with pip:
```sh
$ pip install django-liqpay
```

App settings:
```
REQUIRED:

# Public_key - the identifier of the created company. For example: i00000000
LIQPAY_PUBLIC_KEY = '*********'

# Private key of the created company (not available to anyone except your developer). 
# For example: a4825234f4bae72a0be04eafe9e8e2bada209255
LIQPAY_PRIVATE_KEY = '***********************************'

OPTIONAL:

# Payment currency. Example value: USD, EUR, RUB, UAH, BYN, KZT. 
# Additional currencies can be added by company's request.
# Default: UAH
LIQPAY_DEFAULT_CURRENCY = '***'

# Language code
# Default: uk
LIQPAY_DEFAULT_LANGUAGE = '**'

# Transaction type. Possible values: pay - payment, hold - amount of hold on sender's account, 
# subscribe - regular payment, paydonate - donation, auth - card preauth
# Default: pay
LIQPAY_DEFAULT_ACTION = '***'
```

## Usage example
views.py
```
checkout_form = liqpay.get_checkout_form(
    amount=12.4,
    order_id=1,
    description=_('Provision of services'),
    result_url='http://example.com',
    server_url='http://example.com',
    language='en'
)
```

template.html
```
<form action="{{ checkout_form.action }}" method="{{ checkout_form.method }}" target="_blank">
    {{ checkout_form }}
    <button type="submit" class="btn btn-success pull-left">
        <i class="fa fa-credit-card"></i>
        {% trans 'Pay' %}
    </button>
</form>
```

### Requirements

App require this packages:
* django
