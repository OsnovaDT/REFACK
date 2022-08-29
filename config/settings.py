"""Settings of the project"""

from os import path
from pathlib import Path

from decouple import config


# MAIN

ALLOWED_HOSTS = []

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    },
}

DEBUG = True

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Custom apps
    "account",
    "refactoring",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",

    # Custom middlewares
    "config.middleware.ExceptionHandlerMiddleware",
]

ROOT_URLCONF = "config.urls"

SECRET_KEY = config("SECRET_KEY")

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# INTERNATIONALIZATION

LANGUAGE_CODE = "ru"

TIME_ZONE = "Europe/Moscow"

USE_I18N = True

USE_TZ = True

# STATIC

STATICFILES_DIRS = (path.join(BASE_DIR, "static/"),)

STATIC_URL = "/static/"

# MEDIA

MEDIA_ROOT = path.join(BASE_DIR, "media")

MEDIA_URL = "/media/"

# LOGIN AND LOGOUT

LOGIN_REDIRECT_URL = "refactoring:index"

LOGIN_URL = "account:login"

LOGOUT_REDIRECT_URL = "account:login"

# LOGGING (loguru)

LOG_COMPRESSION = "zip"

LOG_FORMAT = "{level.icon} {level} {time:DD.MM.YYYY HH:mm:ss (Z)} {message}"

LOG_ROTATION = "1 MB"

# OTHERS

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation."
                "UserAttributeSimilarityValidator",
    },

    {
        "NAME": "django.contrib.auth.password_validation."
                "MinimumLengthValidator",
    },

    {
        "NAME": "django.contrib.auth.password_validation."
                "CommonPasswordValidator",
    },

    {
        "NAME": "django.contrib.auth.password_validation."
                "NumericPasswordValidator",
    },
]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

WSGI_APPLICATION = "config.wsgi.application"
