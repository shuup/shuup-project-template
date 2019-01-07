import os

import dj_database_url
import environ

env = environ.Env(DEBUG=(bool, False))

def optenv(var):
    return env(var, default=None)


root = environ.Path(__file__) - 3

BASE_DIR = root()

DEBUG = env('DEBUG')

env.read_env(os.path.join(BASE_DIR, 'shuup-project-template', '.env'))

SECRET_KEY = env('SECRET_KEY', default='xxx')

DATABASES = {'default': dj_database_url.config(default='sqlite:///db.sqlite3')}

MEDIA_URL = env('MEDIA_URL', default='/media/')
STATIC_URL = env('STATIC_URL', default='/static/')

MEDIA_ROOT = root(env('MEDIA_LOCATION', default=os.path.join(BASE_DIR, 'var', 'media')))
STATIC_ROOT = root(env('STATIC_LOCATION', default=os.path.join(BASE_DIR, 'var', 'static')))

SHUUP_HOME_CURRENCY = env('SHOP_CURRENCY', default='USD')

ALLOWED_HOSTS = env('ALLOWED_HOSTS', default='*').split(',')

EMAIL_CONFIG = env.email_url('EMAIL_URL', default='smtp://localhost:25')
vars().update(EMAIL_CONFIG)


INSTALLED_APPS = [
    # django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    # external apps that needs to be loaded before Shuup
    'easy_thumbnails',
    # shuup themes
    'shuup.themes.classic_gray',
    'business_logic',

    # shuup
    'shuup.core',
    'shuup.admin',
    'shuup.api',
    'shuup.addons',
    'shuup.default_tax',
    'shuup.front',
    'shuup.front.apps.auth',
    'shuup.front.apps.carousel',
    'shuup.front.apps.customer_information',
    'shuup.front.apps.personal_order_history',
    'shuup.front.apps.saved_carts',
    'shuup.front.apps.registration',
    'shuup.front.apps.simple_order_notification',
    'shuup.front.apps.simple_search',
    'shuup.front.apps.recently_viewed_products',
    'shuup.notify',
    'shuup.simple_cms',
    'shuup.customer_group_pricing',
    'shuup.campaigns',
    'shuup.simple_supplier',
    'shuup.order_printouts',
    'shuup.testing',
    'shuup.utils',
    'shuup.xtheme',
    'shuup.reports',
    'shuup.default_reports',
    'shuup.regions',
    'shuup.importer',
    'shuup.default_importer',
    'shuup.gdpr',
    'shuup.tasks',
    'shuup.discounts',
    'shuup_stripe',

    # external apps
    'bootstrap3',
    'django_countries',
    'django_jinja',
    'django_filters',
    'filer',
    'reversion',
    'registration',
    'rest_framework',
    'rest_framework_swagger'
]

MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'shuup.front.middleware.ProblemMiddleware',
    'shuup.core.middleware.ShuupMiddleware',
    'shuup.front.middleware.ShuupFrontMiddleware',
    'shuup.xtheme.middleware.XthemeMiddleware',
    'shuup.admin.middleware.ShuupAdminMiddleware'
]

ROOT_URLCONF = 'project.urls'
WSGI_APPLICATION = 'project.wsgi.application'
LANGUAGE_CODE = env('LANGUAGE_CODE', default='en')
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/login/'
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'
RAVEN_CONFIG = {'dsn': optenv('SENTRY_DSN')}

DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL', default='no-reply@myshuup.com')

SITE_ID = env('SITE_ID', default=1)

LANGUAGE_CHOICES = [
    ('en', 'English'),
    ('fi', 'Finnish'),
    ('it', 'Italian'),
    ('ja', 'Japanese'),
    ('pt-br', 'Brazilian Portuguese'),
    ('ru', 'Russian'),
    ('sv', 'Swedish'),
    ('zh-hans', 'Simplified Chinese'),
]

selected_languages = env('LANGUAGES', default='en,fi,ja,zh-hans,pt-br,it').split(',')
LANGUAGES = [(code, name) for code, name in LANGUAGE_CHOICES if code in selected_languages]

PARLER_DEFAULT_LANGUAGE_CODE = env('PARLER_DEFAULT_LANGUAGE_CODE', default='en')

PARLER_LANGUAGES = {
    None: [{'code': c, 'name': n} for (c, n) in LANGUAGES],
    'default': {'hide_untranslated': False}
}

_TEMPLATE_CONTEXT_PROCESSORS = [
    "django.contrib.auth.context_processors.auth",
    "django.template.context_processors.debug",
    "django.template.context_processors.i18n",
    "django.template.context_processors.media",
    "django.template.context_processors.static",
    "django.template.context_processors.request",
    "django.template.context_processors.tz",
    "django.contrib.messages.context_processors.messages"
]

TEMPLATES = [
    {
        "BACKEND": "django_jinja.backend.Jinja2",
        "APP_DIRS": True,
        "OPTIONS": {
            "match_extension": ".jinja",
            "context_processors": _TEMPLATE_CONTEXT_PROCESSORS,
            "newstyle_gettext": True,
            "environment": "shuup.xtheme.engine.XthemeEnvironment",
        },
        "NAME": "jinja2",
    },
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": _TEMPLATE_CONTEXT_PROCESSORS,
            "debug": DEBUG
        }
    },
]

CACHES = {'default': env.cache(default='memcache://127.0.0.1:11211?key_prefix=project')}

LOGIN_URL = "/login/"

SESSION_SERIALIZER = "django.contrib.sessions.serializers.PickleSerializer"

SHUUP_PRICING_MODULE = "customer_group_pricing"

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'shuup.api.permissions.ShuupAPIPermission',
    )
}

JWT_AUTH = {
    'JWT_ALLOW_REFRESH': True
}

SWAGGER_SETTINGS = {
    "SUPPORTED_SUBMIT_METHODS": [
        "get"
    ]
}

# extend the submit methods only if DEBUG is True
if DEBUG:
    SWAGGER_SETTINGS["SUPPORTED_SUBMIT_METHODS"].extend(["post", "patch", "delete", "put"])

SHUUP_SETUP_WIZARD_PANE_SPEC = [
    "shuup.admin.modules.shops.views:ShopWizardPane",
    "shuup.admin.modules.service_providers.views.PaymentWizardPane",
    "shuup.admin.modules.service_providers.views.CarrierWizardPane",
    "shuup.xtheme.admin_module.views.ThemeWizardPane",
    "shuup.admin.modules.content.views.ContentWizardPane",
    "shuup.admin.modules.sample_data.views.SampleObjectsWizardPane",
    "shuup.admin.modules.system.views.TelemetryWizardPane"
]


SHUUP_ERROR_PAGE_HANDLERS_SPEC = [
    "shuup.admin.error_handlers:AdminPageErrorHandler",
    "shuup.front.error_handlers:FrontPageErrorHandler"
]

SHUUP_SIMPLE_SEARCH_LIMIT = 150
