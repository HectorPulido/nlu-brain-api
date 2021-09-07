from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

admin.site.register(Key)
admin.site.register(Record)
