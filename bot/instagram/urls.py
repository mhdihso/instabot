from django.urls import path
from .import views
from rest_framework import routers

# router = routers.SimpleRouter()

#add_data

# router.register(r'bot', views.BotViewSet)
# router.register(r'follow/users', views.FollowUsersViewSet)
# router.register(r'follow/tags', views.FollowTagsViewSet)
# router.register(r'follow/locations', views.FollowLocationsViewSet)
# router.register(r'follow/follower', views.FollowFollowerViewSet)
# router.register(r'follow/following', views.FollowFollowingViewSet)
# router.register(r'follow/intract_followers', views.FollowAndInntractFollowersViewset)
# router.register(r'follow/intract_following', views.FollowAndInntractFollowingViewset)
# router.register(r'follow/likers', views.FollowLikersViewSet)
# router.register(r'follow/commenters', views.FollowCommentersViewSet)

# router.register(r'comment/locations', views.CommentLocationViewSet)

# router.register(r'intraction/url', views.IntractionUrlViewSet)
# router.register(r'intraction/users', views.IntractionUserViewSet)
# router.register(r'intraction/tags', views.IntractionTagsViewSet)
# router.register(r'intraction/following', views.IntractionFollowingViewSet)
# router.register(r'intraction/followers', views.IntractionFollowersViewSet)
# router.register(r'intraction/likers', views.IntractionLikersViewSet)
# router.register(r'intraction/commenters', views.IntractionCommentersViewSet)

# router.register(r'like/tags', views.LikeTagsViewSet)
# router.register(r'like/locations', views.LikeLocationsViewSet)

# router.register(r'story/tags', views.StoryTagsViewSet)
# router.register(r'story/users', views.StoryUsersViewSet)

#call

urlpatterns = [
    path('call/follow/users', views.CallFollowUsers , name = 'follow-users'),
    path('call/follow/tags', views.CallFollowTags , name = 'follow-tags'),
    path('call/follow/locations', views.CallFollowLocations , name = 'follow-location'),
    path('call/follow/follower', views.CallFollowFollower , name = 'follow-followers'),
    path('call/follow/following', views.CallFollowFollowing , name = 'follow-following'),
    path('call/follow/intract_followers', views.CallFollowAndInntractFollowers , name = 'follow-intract-followers'),
    path('call/follow/intract_following', views.CallFollowAndInntractFollowing , name = 'follow-intract-following'),
    path('call/follow/likers', views.CallFollowLikers , name = 'follow-likers'),
    path('call/follow/commenters', views.CallFollowCommenters , name = 'follow-commenters'),
    path('call/comment/locations', views.CallCommentLocation , name = 'comment-location'),
    path('call/intraction/url', views.CallIntractionUrl , name = 'intraction-url'),
    path('call/intraction/users', views.CallIntractionUser , name = 'intraction-users'),
    path('call/intraction/tags', views.CallIntractionTags , name = 'intraction-tags'),
    path('call/intraction/following', views.CallIntractionFollowing , name = 'intraction-following'),
    path('call/intraction/followers', views.CallIntractionFollowers , name = 'intraction-followers'),
    path('call/intraction/likers', views.CallIntractionLikers , name = 'intraction-likers'),
    path('call/intraction/commenters', views.CallIntractionCommenters , name = 'intraction-commenters'),
    path('call/like/tags', views.CallLikeTags , name = 'like-tags'),
    path('call/like/locations', views.CallLikeLocations , name = 'like-location'),
    path('call/story/tags', views.CallStoryTags , name = 'story-tags'),
    path('call/story/users', views.CallStoryUsers , name = 'story-users'),
    path('send/story/<int:id>', views.sendstory,name='send-story'),
    path('send/post/<str:caption>/<int:id>', views.sendpost,name='send-post'),
    path('create/post/<int:id>',views.createpost , name = 'create-post'),
    path('create/story/<int:id>' , views.createstory , name = 'create-story')
]
# urlpatterns = router.urls
