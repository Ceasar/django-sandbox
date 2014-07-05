import os
import sys

from django.conf import settings
from django.conf.urls import patterns
from django.core.management import execute_from_command_line

BASE_PATH = os.path.dirname(__file__)

settings.configure(
    DEBUG=True,
    SECRET_KEY='placerandomsecretkeyhere',
    ROOT_URLCONF=sys.modules[__name__],
    TEMPLATE_DIRS=(
        os.path.join(BASE_PATH, "templates"),
    )
)

from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {'request': request})

urlpatterns = patterns(
    '',
    (r'^$', index),
)


if __name__ == "__main__":
    execute_from_command_line(sys.argv)
