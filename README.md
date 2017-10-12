# MP-Accounts

Django accounts app.

### Installation

Install with pip:

```sh
$ pip install -e git://github.com/pmaigutyak/mp-accounts.git#egg=mp-accounts
```

Add accounts to urls.py:

```
urlpatterns += i18n_patterns(
    
    url(r'^accounts/', include('allauth.urls')),

    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    
)
```

Add accounts to settings.py:
```
INSTALLED_APPS = [
    'accounts',
    'allauth',
    'allauth.account',
]

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

LOGIN_REDIRECT_URL = '/'
```

Run migrations:
```
$ python manage.py migrate
```

### Requirements

App require this packages:

* django-allauth
* django-widget-tweaks
