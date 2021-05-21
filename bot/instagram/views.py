import os
import random
import datetime
import arabic_reshaper
from bidi.algorithm import get_display
from django.http import HttpResponse
from instapy import InstaPy, smart_run
from PIL import Image, ImageDraw, ImageFont
from rest_framework import permissions, viewsets

from . import models, serialaizers

# class Accountzz(viewsets.ModelViewSet):
#     queryset = models.accounts.objects.allView()
#     serializer_class = serialaizers.AccountSerialaizer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# class BotViewSet(viewsets.ModelViewSet):
#     queryset = models.Bot.objects.all()
#     serializer_class = serialaizers.BotSerialaizer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# class FollowUsersViewSet(viewsets.ModelViewSet):
#     queryset = models.FolloweUsernames.objects.all()
#     liest = queryset
#     f= list()
#     for i in liest:
#         f.append(i)
#     print(f)
#     serializer_class = serialaizers.FolloweUsernamesSerialaizer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# class FollowTagsViewSet(viewsets.ModelViewSet):
#     queryset = models.FolloweTags.objects.all()
#     serializer_class = serialaizers.FolloweTagsSerialaizer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# class FollowLocationsViewSet(viewsets.ModelViewSet):
#     queryset = models.FolloweLocations.objects.all()
#     serializer_class = serialaizers.FolloweLocationsSerialaizer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# class FollowFollowerViewSet(viewsets.ModelViewSet):
#     queryset = models.FollowFollower.objects.all()
#     serializer_class = serialaizers.FollowFollowerSerialaizer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# class FollowFollowingViewSet(viewsets.ModelViewSet):
#     queryset = models.FollowFollowing.objects.all()
#     serializer_class = serialaizers.FollowFollowingSerialaizer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# class FollowLikersViewSet(viewsets.ModelViewSet):
#     queryset = models.FollowLikers.objects.all()
#     serializer_class = serialaizers.FollowLikersSerialaizer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# class FollowCommentersViewSet(viewsets.ModelViewSet):
#     queryset = models.FollowCommenters.objects.all()
#     serializer_class = serialaizers.FollowCommentersSerialaizer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# class FollowAndInntractFollowersViewset(viewsets.ModelViewSet):
#     queryset = models.FollowAndInntractFollowers.objects.all()
#     serializer_class = serialaizers.FollowAndInntractFollowersSerialaizer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# class FollowAndInntractFollowingViewset(viewsets.ModelViewSet):
#     queryset = models.FollowAndInntractFollowing.objects.all()
#     serializer_class = serialaizers.FollowAndInntractFollowingSerialaizer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# class CommentLocationViewSet(viewsets.ModelViewSet):
#     queryset = models.CommentLocations.objects.all()
#     serializer_class = serialaizers.CommentLocationsSerialaizer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# class IntractionUrlViewSet(viewsets.ModelViewSet):
#     queryset = models.IntractionUrl.objects.all()
#     serializer_class = serialaizers.IntractionUrlSerialaizer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# class IntractionUserViewSet(viewsets.ModelViewSet):
#     queryset = models.IntractionUser.objects.all()
#     serializer_class = serialaizers.IntractionUserSerialaizer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# class IntractionTagsViewSet(viewsets.ModelViewSet):
#     queryset = models.IntractionTags.objects.all()
#     serializer_class = serialaizers.IntractionTagsSerialaizer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# class IntractionFollowingViewSet(viewsets.ModelViewSet):
#     queryset = models.IntractionFollowing.objects.all()
#     serializer_class = serialaizers.IntractionFollowingSerialaizer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# class IntractionFollowersViewSet(viewsets.ModelViewSet):
#     queryset = models.IntractionFollowers.objects.all()
#     serializer_class = serialaizers.IntractionFollowersSerialaizer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# class IntractionLikersViewSet(viewsets.ModelViewSet):
#     queryset = models.IntractionLikers.objects.all()
#     serializer_class = serialaizers.IntractionLikersSerialaizer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# class IntractionCommentersViewSet(viewsets.ModelViewSet):
#     queryset = models.IntractionCommenters.objects.all()
#     serializer_class = serialaizers.IntractionCommentersSerialaizer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# class LikeTagsViewSet(viewsets.ModelViewSet):
#     queryset = models.LikeTags.objects.all()
#     serializer_class =serialaizers.LikeTagsSerialaizer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# class LikeLocationsViewSet(viewsets.ModelViewSet):
#     queryset = models.LikeLocations.objects.all()
#     serializer_class = serialaizers.LikeLocationsSerialaizer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# class StoryTagsViewSet(viewsets.ModelViewSet):
#     queryset = models.StoryTags.objects.all()
#     serializer_class = serialaizers.StoryTagsSerialaizer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# class StoryUsersViewSet(viewsets.ModelViewSet):
#     queryset = models.StoryUsers.objects.all()
#     serializer_class = serialaizers.StoryUsersSerialaizer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]


def CallFollowUsers(request):
    skip_top_posts = bool(random.getrandbits(1))
    randomaize = bool(random.getrandbits(1))
    amount = random.randrange(20 , 30)
    sleep_delay = random.randrange(400 , 800)
    photos_grab_amount = random.randrange(2 , 6)
    follow_likers_per_photo = random.randrange(2 , 6)
    max_pic = random.randrange(100 , 365)

    all_users= models.FolloweUsernames.objects.all()
    accs= models.accounts.objects.all()
    objects = list()
    for i in all_users:
        p= i.name
        objects.append(p)
    for ac in accs:
        u = ac.username
        p = ac.password
        session = InstaPy (username= u, password = p)
        try:
            with  smart_run(session):
                session.follow_by_list(objects,times=1, sleep_delay=sleep_delay, interact=False)
                session.set_skip_users(skip_private=False)
        except :
            import traceback
            print(traceback.format_exc())
            pass

    response = """done....."""
    return HttpResponse(response)

def CallFollowTags(request):
    skip_top_posts = bool(random.getrandbits(1))
    randomaize = bool(random.getrandbits(1))
    amount = random.randrange(20 , 30)
    sleep_delay = random.randrange(200 , 600)
    photos_grab_amount = random.randrange(2 , 6)
    follow_likers_per_photo = random.randrange(2 , 6)
    max_pic = random.randrange(100 , 365)

    all_tags= models.FolloweTags.objects.all()
    accs= models.accounts.objects.all()
    objects = list()
    for i in all_tags:
        p= i.name
        objects.append(p)
    for ac in accs:
        u = ac.username
        p = ac.password
        session = InstaPy (username= u, password = p)
        print(objects)
        try:
            with  smart_run(session):
                session.follow_by_tags(objects, amount=amount ,randomize = randomaize , skip_top_posts= skip_top_posts)
                session.set_skip_users(skip_private=False)
        except :
            import traceback
            print(traceback.format_exc())
            pass
        
    response = """done....."""
    return HttpResponse(response)

def CallFollowLocations(request):
    skip_top_posts = bool(random.getrandbits(1))
    randomaize = bool(random.getrandbits(1))
    amount = random.randrange(20 , 30)
    sleep_delay = random.randrange(200 , 600)
    photos_grab_amount = random.randrange(2 , 6)
    follow_likers_per_photo = random.randrange(2 , 6)
    max_pic = random.randrange(100 , 365)

    all_loc= models.FolloweLocations.objects.all()
    accs= models.accounts.objects.all()
    objects = list()
    for i in all_loc:
        p= i.name
        objects.append(p)
    for ac in accs:
        u = ac.username
        p = ac.password
        session = InstaPy (username= u, password = p)
        try:
            with  smart_run(session):
                session.follow_by_locations(objects, amount=amount , skip_top_posts = skip_top_posts)
                session.set_skip_users(skip_private=False)
        except :
            import traceback
            print(traceback.format_exc())
            pass
        
    response = """done....."""
    return HttpResponse(response)

def CallFollowFollower(request):
    skip_top_posts = bool(random.getrandbits(1))
    randomaize = bool(random.getrandbits(1))
    amount = random.randrange(20 , 30)
    sleep_delay = random.randrange(200 , 600)
    photos_grab_amount = random.randrange(2 , 6)
    follow_likers_per_photo = random.randrange(2 , 6)
    max_pic = random.randrange(100 , 365)

    all_users_follower= models.FollowFollower.objects.all()
    accs= models.accounts.objects.all()
    objects = list()
    for i in all_users_follower:
        p= i.name
        objects.append(p)
    print(objects)
    for ac in accs:
        u = ac.username
        p = ac.password
        session = InstaPy (username= u, password = p )
        print(objects)
        try:
            with  smart_run(session):
                session.follow_user_followers(objects, amount=amount ,randomize = randomaize, sleep_delay=sleep_delay)
        except :
            import traceback
            print(traceback.format_exc())
            pass
        
    response = """done....."""
    return HttpResponse(response)

def CallFollowFollowing(request):
    skip_top_posts = bool(random.getrandbits(1))
    randomaize = bool(random.getrandbits(1))
    amount = random.randrange(20 , 30)
    sleep_delay = random.randrange(200 , 600)
    photos_grab_amount = random.randrange(2 , 6)
    follow_likers_per_photo = random.randrange(2 , 6)
    max_pic = random.randrange(100 , 365)

    all_users_following= models.FollowFollowing.objects.all()
    accs= models.accounts.objects.all()
    objects = list()
    for i in all_users_following:
        p= i.name
        objects.append(p)
    print(objects)
    for ac in accs:
        u = ac.username
        p = ac.password
        session = InstaPy (username= u, password = p)
        try:
            with  smart_run(session):
                session.follow_user_following(objects, amount=amount ,randomize = randomaize, sleep_delay=sleep_delay)
        except :
            import traceback
            print(traceback.format_exc())
            pass
        
    response = """done....."""
    return HttpResponse(response)

def CallFollowLikers(request):
    skip_top_posts = bool(random.getrandbits(1))
    randomaize = bool(random.getrandbits(1))
    amount = random.randrange(20 , 30)
    sleep_delay = random.randrange(200 , 600)
    photos_grab_amount = random.randrange(2 , 6)
    follow_likers_per_photo = random.randrange(2 , 6)
    max_pic = random.randrange(100 , 365)

    all_liker= models.FollowLikers.objects.all()
    accs= models.accounts.objects.all()
    objects = list()
    for i in all_liker:
        p= i.name
        objects.append(p)
    for ac in accs:
        u = ac.username
        p = ac.password
        session = InstaPy (username= u, password = p)
        print(objects)
        try:
            with  smart_run(session):
                session.follow_likers(objects, photos_grab_amount = photos_grab_amount, follow_likers_per_photo = follow_likers_per_photo, randomize=randomaize, sleep_delay=sleep_delay, interact=False)
                session.set_skip_users(skip_private=False)
        except :
            import traceback
            print(traceback.format_exc())
            continue
        
    response = """done....."""
    return HttpResponse(response)

def CallFollowCommenters(request):
    skip_top_posts = bool(random.getrandbits(1))
    randomaize = bool(random.getrandbits(1))
    amount = random.randrange(20 , 30)
    sleep_delay = random.randrange(200 , 600)
    photos_grab_amount = random.randrange(2 , 6)
    follow_likers_per_photo = random.randrange(2 , 6)
    max_pic = random.randrange(100 , 365)

    all_commenters= models.FollowCommenters.objects.all()
    accs= models.accounts.objects.all()
    objects = list()
    for i in all_commenters:
        p= i.name
        objects.append(p)
    for ac in accs:
        u = ac.username
        p = ac.password
        session = InstaPy (username= u, password = p)
        try:
            with  smart_run(session):
                session.follow_commenters(objects, amount=amount, daysold=365, max_pic = max_pic, sleep_delay=sleep_delay, interact=False)
                session.set_skip_users(skip_private=False) 
        except :
            import traceback
            print(traceback.format_exc())
            continue
        
    response = """done....."""
    return HttpResponse(response)

def CallFollowAndInntractFollowers(request):
    skip_top_posts = bool(random.getrandbits(1))
    randomaize = bool(random.getrandbits(1))
    amount = random.randrange(20 , 30)
    sleep_delay = random.randrange(200 , 600)
    photos_grab_amount = random.randrange(2 , 6)
    follow_likers_per_photo = random.randrange(2 , 6)
    max_pic = random.randrange(100 , 365)

    all_intract_followers= models.FollowAndInntractFollowers.objects.all()
    accs= models.accounts.objects.all()
    objects = list()
    for i in all_intract_followers:
        p= i.name
        objects.append(p)
    for ac in accs:
        u = ac.username
        p = ac.password
        session = InstaPy (username= u, password = p)
        try:
            with  smart_run(session):
                session.set_user_interact(amount=amount, randomize=randomaize, percentage=70 )
                session.follow_user_followers(objects, amount=amount, randomize=randomaize, interact=True , sleep_delay= sleep_delay)
                session.set_skip_users(skip_private=False)
        except :
            import traceback
            print(traceback.format_exc())
            pass
        
    response = """done....."""
    return HttpResponse(response)

def CallFollowAndInntractFollowing(request):
    skip_top_posts = bool(random.getrandbits(1))
    randomaize = bool(random.getrandbits(1))
    amount = random.randrange(20 , 30)
    sleep_delay = random.randrange(200 , 600)
    photos_grab_amount = random.randrange(2 , 6)
    follow_likers_per_photo = random.randrange(2 , 6)
    max_pic = random.randrange(100 , 365)

    all_intract_following= models.FollowAndInntractFollowing.objects.all()
    accs= models.accounts.objects.all()
    objects = list()
    for i in all_intract_following:
        p= i.name
        objects.append(p)
    for ac in accs:
        u = ac.username
        p = ac.password
        session = InstaPy (username= u, password = p)
        try:
            with  smart_run(session):
                session.set_user_interact(amount=amount, randomize=randomaize, percentage=70 )
                session.follow_user_following(objects, amount=amount, randomize=True, interact=True , sleep_delay= sleep_delay)
                session.set_skip_users(skip_private=False)
        except :
            import traceback
            print(traceback.format_exc())
            pass
        
    response = """done....."""
    return HttpResponse(response)

def CallCommentLocation(request):
    skip_top_posts = bool(random.getrandbits(1))
    randomaize = bool(random.getrandbits(1))
    amount = random.randrange(20 , 60)
    sleep_delay = random.randrange(200 , 600)

    all_comments= models.CommentLocations.objects.all()
    accs= models.accounts.objects.all()
    objects = list()
    for i in all_comments:
        p= i.name
        objects.append(p)
    for ac in accs:
        u = ac.username
        p = ac.password
        session = InstaPy (username= u, password = p)
        try:
            with  smart_run(session):
                session.comment_by_locations(objects, amount=amount, skip_top_posts=skip_top_posts , randomize = randomaize , sleep_delay = sleep_delay)
        except :
            import traceback
            print(traceback.format_exc())
            pass
        
    response = """done....."""
    return HttpResponse(response)

def CallIntractionUrl(request):
    skip_top_posts = bool(random.getrandbits(1))
    randomaize = bool(random.getrandbits(1))
    reply = bool(random.getrandbits(1))
    amount = random.randrange(20 , 60)
    sleep_delay = random.randrange(200 , 600)
    max_pic = random.randrange(100 , 365)
    posts_amount = random.randrange(5 , 15)
    comments_per_post = random.randrange(5 , 15)
    posts_grab_amount = random.randrange(5 , 15)
    interact_likers_per_post = random.randrange(5 , 15)

    all_users= models.FolloweUsernames.objects.all()
    accs= models.accounts.objects.all()
    objects = list()
    for i in all_users:
        p= i.name
        objects.append(p)
    for ac in accs:
        u = ac.username
        p = ac.password
        session = InstaPy (username= u, password = p)
        try:
            with  smart_run(session):
                session.set_do_like(enabled=True, percentage=94)
                session.set_do_comment(enabled=True, percentage=24)
                session.set_comments([])
                session.set_do_follow(enabled=True, percentage=44)
                session.set_user_interact(amount=amount, randomize=randomaize, percentage=72)
                session.interact_by_URL(urls=[], randomize=randomaize, interact=True)
        except :
            import traceback
            print(traceback.format_exc())
            pass
        
    response = """done....."""
    return HttpResponse(response)

def CallIntractionUser(request):
    skip_top_posts = bool(random.getrandbits(1))
    randomaize = bool(random.getrandbits(1))
    reply = bool(random.getrandbits(1))
    amount = random.randrange(20 , 60)
    sleep_delay = random.randrange(200 , 600)
    max_pic = random.randrange(100 , 365)
    posts_amount = random.randrange(5 , 15)
    comments_per_post = random.randrange(5 , 15)
    posts_grab_amount = random.randrange(5 , 15)
    interact_likers_per_post = random.randrange(5 , 15)

    all_users= models.FolloweUsernames.objects.all()
    accs= models.accounts.objects.all()
    objects = list()
    for i in all_users:
        p= i.name
        objects.append(p)
    for ac in accs:
        u = ac.username
        p = ac.password
        session = InstaPy (username= u, password = p)
        try:
            with  smart_run(session):
                session.set_do_follow(enabled=True, percentage=50)
                session.set_comments([])
                session.set_do_comment(enabled=True, percentage=80)
                session.set_do_like(True, percentage=70)
                session.interact_by_users([], amount=amount, randomize=randomaize)
        except :
            import traceback
            print(traceback.format_exc())
            pass
        
    response = """done....."""
    return HttpResponse(response)

def CallIntractionTags(request):
    skip_top_posts = bool(random.getrandbits(1))
    randomaize = bool(random.getrandbits(1))
    reply = bool(random.getrandbits(1))
    amount = random.randrange(20 , 60)
    sleep_delay = random.randrange(200 , 600)
    max_pic = random.randrange(100 , 365)
    posts_amount = random.randrange(5 , 15)
    comments_per_post = random.randrange(5 , 15)
    posts_grab_amount = random.randrange(5 , 15)
    interact_likers_per_post = random.randrange(5 , 15)

    all_users= models.FolloweUsernames.objects.all()
    accs= models.accounts.objects.all()
    objects = list()
    for i in all_users:
        p= i.name
        objects.append(p)
    for ac in accs:
        u = ac.username
        p = ac.password
        session = InstaPy (username= u, password = p)
        try:
            with  smart_run(session):
                session.set_do_follow(enabled=True, percentage=50)
                session.set_comments([])
                session.set_do_comment(enabled=True, percentage=80)
                session.set_do_like(enabled=True,percentage=70)
                session.interact_by_users_tagged_posts([], amount=amount, randomize=randomaize)
        except :
            import traceback
            print(traceback.format_exc())
            pass
        
    response = """done....."""
    return HttpResponse(response)

def CallIntractionFollowing(request):
    skip_top_posts = bool(random.getrandbits(1))
    randomaize = bool(random.getrandbits(1))
    reply = bool(random.getrandbits(1))
    amount = random.randrange(20 , 60)
    sleep_delay = random.randrange(200 , 600)
    max_pic = random.randrange(100 , 365)
    posts_amount = random.randrange(5 , 15)
    comments_per_post = random.randrange(5 , 15)
    posts_grab_amount = random.randrange(5 , 15)
    interact_likers_per_post = random.randrange(5 , 15)

    all_users= models.IntractionFollowing.objects.all()
    accs= models.accounts.objects.all()
    coment= models.Comments.objects.all()
    objects = list()
    comment = list()
    for e in coment:
        g = e.comment
        comment.append(g)
    for i in all_users:
        p= i.name
        objects.append(p)
    print('+'*80)
    print(objects)
    print('*'*80)
    for ac in accs:
        u = ac.username
        p = ac.password
        session = InstaPy (username= u, password = p)
        try:
            with smart_run(session):
                session.set_user_interact(amount=5, randomize=True, percentage=50)
                session.set_do_follow(enabled=True, percentage=70)
                session.set_do_like(enabled=True, percentage=70)
                session.set_comments(comment)
                session.set_do_comment(enabled=True, percentage=80)
                session.interact_user_following(objects, amount=10, randomize=True)

        except :
            import traceback
            print(traceback.format_exc())
            pass
        
    response = """done....."""
    return HttpResponse(response)

def CallIntractionFollowers(request):
    skip_top_posts = bool(random.getrandbits(1))
    randomaize = bool(random.getrandbits(1))
    reply = bool(random.getrandbits(1))
    amount = random.randrange(20 , 60)
    sleep_delay = random.randrange(200 , 600)
    max_pic = random.randrange(100 , 365)
    posts_amount = random.randrange(5 , 15)
    comments_per_post = random.randrange(5 , 15)
    posts_grab_amount = random.randrange(5 , 15)
    interact_likers_per_post = random.randrange(5 , 15)

    all_users= models.IntractionFollowers.objects.all()
    accs= models.accounts.objects.all()
    coment= models.Comments.objects.all()
    objects = list()
    comment = list()
    for e in coment:
        g = e.comment
        comment.append(g)
    for i in all_users:
        p= i.name
        objects.append(p)
    for ac in accs:
        u = ac.username
        p = ac.password
        session = InstaPy (username= u, password = p)
        try:
            with  smart_run(session):
                session.set_user_interact(amount=amount, randomize=randomaize, percentage=50)
                session.set_do_follow(enabled=True, percentage=70)
                session.set_do_like(enabled=True, percentage=70)
                session.set_comments(comment)
                session.set_do_comment(enabled=True, percentage=80)
                session.interact_user_followers(objects, amount=amount, randomize=randomaize)
        except :
            import traceback
            print(traceback.format_exc())
            pass
        
    response = """done....."""
    return HttpResponse(response)

def CallIntractionLikers(request):
    skip_top_posts = bool(random.getrandbits(1))
    randomaize = bool(random.getrandbits(1))
    reply = bool(random.getrandbits(1))
    amount = random.randrange(20 , 60)
    sleep_delay = random.randrange(200 , 600)
    max_pic = random.randrange(100 , 365)
    posts_amount = random.randrange(5 , 15)
    comments_per_post = random.randrange(5 , 15)
    posts_grab_amount = random.randrange(5 , 15)
    interact_likers_per_post = random.randrange(5 , 15)

    all_users= models.IntractionLikers.objects.all()
    accs= models.accounts.objects.all()
    objects = list()
    for i in all_users:
        p= i.name
        objects.append(p)
    for ac in accs:
        u = ac.username
        p = ac.password
        session = InstaPy (username= u, password = p)
        try:
            with  smart_run(session):
                session.set_do_reply_to_comments(enabled=True, percentage=14)
                session.set_comment_replies(replies=[""])
                session.set_user_interact(amount=amount, percentage=70, randomize=randomaize)
                session.set_do_like(enabled=True, percentage=94)
                session.interact_user_likers(usernames=objects,
                                            posts_grab_amount=posts_grab_amount,
                                            interact_likers_per_post=interact_likers_per_post,
                                            randomize=randomaize)
        except :
            import traceback
            print(traceback.format_exc())
            pass
        
    response = """done....."""
    return HttpResponse(response)

def CallIntractionCommenters(request):
    skip_top_posts = bool(random.getrandbits(1))
    randomaize = bool(random.getrandbits(1))
    reply = bool(random.getrandbits(1))
    amount = random.randrange(20 , 60)
    sleep_delay = random.randrange(200 , 600)
    max_pic = random.randrange(100 , 365)
    posts_amount = random.randrange(5 , 15)
    comments_per_post = random.randrange(5 , 15)
    posts_grab_amount = random.randrange(5 , 15)
    interact_likers_per_post = random.randrange(5 , 15)

    all_users= models.FolloweUsernames.objects.all()
    accs= models.accounts.objects.all()
    objects = list()
    for i in all_users:
        p= i.name
        objects.append(p)
    for ac in accs:
        u = ac.username
        p = ac.password
        session = InstaPy (username= u, password = p)
        try:
            with  smart_run(session):
                session.set_do_reply_to_comments(enabled=True, percentage=14)
                session.set_comment_replies(replies=[""])
                session.set_user_interact(amount=amount, percentage=70, randomize=randomaize)
                session.set_do_like(enabled=True, percentage=94)
                session.interact_by_comments(usernames=[""], posts_amount= posts_amount, comments_per_post=comments_per_post, reply=reply, interact=True, randomize=randomaize)
        except :
            import traceback
            print(traceback.format_exc())
            pass
        
    response = """done....."""
    return HttpResponse(response)

def CallLikeTags(request):
    skip_top_posts = bool(random.getrandbits(1))
    randomaize = bool(random.getrandbits(1))
    amount = random.randrange(20 , 60)
    sleep_delay = random.randrange(200 , 600)

    all_users= models.FolloweUsernames.objects.all()
    accs= models.accounts.objects.all()
    objects = list()
    for i in all_users:
        p= i.name
        objects.append(p)
    for ac in accs:
        u = ac.username
        p = ac.password
        session = InstaPy (username= u, password = p)
        try:
            with  smart_run(session):
                session.like_by_tags([], amount=amount , randomize = randomaize , skip_top_posts = skip_top_posts , sleep_delay =sleep_delay) 
        except :
            import traceback
            print(traceback.format_exc())
            pass
        
    response = """done....."""
    return HttpResponse(response)

def CallLikeLocations(request):
    skip_top_posts = bool(random.getrandbits(1))
    randomaize = bool(random.getrandbits(1))
    amount = random.randrange(20 , 60)
    sleep_delay = random.randrange(200 , 600)

    all_users= models.FolloweUsernames.objects.all()
    accs= models.accounts.objects.all()
    objects = list()
    for i in all_users:
        p= i.name
        objects.append(p)
    for ac in accs:
        u = ac.username
        p = ac.password
        session = InstaPy (username= u, password = p)
        try:
            with  smart_run(session):
                session.like_by_locations([], amount=amount , randomize = randomaize , skip_top_posts = skip_top_posts , sleep_delay =sleep_delay) 
        except :
            import traceback
            print(traceback.format_exc())
            pass
        
    response = """done....."""
    return HttpResponse(response)

def CallStoryTags(request):

    all_users= models.FolloweUsernames.objects.all()
    accs= models.accounts.objects.all()
    objects = list()
    for i in all_users:
        p= i.name
        objects.append(p)
    for ac in accs:
        u = ac.username
        p = ac.password
        session = InstaPy (username= u, password = p)
        try:
            with  smart_run(session):
                session.story_by_tags([]) 
        except :
            import traceback
            print(traceback.format_exc())
            pass
        
    response = """done....."""
    return HttpResponse(response)

def CallStoryUsers(request):

    all_users= models.FolloweUsernames.objects.all()
    accs= models.accounts.objects.all()
    objects = list()
    for i in all_users:
        p= i.name
        objects.append(p)
    for ac in accs:
        u = ac.username
        p = ac.password
        session = InstaPy (username= u, password = p)
        try:
            with  smart_run(session):
                session.story_by_users([]) 
        except :
            import traceback
            print(traceback.format_exc())
            pass
        
    response = """done....."""
    return HttpResponse(response)



def sendstory(request,id):
    path = "/home/mehdi/Documents/bot/bot/story"
    dirs = os.listdir( path )
    accs= models.accounts.objects.all()

    for file in dirs:
        jpg_to_post = path + '/' + file
        
        if file == f'{id}.jpg':
            for ac in accs:
                u = ac.username
                p = ac.password
                print(u)
                print(p)
                os.system(f'java -jar /home/mehdi/IdeaProjects/MadtalkRobot/out/artifacts/MadtalkRobot_jar/MadtalkRobot.jar {u} {p} {jpg_to_post}')

    response = """done....."""

    return HttpResponse(response)

def sendpost(request, caption ,id):
    path = "/home/mehdi/Documents/bot/bot/post"
    dirs = os.listdir( path )

    for file in dirs:
        jpg_to_post = path + '/' + file
        accs= models.accounts.objects.all()
        if file == f'{id}.jpg':
            for ac in accs:
                u = ac.username
                p = ac.password
                os.system(f'java -jar /home/mehdi/IdeaProjects/MadtalkRobot/out/artifacts/MadtalkRobot_jar/MadtalkRobot.jar {u} {p} {jpg_to_post} "{caption}"')
    response = """done....."""

    return HttpResponse(response)

def createpost(request , id):
    object = models.createpost.objects.get(id=id)

    template = object.template.path
    photo1 = object.photoup.path
    photo2= object.photobut.path
    x = object.text1
    type = object.type

    x = x.strip()
    y = ""
    i=0
    n = 30
    while True:
        if i+n > len(x):
            y = y + x[i:i+n]
            break
        if x[i+n] == " ":
            y = y + x[i:i+n] + "\n"
            i = i+n+1
        else:
            for j in range(n):
                if x[i+n-j]==" ":
                    y = y + x[i:i+n-j] + "\n"
                    i = i+n-j+1
                    break

    my_image = Image.open(f"{template}")
    pastedi=Image.open(f"{photo1}")
    logo=Image.open(f"{photo2}")

    resized_im =  pastedi.resize((312, 136))
    resize_lg = logo.resize((164, 238))
    title_font = ImageFont.truetype('dana/Dana-FaNum-Medium.ttf', 40)

    title_text = f"{y}"
    reshaped_text = arabic_reshaper.reshape(title_text) 
    bidi_text = get_display(reshaped_text)  

    image_editable = ImageDraw.Draw(my_image)

    image_editable.text((350,400), title_text ,(0,0,0), font=title_font ,align='right', spacing=50 )

    # draw = ImageDraw.Draw(my_image)
    # draw.text((250,70), (0,0,0), font=title_font)

    copyi=my_image.copy()
    pastii=pastedi.copy()
    logoi= logo.copy()

    copyi.paste(resized_im ,(600, 200))
    copyi.paste(resize_lg ,(165, 1480)) 
    date = datetime.datetime.now()
    copyi.save(f"./story/{id}.jpg")
    response = """done....."""
    return HttpResponse(response)


def createstory(request , id):
    object = models.createstory.objects.get(id=id)

    template = object.template.path
    photo1 = object.photoup.path
    photo2= object.photobut.path
    x = object.text1
    type = object.type

    x = x.strip()
    y = ""
    i=0
    n = 30
    while True:
        if i+n > len(x):
            y = y + x[i:i+n]
            break
        if x[i+n] == " ":
            y = y + x[i:i+n] + "\n"
            i = i+n+1
        else:
            for j in range(n):
                if x[i+n-j]==" ":
                    y = y + x[i:i+n-j] + "\n"
                    i = i+n-j+1
                    break

    my_image = Image.open(f"{template}")
    pastedi=Image.open(f"{photo1}")
    logo=Image.open(f"{photo2}")

    if type == 1 :

        top_pos = (720, 50)
        but_pos = (50, 1650)
        text_pos = (200,550)
        resized_im =  pastedi.resize((312, 136))
        resize_lg = logo.resize((164, 238))
        font_size = 60

    if type == 2 :

        top_pos = (720, 50)
        but_pos = (50, 1650)
        text_pos = (200,600)
        resized_im =  pastedi.resize((312, 136))
        resize_lg = logo.resize((164, 238))
        font_size = 50

    if type == 3 :

        top_pos = (720, 50)
        but_pos = (50, 50)
        text_pos = (300,1000)
        resized_im =  pastedi.resize((312, 136))
        resize_lg = logo.resize((164, 238))
        font_size = 50

    if type == 4 :
    
        top_pos = (385, 150)
        but_pos = (460, 1600)
        text_pos = (200,700)
        resized_im =  pastedi.resize((312, 136))
        resize_lg = logo.resize((164, 238))
        font_size = 55

    if type == 5 :

        top_pos = (385, 100)
        but_pos = (10600, -3)
        text_pos = (250,350)
        resized_im =  pastedi.resize((312, 136))
        resize_lg = logo.resize((164, 238))
        font_size = 45

    if type == 6 :

        top_pos = (50, 50)
        but_pos = (850, 1600)
        text_pos = (200,250)
        resized_im =  pastedi.resize((312, 136))
        resize_lg = logo.resize((164, 238))
        font_size = 55

    if type == 7 :

        top_pos = (384, 1465)
        but_pos = (850, 16000)
        text_pos = (240,250)
        resized_im =  pastedi.resize((312, 136))
        resize_lg = logo.resize((164, 238))
        font_size = 50

    if type == 8 :

        top_pos = (40, 1232)
        but_pos = (850, 16000)
        text_pos = (240,460)
        resized_im =  pastedi.resize((312, 136))
        resize_lg = logo.resize((164, 238))
        font_size = 50

    if type == 9 :

        top_pos = (385, 100)
        but_pos = (800, 1650)
        text_pos = (240,350)
        resized_im =  pastedi.resize((312, 136))
        resize_lg = logo.resize((164, 238))
        font_size = 50

    if type == 10 :

        top_pos = (385, 1400)
        but_pos = (800, 16000)
        text_pos = (200,200)
        resized_im =  pastedi.resize((312, 136))
        resize_lg = logo.resize((164, 238))
        font_size = 40

    if type == 11 :

        top_pos = (50, 1750)
        but_pos = (800, 16000)
        text_pos = (250,200)
        resized_im =  pastedi.resize((312, 136))
        resize_lg = logo.resize((164, 238))
        font_size = 55

    if type == 12 :

        top_pos = (50, 1750)
        but_pos = (800, 16000)
        text_pos = (250,80)
        resized_im =  pastedi.resize((312, 136))
        resize_lg = logo.resize((164, 238))
        font_size = 55

    if type == 13 :

        top_pos = (385, 760)
        but_pos = (455, 300)
        text_pos = (300,955)
        resized_im =  pastedi.resize((312, 136))
        resize_lg = logo.resize((164, 238))
        font_size = 45

    if type == 14 :

        top_pos = (755, 10)
        but_pos = (30, 1650)
        text_pos = (450,400)
        resized_im =  pastedi.resize((312, 136))
        resize_lg = logo.resize((164, 238))
        font_size = 45
    
    title_font = ImageFont.truetype('dana/Dana-FaNum-Medium.ttf', font_size)

    title_text = f"{y}"
    reshaped_text = arabic_reshaper.reshape(title_text) 
    bidi_text = get_display(reshaped_text)  

    image_editable = ImageDraw.Draw(my_image)

    image_editable.text(text_pos, title_text ,(0,0,0), font=title_font ,align='right', spacing=50 )

    # draw = ImageDraw.Draw(my_image)
    # draw.text((250,70), (0,0,0), font=title_font)

    copyi=my_image.copy()
    pastii=pastedi.copy()
    logoi= logo.copy()

    copyi.paste(resized_im ,top_pos)
    copyi.paste(resize_lg , but_pos) 
    date = datetime.datetime.now()
    copyi.save(f"./story/{id}.jpg")
    response = """done....."""
    return HttpResponse(response)
