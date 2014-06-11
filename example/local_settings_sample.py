#-*- coding: utf-8 -*-

# THIS IS FOR DEVELOPMENT ENVIRONMENT, MOSTLY TO SPEED UP TESTS
# DO NOT USE IT IN PRODUCTION

import os
import sys


DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', ]

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# == Database ==
DATABASES = {
    #'default': {
    #    'ENGINE': 'django.db.backends.sqlite3',
    #    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    #}
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'swift_spirit',                      
        'USER': 'root',                      
        'PASSWORD': 'password',                  
        'HOST': '127.0.0.1',        
        'PORT': '3306',                      
    }
}


# == EMAIL ==
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


#EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.exmail.qq.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'noreply@swift.sh'
EMAIL_HOST_PASSWORD = 'password'
DEFAULT_FROM_EMAIL = u'Swift China<noreply@swift.sh>'

#EMAIL_PORT = 587
#EMAIL_HOST_USER = 'swiftshmail@gmail.com'
#EMAIL_HOST_PASSWORD = 'password'
#DEFAULT_FROM_EMAIL = u'Swift China <swiftshmail@gmail.com>'

#EMAIL_USE_TLS = True
#EMAIL_HOST = 'smtp.qq.com'
#EMAIL_PORT = 465
#EMAIL_HOST_USER = 'idevchina@qq.com'
#EMAIL_HOST_PASSWORD = 'password'

#EMAIL_HOST = 'smtp.qq.com'
#EMAIL_PORT = '25'
#EMAIL_HOST_USER = 'idevchina@qq.com'
#EMAIL_HOST_PASSWORD = 'password'
#DEFAULT_FROM_EMAIL = u'Swift China <idevchina@qq.com>'



CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
    'djconfig': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
}

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.SHA1PasswordHasher',
    'django.contrib.auth.hashers.MD5PasswordHasher',
    'django.contrib.auth.hashers.CryptPasswordHasher',
)


TESTING = 'test' in sys.argv

if TESTING:
    # Keep templates in memory
    TEMPLATE_LOADERS = (
        ('django.template.loaders.cached.Loader', (
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        )),
    )
else:
    TEMPLATE_LOADERS = (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )

