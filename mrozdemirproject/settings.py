from pathlib import Path
import os
from django.utils.translation import gettext_lazy as _

# Proje kök dizini
BASE_DIR = Path(__file__).resolve().parent.parent

# Güvenlik için gizli anahtar (yerel ortamda varsayılan bir değer kullanıyoruz)
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'django-insecure-9kazuo3)@jxz4nav$e0c@0fx8=(s+iq8%h118a%x@j_r@j1po3')

# Hata ayıklama modu (yerel ortamda True)
DEBUG = True

# Yerel ortamda çalışırken localhost ve 127.0.0.1 ekliyoruz
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Yüklü uygulamalar
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'widget_tweaks',
    'portfolio',  # 'portfolio.apps.PortfolioConfig' yerine yalnızca 'portfolio' kullanıyoruz
]

# Middleware'ler
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URL yapılandırması
ROOT_URLCONF = 'mrozdemirproject.urls'

# Şablon ayarları
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

# WSGI uygulaması
WSGI_APPLICATION = 'mrozdemirproject.wsgi.application'

# Veritabanı (yerel ortamda SQLite kullanıyoruz)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Şifre doğrulama kuralları
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

# Dil ve saat dilimi ayarları
LANGUAGE_CODE = 'tr'  # Türkçe dil desteği
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Statik dosyalar
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Medya dosyaları
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Varsayılan otomatik alan tipi
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# settings.py sonuna ekle
LOGIN_REDIRECT_URL = 'home'  # Oturum açtıktan sonra yönlendirilecek URL
LOGOUT_REDIRECT_URL = 'home'  # Oturum kapattıktan sonra yönlendirilecek URL