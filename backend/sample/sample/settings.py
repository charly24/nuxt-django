import os

from configurations import Configuration, values


class Base(Configuration):
    IS_TEST = values.BooleanValue(False)
    DEBUG = values.BooleanValue(False)
    SECRET_KEY = values.SecretValue()

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    DATABASES = values.DatabaseURLValue()

    ALLOWED_HOSTS = []

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'rest_framework',
        'rest_framework.authtoken',
        'corsheaders',
        'djoser',
        'apps.account',
    ]

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'corsheaders.middleware.CorsMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    ROOT_URLCONF = 'sample.urls'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
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

    # WSGI

    WSGI_APPLICATION = 'sample.wsgi.application'

    # Password validators

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

    AUTH_USER_MODEL = 'account.User'

    # Internationalization

    LANGUAGE_CODE = 'ja-JP'
    TIME_ZONE = 'Asia/Tokyo'
    USE_I18N = True
    USE_L10N = True
    USE_TZ = True

    # Static files
    STATIC_URL = '/static/'
    STATIC_BASE = os.path.join(BASE_DIR, 'static')
    STATICFILES_DIRS = (
        STATIC_BASE,
    )

    # REST
    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework.authentication.TokenAuthentication',
            'rest_framework.authentication.BasicAuthentication',
            'rest_framework.authentication.SessionAuthentication',
        ),
        'DEFAULT_PAGINATION_CLASS':
        'rest_framework.pagination.PageNumberPagination',
        'PAGE_SIZE': 100,
    }

    DJOSER = {
        'SERIALIZERS': {
            'user': 'apps.account.serializers.CustomUserSerializer',
        }
    }


class Development(Base):
    DEBUG = values.BooleanValue(True)
    CORS_ORIGIN_ALLOW_ALL = True
    ALLOWED_HOSTS = ['localhost']
    INSTALLED_APPS = Base.INSTALLED_APPS + ['django_extensions']


class Production(Base):
    pass


class Testing(Base):
    pass
