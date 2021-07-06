from django.contrib import admin
from .models import Todo

class Todo(admin.ModelAdmin):
  list = ('title', 'description', 'completed')

  admin.site.register(Todo)
