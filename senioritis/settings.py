import os
import site


ROOT = os.path.dirname(os.path.abspath(__file__))
path = lambda *a: os.path.join(ROOT, *a)
site.addsitedir(path('.'))

INSTALLED_APPS = (
    'course',
    'django_extensions'
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
