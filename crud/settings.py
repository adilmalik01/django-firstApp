from pathlib import Path
import os

# Ye base directory ko resolve karne ke liye use hota hai, jahan se project ka root path define hota hai.
BASE_DIR = Path(__file__).resolve().parent.parent

# Development ke liye aasan settings - Ye production ke liye theek nahi hain.
# Hamesha production mein security cheezein activate karein.
SECRET_KEY = 'django-insecure-9ufz76i-#yfd5va9pm%f1l$%h@&!kr)wr1xh!m2cfbjd4h5t96'

# Debug ko production mein False rakhein, taki sensitive info expose na ho.
DEBUG = True  # Production ke liye ise False karna zaroori hai.

# ALLOWED_HOSTS mein aapka domain add karein jab production pe deploy karein.
ALLOWED_HOSTS = ['*']  # '*' development ke liye theek hai, lekin production mein specific host ya domain daalein.

# Installed apps mein wo saare apps hain jo aapke project mein istemal ho rahe hain.
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Home',  # Aapka Home app ka naam jo app directory mein hai.
]

# Middleware wo cheezein hain jo request ko handle karti hain.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # Ye session handle karne ke liye zaroori hai.
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Authentication ke liye zaroori hai.
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Ye aapke project's root url configuration ko specify karta hai.
ROOT_URLCONF = 'crud.urls'

# Templates ke liye directory define karna zaroori hai. 
# 'DIRS' mein aap manually templates directory ka path specify kar sakte hain.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Yahan custom templates ka path daalein.
        'APP_DIRS': True,  # Agar app-specific templates hain to ise True chhod dein.
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

# WSGI Application, production mein use hota hai. 
WSGI_APPLICATION = 'crud.wsgi.application'

# Database ke liye aap SQLite use kar rahe hain. 
# Production ke liye aap PostgreSQL ya MySQL consider kar sakte hain.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Ye password validation rules hain jo Django ke default hain. 
# Production mein password ke liye strong rules lagana zaroori hai.
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

# Internationalization settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Sessions aur Cookies ke settings.
SESSION_COOKIE_SAMESITE = 'Lax'  # Cross-origin ke liye agar zaroorat ho to ise 'None' kar sakte hain.
SESSION_COOKIE_SECURE = False  # Agar aap HTTPS pe ho to ise True kar dein.
SESSION_EXPIRE_AT_BROWSER_CLOSE = True  # Browser close hone pe session expire ho jayega.
SESSION_COOKIE_AGE = 3600  # Session expiry time, 1 hour (3600 seconds).

# Static files ka URL, CSS aur JS files ke liye zaroori hota hai.
STATIC_URL = 'static/'

# Production ke liye static files aur media ka proper path define karein.
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Production ke liye jab aap `collectstatic` use karte hain.
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Authentication ke liye zaroori URLs
LOGIN_URL = 'login/'  # Login page ka URL
LOGIN_REDIRECT_URL = '/'  # Login ke baad user ko home page pe redirect karna
LOGOUT_REDIRECT_URL = 'login/'  # Logout ke baad login page pe redirect karna


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
