from django.contrib import admin

# Register your models here.
from .models import Question

#This registers the polls app models to be visible in the admins panel.
admin.site.register(Question)


