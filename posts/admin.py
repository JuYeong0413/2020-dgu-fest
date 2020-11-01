from django.contrib import admin
from .models import *

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "get_user_name",
        "get_student_id",
        "get_phone_number",
        "category",
        "title",
        "mediafile",
        "number_of_likes",
    )

    def number_of_likes(self, obj):
        return obj.like_count
    number_of_likes.admin_order_field = 'like'

    def get_user_name(self, obj):
        return obj.user.profile.name
    get_user_name.short_description = 'User Name'

    def get_student_id(self, obj):
        return obj.user.profile.student_id
    get_student_id.short_description = 'Student Id'

    def get_phone_number(self, obj):
        return obj.user.profile.phone_number
    get_phone_number.short_description = 'Phone Number'


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "get_student_id",
        "post",
        "created_at",
    )

    def get_student_id(self, obj):
      return obj.user.profile.student_id
    get_student_id.short_description = 'Student Id'
