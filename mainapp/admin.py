from django.contrib import admin
from .models import Info
from .models import Person
from .models import Stuff

admin.site.register(Info)
admin.site.register(Person)
admin.site.register(Stuff)

