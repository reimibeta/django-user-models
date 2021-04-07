"""
Django settings for main project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from datetime import timedelta
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'it%$auom5nbd&tap0e@w*um&utoi$#_io(#81mb0ekhrprzpgu'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # django rest-framework
    'rest_framework',
    # user
    'user_models.apps.UsersConfig',
    # wallets
    'wallet_models.apps.WalletConfig',
    # pcr modules
    # suppliers
    'pcr_models.suppliers.suppliers.apps.SuppliersConfig',
    # staffs
    'pcr_models.staffs.staffs.apps.StaffsConfig',
    'pcr_models.staffs.staff_groups.apps.StaffGroupsConfig',
    'pcr_models.staffs.staff_group_payments.apps.StaffGroupPaymentsConfig',  # install it with wallet modules
    # branches
    'pcr_models.branches.branches.apps.BranchConfig',
    # customers
    'pcr_models.customers.customers.apps.CustomersConfig',
    # products
    'pcr_models.products.products.apps.ProductsConfig',
    'pcr_models.products.product_stocks.apps.ProductStocksConfig',
    'pcr_models.products.product_supplies.apps.ProductSuppliesConfig',
    'pcr_models.products.product_builds.apps.ProductBuildsConfig',
    # items
    'pcr_models.items.items.apps.ItemsConfig',
    'pcr_models.items.item_stocks.apps.ItemStocksConfig',
    'pcr_models.items.item_suppliers.apps.ItemSuppliersConfig',
    'pcr_models.items.item_purchases.apps.ItemPurchasesConfig',
    'pcr_models.items.item_uses.apps.ItemUsesConfig',
    # orders
    'pcr_models.orders.orders.apps.OrdersConfig',
    # revenues
    # 'pcr_models.revenues.revenues.apps.RevenuesConfig',
    # Clean-Up
    'django_cleanup.apps.CleanupConfig',  # should go after your apps
    # Filter
    'django_admin_listfilter_dropdown',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'main.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'app/static')
]

# Media Folder Settings
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media').replace('\\', '/')
MEDIA_URL = '/media/'
try:
    from .local_settings import *
except ImportError:
    pass

# handle upload with permission
FILE_UPLOAD_PERMISSIONS = 0o644
# AUTH
AUTH_USER_MODEL = 'user_models.User'
# Django-Rest-FrameWork
REST_FRAMEWORK = {
    # this bit makes the magic.
    'DEFAULT_RENDERER_CLASSES': (
        # UnicodeJSONRenderer has an ensure_ascii = False attribute,
        # thus it will not escape characters.
        # 'rest_framework_utils.rest_framework.renders.UTF8JSONRender',
        'rest_framework_utils.renders.UTF8JSONRender',
        # You only need to keep this one if you're using the browsable API
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    # 'EXCEPTION_HANDLER': 'applications.users.custom_exception_handler.custom_exception_handler'
}

# JWT_AUTH = {
#     'JWT_VERIFY_EXPIRATION': False,
# }
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=50),
    'REFRESH_TOKEN_LIFETIME': timedelta(minutes=60),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,

    # 'ALGORITHM': 'HS256',
    # 'SIGNING_KEY': settings.SECRET_KEY,
    # 'VERIFYING_KEY': None,
    # 'AUDIENCE': None,
    # 'ISSUER': None,

    # 'AUTH_HEADER_TYPES': ('Bearer',),
    # 'USER_ID_FIELD': 'id',
    # 'USER_ID_CLAIM': 'user_id',
    #
    # 'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    # 'TOKEN_TYPE_CLAIM': 'token_type',
    #
    # 'JTI_CLAIM': 'jti',
    #
    # 'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    # 'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    # 'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}
