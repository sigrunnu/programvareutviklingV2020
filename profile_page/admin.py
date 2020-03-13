from django.contrib import admin
from .models import OwnUser


class UserAdmin(admin.ModelAdmin):
    filter_horizontal = ('hasLiked',)


admin.site.register(OwnUser, UserAdmin)
