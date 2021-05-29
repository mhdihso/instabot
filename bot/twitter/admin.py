from django.contrib import admin
from . import models

admin.site.register(models.Account)
admin.site.register(models.TweetMedia)
admin.site.register(models.searchlike)
admin.site.register(models.searchreply)
admin.site.register(models.searchretweet)
admin.site.register(models.searchfollow)
admin.site.register(models.searchintraction)
admin.site.register(models.searchdirectmassage)