import os
import sys

from django.conf import settings
from django.conf.urls import include, patterns
from django.core.management import execute_from_command_line

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
BASE_PATH = os.path.dirname(__file__)

settings.configure(
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    },
    DEBUG=True,
    INSTALLED_APPS=(
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.staticfiles',
    ),
    SECRET_KEY='placerandomsecretkeyhere',
    STATIC_URL='/static/',
    ROOT_URLCONF=sys.modules[__name__],
    TEMPLATE_DIRS=(
        os.path.join(BASE_PATH, "templates"),
    )
)


from django.contrib import admin
from django.shortcuts import render

admin.autodiscover()


def index(request):
    return render(request, 'index.html', {'request': request})

urlpatterns = patterns(
    '',
    (r'^$', index),
    (r'^admin/', include(admin.site.urls)),
)


if __name__ == "__main__":
    execute_from_command_line(sys.argv)
