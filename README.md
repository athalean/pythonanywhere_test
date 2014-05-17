pythonanywhere_test
===================

Trying to find out how to host stuff on pythonanywhere.com

Production has its own `settings.py`, but here is the essential change, apart from the different `SECRET_KEY` and `DEBUG=False`:

    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'athalean$default',
        'USER' : 'athalean',
        'PASSWORD': password-goes-here,
        'HOST': 'mysql.server',
        }
    }
