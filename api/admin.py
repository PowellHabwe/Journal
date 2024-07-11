from django.contrib import admin
from .models import Category, JournalPost


# Register your models here.
admin.site.register(Category)
admin.site.register(JournalPost)
