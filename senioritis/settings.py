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

MEDIA_ROOT = os.path.abspath('media')
MEDIA_URL = '/media/'

ROOT_URLCONF = 'senioritis.urls'

MINIFY_BUNDLES = {
    'css': {
        'senioritis': {
            'css/senioritis.scss',
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
        'PASSWORD': 'yoursql',
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
