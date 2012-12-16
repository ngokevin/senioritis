INSTALLED_APPS = (
    'course'
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
