from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# ⚠️ SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-b@qzza*9#0e((kkb6(3b0xj*bus62tv1+54f7j#ztb7%0hwctp'

# ⚠️ DEBUG should be False in production
DEBUG = True

# ✅ Allow all hosts for now (change in production)
ALLOWED_HOSTS = ['*']


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',      # Admin panel (optional, can remove if not using superuser)
    'django.contrib.auth',       # Authentication system
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'notes',                     # Your app
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Required for login/logout
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Keep_It.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],   # ✅ Better: use BASE_DIR / 'templates'
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Keep_It.wsgi.application'


# Database (SQLite for dev, switch to PostgreSQL/MySQL in production)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# ✅ Password validation (good for production, fine to keep as is)
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


# ✅ Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# ✅ Static files settings
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / "static"]   # Optional: if you have a global /static folder

# ✅ Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# 🚀 Authentication redirects (important for login/logout system)
LOGIN_REDIRECT_URL = 'home'     # After login → redirect to home page
LOGOUT_REDIRECT_URL = 'login'   # After logout → redirect to login page
LOGIN_URL = 'login'             # If not logged in → redirect to login page
