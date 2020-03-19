
from django.contrib import admin
from .models import Profile

'''
class ProfileAdmin(admin.ModelAdmin):
    filter_horizontal = ('hasLiked',)
'''

admin.site.register(Profile)
