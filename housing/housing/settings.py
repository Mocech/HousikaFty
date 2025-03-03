import os
from pathlib import Path





# Build paths inside the project like this: BASE_DIR / 'subdir'.
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = Path(__file__).resolve().parent.parent


from dotenv import load_dotenv

load_dotenv()

SITE_ID = 3
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]


# Application definition

INSTALLED_APPS = [
    # 'jazzmin',
    'auth_system',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rentals',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
]  

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #django-allauth middleware
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'housing.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'housing.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


#Google Set up of Scopes
SOCIALACCOUNT_PROVIDERS = {
    "google": {
        # "APP": {
        #     "client_id": os.getenv("GOOGLE_CLIENT_ID", ""),
        #     "secret": os.getenv("GOOGLE_CLIENT_SECRET", ""),
        # },
        "scope": [
            "profile",
            "email"
        ],
        "AUTH_PARAMS":{"access_type":"online"}
        
    }
}



# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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


AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
     'allauth.account.auth_backends.AuthenticationBackend',
    
    
 )

# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
    
    ] 

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') 


MEDIA_URL = '/media/'

# MEDIA_ROOT = os.path.join(BASE_DIR,'media')

MEDIA_ROOT = os.path.join(BASE_DIR,'media')

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


AUTH_USER_MODEL = 'auth_system.CustomUser'

LOGIN_REDIRECT_URL = 'home'

# Email configuration


ACCOUNT_EMAIL_VERIFICATION = "mandatory"  # Default

# # Specify Google authentication settings
# GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
# GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')
# SOCIALACCOUNT_LOGIN_ON_GET = True 


VERIFICATION_EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
VERIFICATION_EMAIL_HOST = 'smtp.gmail.com'
VERIFICATION_EMAIL_PORT = 587
VERIFICATION_EMAIL_USE_TLS = True
VERIFICATION_EMAIL_HOST_USER = os.getenv('VERIFICATION_EMAIL_HOST_USER')
VERIFICATION_EMAIL_HOST_PASSWORD =os.getenv('VERIFICATION_EMAIL_HOST_PASSWORD')
ACCOUNT_DEFAULT_HTTP_PROTOCOL = "http"



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True  
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = 'MoxienTechs'
ACCOUNT_EMAIL_SUBJECT_PREFIX = '' # The subject-line prefix to use for email messages sent. 
ACCOUNT_EMAIL_REQUIRED = True



# ACCOUNT_LOGIN_METHODS = {'email'} 
# ACCOUNT_USERNAME_REQUIRED = False
# ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_EMAIL_VERIFICATION = "optional"


PASSWORD_RESET_TIMEOUT = 3600  # 1 hour (optional)


# Redirects
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"
# ACCOUNT_LOGOUT_REDIRECT_URL = "/accounts/login/" # Change this to your actual login page
# LOGOUT_REDIRECT_URL = "/accounts/login/"

# ACCOUNT_USER_MODEL_USERNAME_FIELD = None
# ACCOUNT_EMAIL_SUBJECT_PREFIX = "[HousikaFty] "

SOCIALACCOUNT_LOGIN_ON_GET = True
SOCIALACCOUNT_ADAPTER = "auth_system.adapters.CustomSocialAccountAdapter"


from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
    messages.ERROR: "alert-danger",
    messages.SUCCESS: "alert-success",
}

