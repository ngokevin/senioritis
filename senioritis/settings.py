import os
import site

DEBUG = True
TEMPLATE_DEBUG = True

ROOT = os.path.dirname(os.path.abspath(__file__))
path = lambda *a: os.path.join(ROOT, *a)
site.addsitedir(path('.'))

SASS_PREPROCESS = True
SASS_BIN = '/usr/local/bin/sass'
JINGO_MINIFY_USE_STATIC = False

MEDIA_ROOT = '/home/ngoke/Code/senioritis/media/'
MEDIA_URL = '/media/'

ROOT_URLCONF = 'senioritis.urls'

MINIFY_BUNDLES = {
    'css': {
        'senioritis': {
            'css/senioritis.css',
        }
    },
    'js': {
        'senioritis': {
            'js/lib/jquery-1.8.3.min.js',
        }
    }
}

INSTALLED_APPS = (
    'course',

    'django_extensions',
    'jingo_minify',
)

DATABASES = {
    'default': {
        'HOST': 'localhost',
        'NAME': 'senioritis',
        'USER': 'root',
        'PASSWORD': 'amazonriver',
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'init_command': 'SET storage_engine=InnoDB;'
                            'SET foreign_key_checks = 0;',
        },
    },
}

TEMPLATE_DIRS = (
    path('templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = {
    'django.core.context_processors.request',
    'django.core.context_processors.csrf',
}

MIDDLEWARE_CLASSES = {
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
}

SECRET_KEY = 'abc'
