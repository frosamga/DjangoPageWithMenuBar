"""
Django settings for webs_abax project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# -*- coding: utf-8 -*-
import os
gettext = lambda s: s
PROJECT_PATH = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'hx!mmj@b%xcd=6rrg%662fs^hy3x+-t3$3q*33)hy2^2ef5ce8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SITE_ID = 1

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cms',
    'mptt',
    'menus',
    'south',
    'sekizai',

#    'cms.plugins.file',
    'cms.plugins.flash',
    'cms.plugins.googlemap',
    'cms.plugins.link',
#    'cms.plugins.picture',
    'cms.plugins.snippet',
 #   'cms.plugins.teaser',
    'cms.plugins.text',
#    'cms.plugins.video',
#    'cms.plugins.twitter',
#    'djangocms_twitter',

#    using filer instead of the commented apps
     'filer',
     'cmsplugin_filer_file',
     'cmsplugin_filer_folder',
     'cmsplugin_filer_image',
     'cmsplugin_filer_teaser',
     'cmsplugin_filer_video',

#    thumbnails for filer
     'easy_thumbnails',

#    app for content versioning
     'reversion',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
 #   'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'cms.context_processors.media',
    'sekizai.context_processors.sekizai',
)

ROOT_URLCONF = 'ocagestion.urls'

WSGI_APPLICATION = 'ocagestion.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

ROOT_PATH = os.path.dirname(__file__)

STATICFILES_DIRS = (
   os.path.abspath(os.path.join(ROOT_PATH, 'static')),
)

TEMPLATE_DIRS = (
   os.path.join(ROOT_PATH, "templates"),
)

CMS_TEMPLATES = (
    ('base.html', 'Base'),
)

LANGUAGES = [
     ('en', 'English'),
     ('es', 'Spanish'),
]

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
#    'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnails_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)
