from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Profile)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "student_id",
        "name",
        "phone_number",
    )