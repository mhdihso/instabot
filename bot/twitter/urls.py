from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path('tweet-manager/<int:id>',views.statusmanager, name='status_text_manager') , 
    path('tweet-others/<int:id>',views.statusothers, name='status_text_others') , 
    path('like-timeline/<int:count>' ,views.liketimeline, name='liketimeline'),
    path('search-like-manager/<int:id>/<int:count>' , views.searchlikemanager , name='search-like-manager'),
    path('search-like-others/<int:id>/<int:count>' , views.searchlikeothers , name='search-like-others'),
    path('search-reply-manager/<int:id>/<int:count>' , views.searchreplymanager , name='search-reply-manager'),
    path('search-reply-others/<int:id>/<int:count>' , views.searchreplyothers , name='search-reply-others'),
    path('search-retweet-manager/<int:id>/<int:count>', views.searchretweetmanager , name='search-retweet-manager'),
    path('search-retweet-others/<int:id>/<int:count>', views.searchretweetothers , name='search-retweet-others'),
    path('search-follow-manager/<int:id>/<int:count>', views.searchfollowmanager , name='search-follow-manager'),
    path('search-follow-others/<int:id>/<int:count>', views.searchfollowothers , name='search-follow-others'),
    path('search-intraction-manager/<int:id>/<int:count>', views.searchintractionmanager , name='search-intraction-manager'),
    path('search-intraction-others/<int:id>/<int:count>', views.searchintractionothers , name='search-intraction-others'),
    path('search-send-direct-manager/<int:id>/<int:count>', views.searchsenddirectmanager , name='search-intraction-manager'),
    path('search-send-direct-others/<int:id>/<int:count>', views.searchsenddirectothers , name='search-intraction-others'),
    path('retweet-specific-tweet-manager/<int:tweet_id>',views.retweetmanager, name='retweetmanager'),
    path('retweet-specific-tweet-others/<int:tweet_id>',views.retweetothers, name='retweetothers'),
    path('like-specific-tweet-manager/<int:tweet_id>',views.likemanager, name='likemanager'),
    path('like-specific-tweet-others/<int:tweet_id>',views.likeothers, name='likeothers'),
    path('reply-specific-tweet-manager/<int:tweet_id>/<str:reply_text>',views.replymanager, name='replymanager'),
    path('reply-specific-tweet-others/<int:tweet_id>/<str:reply_text>',views.replyothers, name='replyothers'),
]