from django.contrib import admin
from . import models


admin.site.register(models.Bot)
admin.site.register(models.FolloweTags)
admin.site.register(models.FolloweLocations)
admin.site.register(models.FolloweUsernames)
admin.site.register(models.FollowFollower)
admin.site.register(models.FollowFollowing)
admin.site.register(models.FollowLikers)
admin.site.register(models.FollowCommenters)
admin.site.register(models.CommentLocations)
admin.site.register(models.IntractionUrl)
admin.site.register(models.IntractionUser)
admin.site.register(models.IntractionTags)
admin.site.register(models.IntractionFollowers)
admin.site.register(models.IntractionFollowing)
admin.site.register(models.IntractionCommenters)
admin.site.register(models.IntractionLikers)
admin.site.register(models.LikeTags)
admin.site.register(models.LikeLocations)
admin.site.register(models.StoryTags)
admin.site.register(models.StoryUsers)
admin.site.register(models.accounts)
admin.site.register(models.Comments)

admin.site.register(models.createstory)
admin.site.register(models.createpost)
admin.site.register(models.story)
admin.site.register(models.post)