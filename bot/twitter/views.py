from django.db.models import manager
from django.shortcuts import render
from django.http import HttpResponse
from  . import models

import tweepy


def statusmanager(request, id):
    accs = models.Account.objects.filter(is_managerdb = True)
    tmedia = models.TweetMedia.objects.get(id = id)

    for ac in accs:
        api_key = ac.api_key
        api_secret_key = ac.api_secret_key
        access_token = ac.access_token
        access_token_secret = ac.access_token_secret

        auth = tweepy.OAuthHandler(api_key, 
        api_secret_key)

        auth.set_access_token(access_token, 
            access_token_secret)


        api = tweepy.API(auth)

        try:
            api.verify_credentials()
            print("Authentication OK")
        except:
            print("Error during authentication")

        filenames = list()
        if tmedia.file1:
            filenames.append(tmedia.file1.path)
        if tmedia.file2:
            filenames.append(tmedia.file2.path)
        if tmedia.file3:
            filenames.append(tmedia.file3.path)
        if tmedia.file4:
            filenames.append(tmedia.file4.path)

        media_ids = []
        for filename in filenames:
            res = api.media_upload(filename)
            media_ids.append(res.media_id)

        api.update_status(status=tmedia.text, media_ids=media_ids)

    response = """done....."""

    return HttpResponse(response)


def statusothers(request,id):

    accs = models.Account.objects.filter(is_managerdb = False)
    tmedia = models.TweetMedia.objects.get(id = id)

    for ac in accs:
        api_key = ac.api_key
        api_secret_key = ac.api_secret_key
        access_token = ac.access_token
        access_token_secret = ac.access_token_secret

        auth = tweepy.OAuthHandler(api_key, 
        api_secret_key)

        auth.set_access_token(access_token, 
            access_token_secret)


        api = tweepy.API(auth)

        try:
            api.verify_credentials()
            print("Authentication OK")
        except:
            print("Error during authentication")

        filenames = list()
        if tmedia.file1:
            filenames.append(tmedia.file1.path)
        if tmedia.file2:
            filenames.append(tmedia.file2.path)
        if tmedia.file3:
            filenames.append(tmedia.file3.path)
        if tmedia.file4:
            filenames.append(tmedia.file4.path)

        media_ids = []
        for filename in filenames:
            res = api.media_upload(filename)
            media_ids.append(res.media_id)

        api.update_status(status=tmedia.text, media_ids=media_ids)

    response = """done....."""

    return HttpResponse(response)

def liketimeline(request , count):
    accs = models.Account.objects.filter(is_managerdb = True)

    for ac in accs:
        api_key = ac.api_key
        api_secret_key = ac.api_secret_key
        access_token = ac.access_token
        access_token_secret = ac.access_token_secret

        auth = tweepy.OAuthHandler(api_key, 
        api_secret_key)

        auth.set_access_token(access_token, 
            access_token_secret)


        api = tweepy.API(auth)

        try:
            api.verify_credentials()
            print("Authentication OK")
        except:
            print("Error during authentication")
        try :
            for tweet in tweepy.Cursor(api.home_timeline).items(count):
                api.create_favorite(tweet.id)
        except :
            continue


    response = """done....."""
    return HttpResponse(response)

def searchlikemanager(request , id , count):

    accs = models.Account.objects.filter(is_managerdb = True)
    args = models.searchlike.objects.get(id=id)
    ar = args.args
    st =str()
    li = list()
    li = ar.split()
    for i in li:
        st = st + i
        st = st + ','

    g = len(st)-2
    st = ''.join(st[x] for x in range(len(st)) if x != g+1)

    for ac in accs:
        api_key = ac.api_key
        api_secret_key = ac.api_secret_key
        access_token = ac.access_token
        access_token_secret = ac.access_token_secret

        auth = tweepy.OAuthHandler(api_key, 
        api_secret_key)

        auth.set_access_token(access_token, 
            access_token_secret)


        api = tweepy.API(auth)

        try:
            api.verify_credentials()
            print("Authentication OK")
        except:
            print("Error during authentication")
        try :
            for tweet in api.search(q= f"{st}", lang="fa", rpp=count):
                api.create_favorite(tweet.id)

        except :
            continue


    response = """done....."""
    return HttpResponse(response)

def searchlikeothers(request , id , count):
    accs = models.Account.objects.filter(is_managerdb = False)
    args = models.searchlike.objects.get(id=id)
    ar = args.args
    st =str()
    li = list()
    li = ar.split()
    for i in li:
        st = st + i
        st = st + ','

    g = len(st)-2
    st = ''.join(st[x] for x in range(len(st)) if x != g+1)

    for ac in accs:
        api_key = ac.api_key
        api_secret_key = ac.api_secret_key
        access_token = ac.access_token
        access_token_secret = ac.access_token_secret

        auth = tweepy.OAuthHandler(api_key, 
        api_secret_key)

        auth.set_access_token(access_token, 
            access_token_secret)


        api = tweepy.API(auth)

        try:
            api.verify_credentials()
            print("Authentication OK")
        except:
            print("Error during authentication")
        try :
            for tweet in api.search(q= f"{st}", lang="fa", rpp=count):
                api.create_favorite(tweet.id)

        except :
            continue


    response = """done....."""
    return HttpResponse(response)

def searchreplymanager(request , id , count):
    accs = models.Account.objects.filter(is_managerdb = True)
    args = models.searchreply.objects.get(id=id)
    ar = args.args
    st =str()
    li = list()
    li = ar.split()
    for i in li:
        st = st + i
        st = st + ','

    g = len(st)-2
    st = ''.join(st[x] for x in range(len(st)) if x != g+1)

    for ac in accs:
        api_key = ac.api_key
        api_secret_key = ac.api_secret_key
        access_token = ac.access_token
        access_token_secret = ac.access_token_secret

        auth = tweepy.OAuthHandler(api_key, 
        api_secret_key)

        auth.set_access_token(access_token, 
            access_token_secret)


        api = tweepy.API(auth)

        try:
            api.verify_credentials()
            print("Authentication OK")
        except:
            print("Error during authentication")
        try :
            for tweet in api.search(q= st, lang="fa", rpp=count):
                api.update_status(status = args.texts, in_reply_to_status_id = tweet.id , auto_populate_reply_metadata=True)

        except :
            continue


    response = """done....."""
    return HttpResponse(response)


def searchreplyothers(request , id , count):
    accs = models.Account.objects.filter(is_managerdb = False)
    args = models.searchreply.objects.get(id=id)
    ar = args.args
    st =str()
    li = list()
    li = ar.split()
    for i in li:
        st = st + i
        st = st + ','

    g = len(st)-2
    st = ''.join(st[x] for x in range(len(st)) if x != g+1)

    for ac in accs:
        api_key = ac.api_key
        api_secret_key = ac.api_secret_key
        access_token = ac.access_token
        access_token_secret = ac.access_token_secret

        auth = tweepy.OAuthHandler(api_key, 
        api_secret_key)

        auth.set_access_token(access_token, 
            access_token_secret)


        api = tweepy.API(auth)

        try:
            api.verify_credentials()
            print("Authentication OK")
        except:
            print("Error during authentication")
        try :
            for tweet in api.search(q= st, lang="fa", rpp=count):
                api.update_status(status = args.texts, in_reply_to_status_id = tweet.id , auto_populate_reply_metadata=True)

        except :
            continue


    response = """done....."""
    return HttpResponse(response)

def searchretweetmanager(request , id , count):
    accs = models.Account.objects.filter(is_managerdb = True)
    args = models.searchretweet.objects.get(id=id)
    ar = args.args
    st =str()
    li = list()
    li = ar.split()
    for i in li:
        st = st + i
        st = st + ','

    g = len(st)-2
    st = ''.join(st[x] for x in range(len(st)) if x != g+1)

    for ac in accs:
        api_key = ac.api_key
        api_secret_key = ac.api_secret_key
        access_token = ac.access_token
        access_token_secret = ac.access_token_secret

        auth = tweepy.OAuthHandler(api_key, 
        api_secret_key)

        auth.set_access_token(access_token, 
            access_token_secret)


        api = tweepy.API(auth)

        try:
            api.verify_credentials()
            print("Authentication OK")
        except:
            print("Error during authentication")
        try :
            for tweet in api.search(q= st, lang="fa", rpp=count):
                api.retweet(tweet.id)

        except :
            continue


    response = """done....."""
    return HttpResponse(response)


def searchretweetothers(request , id , count):
    accs = models.Account.objects.filter(is_managerdb = False)
    args = models.searchretweet.objects.get(id=id)
    ar = args.args
    st =str()
    li = list()
    li = ar.split()
    for i in li:
        st = st + i
        st = st + ','

    g = len(st)-2
    st = ''.join(st[x] for x in range(len(st)) if x != g+1)

    for ac in accs:
        api_key = ac.api_key
        api_secret_key = ac.api_secret_key
        access_token = ac.access_token
        access_token_secret = ac.access_token_secret

        auth = tweepy.OAuthHandler(api_key, 
        api_secret_key)

        auth.set_access_token(access_token, 
            access_token_secret)


        api = tweepy.API(auth)

        try:
            api.verify_credentials()
            print("Authentication OK")
        except:
            print("Error during authentication")
        try :
            for tweet in api.search(q= st, lang="fa", rpp=count):
                api.retweet(tweet.id)

        except :
            continue


    response = """done....."""
    return HttpResponse(response)

def searchfollowmanager(request , id , count):
    accs = models.Account.objects.filter(is_managerdb = True)
    args = models.searchfollow.objects.get(id=id)
    ar = args.args
    st =str()
    li = list()
    li = ar.split()
    for i in li:
        st = st + i
        st = st + ','

    g = len(st)-2
    st = ''.join(st[x] for x in range(len(st)) if x != g+1)

    for ac in accs:
        api_key = ac.api_key
        api_secret_key = ac.api_secret_key
        access_token = ac.access_token
        access_token_secret = ac.access_token_secret

        auth = tweepy.OAuthHandler(api_key, 
        api_secret_key)

        auth.set_access_token(access_token, 
            access_token_secret)


        api = tweepy.API(auth)

        try:
            api.verify_credentials()
            print("Authentication OK")
        except:
            print("Error during authentication")
        try :
            for tweet in api.search(q= st, lang="fa", rpp=count):
                api.create_friendship(tweet.user.screen_name)

        except :
            continue


    response = """done....."""
    return HttpResponse(response)

def searchfollowothers(request , id , count):
    accs = models.Account.objects.filter(is_managerdb = False)
    args = models.searchfollow.objects.get(id=id)
    ar = args.args
    st =str()
    li = list()
    li = ar.split()
    for i in li:
        st = st + i
        st = st + ','

    g = len(st)-2
    st = ''.join(st[x] for x in range(len(st)) if x != g+1)

    for ac in accs:
        api_key = ac.api_key
        api_secret_key = ac.api_secret_key
        access_token = ac.access_token
        access_token_secret = ac.access_token_secret

        auth = tweepy.OAuthHandler(api_key, 
        api_secret_key)

        auth.set_access_token(access_token, 
            access_token_secret)


        api = tweepy.API(auth)

        try:
            api.verify_credentials()
            print("Authentication OK")
        except:
            print("Error during authentication")
        try :
            for tweet in api.search(q= st, lang="fa", rpp=count):
                api.create_friendship(tweet.user.screen_name)

        except :
            continue


    response = """done....."""
    return HttpResponse(response)

def searchintractionmanager(request , id , count):
    accs = models.Account.objects.filter(is_managerdb = True)
    args = models.searchintraction.objects.get(id=id)
    ar = args.args
    st =str()
    li = list()
    li = ar.split()
    for i in li:
        st = st + i
        st = st + ','

    g = len(st)-2
    st = ''.join(st[x] for x in range(len(st)) if x != g+1)

    for ac in accs:
        api_key = ac.api_key
        api_secret_key = ac.api_secret_key
        access_token = ac.access_token
        access_token_secret = ac.access_token_secret

        auth = tweepy.OAuthHandler(api_key, 
        api_secret_key)

        auth.set_access_token(access_token, 
            access_token_secret)


        api = tweepy.API(auth)

        try:
            api.verify_credentials()
            print("Authentication OK")
        except:
            print("Error during authentication")
        try :
            for tweet in api.search(q= st, lang="fa", rpp=count):
                api.create_friendship(tweet.user.screen_name)
                api.retweet(tweet.id)
                api.update_status(status = args.text_for_reply, in_reply_to_status_id = tweet.id , auto_populate_reply_metadata=True)
                api.create_favorite(tweet.id)

        except :
            continue


    response = """done....."""
    return HttpResponse(response)

def searchintractionothers(request , id , count):
    accs = models.Account.objects.filter(is_managerdb = False)
    args = models.searchintraction.objects.get(id=id)
    ar = args.args
    st =str()
    li = list()
    li = ar.split()
    for i in li:
        st = st + i
        st = st + ','

    g = len(st)-2
    st = ''.join(st[x] for x in range(len(st)) if x != g+1)

    for ac in accs:
        api_key = ac.api_key
        api_secret_key = ac.api_secret_key
        access_token = ac.access_token
        access_token_secret = ac.access_token_secret

        auth = tweepy.OAuthHandler(api_key, 
        api_secret_key)

        auth.set_access_token(access_token, 
            access_token_secret)


        api = tweepy.API(auth)

        try:
            api.verify_credentials()
            print("Authentication OK")
        except:
            print("Error during authentication")
        try :
            for tweet in api.search(q= st, lang="fa", rpp=count):
                api.create_friendship(tweet.user.screen_name)
                api.retweet(tweet.id)
                api.update_status(status = args.text_for_reply, in_reply_to_status_id = tweet.id , auto_populate_reply_metadata=True)
                api.create_favorite(tweet.id)

        except :
            continue


    response = """done....."""
    return HttpResponse(response)

def searchsenddirectmanager(request , id , count):
    accs = models.Account.objects.filter(is_managerdb = True)
    args = models.searchdirectmassage.objects.get(id=id)
    ar = args.args
    ar = ar.strip()
    st =str()
    li = list()
    li = ar.split()
    for i in li:
        st = st + i
        st = st + ','

    g = len(st)-2
    st = ''.join(st[x] for x in range(len(st)) if x != g+1)


    for ac in accs:
        api_key = ac.api_key
        api_secret_key = ac.api_secret_key
        access_token = ac.access_token
        access_token_secret = ac.access_token_secret

        auth = tweepy.OAuthHandler(api_key, 
        api_secret_key)

        auth.set_access_token(access_token, 
            access_token_secret)


        api = tweepy.API(auth)

        try:
            api.verify_credentials()
            print("Authentication OK")
        except:
            print("Error during authentication")

        for tweet in api.search(q=st, lang="fa", rpp=count):
            try:
                api.send_direct_message(recipient_id =tweet.user.id, text = args.text_direct)
            except :
                continue


    response = """done....."""
    return HttpResponse(response)

def searchsenddirectothers(request , id , count):
    accs = models.Account.objects.filter(is_managerdb = False)
    args = models.searchdirectmassage.objects.get(id=id)
    ar = args.args
    ar = ar.strip()
    st =str()
    li = list()
    li = ar.split()
    for i in li:
        st = st + i
        st = st + ','

    g = len(st)-2
    st = ''.join(st[x] for x in range(len(st)) if x != g+1)


    for ac in accs:
        api_key = ac.api_key
        api_secret_key = ac.api_secret_key
        access_token = ac.access_token
        access_token_secret = ac.access_token_secret

        auth = tweepy.OAuthHandler(api_key, 
        api_secret_key)

        auth.set_access_token(access_token, 
            access_token_secret)


        api = tweepy.API(auth)

        try:
            api.verify_credentials()
            print("Authentication OK")
        except:
            print("Error during authentication")

        for tweet in api.search(q=st, lang="fa", rpp=count):
            try:
                api.send_direct_message(recipient_id =tweet.user.id, text = args.text_direct)
            except :
                continue


    response = """done....."""
    return HttpResponse(response)