
from django.contrib import admin
from .models import Profile,CreatedBy

'''
class ProfileAdmin(admin.ModelAdmin):
    filter_horizontal = ('hasLiked',)
'''

admin.site.register(Profile)
admin.site.register(CreatedBy)
