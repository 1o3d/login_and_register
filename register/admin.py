from django.contrib import admin
from .models import PersonalQuestions

from register.models import PersonalQuestions, Clipboard

# Register your models here.

admin.site.register(PersonalQuestions)
admin.site.register(Clipboard)

