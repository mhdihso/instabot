from instapy import InstaPy , smart_run


def follow_by_username():

    users = [
        'udemy',
        'nasa',
    ]

    session = InstaPy (username= 'hellophpwotld',
                         password = 'world@@@',
                         headless_browser=True)
    try:
        with  smart_run(session):
            session.follow_user_followers(users,amount=10,randomize=True, sleep_delay=20, skip_top_posts= True)
            session.lik
    except :
        import traceback
        print(traceback.format_exc())
        pass


def follow_by_tags():

    session = InstaPy (username= 'hellophpwotld',
                         password = 'world@@@')

    try:
        with  smart_run(session):
            session.follow_by_tags(['konkor','کنکور'], amount=10 , media='photo', skip_top_posts= True) 
    except :
        import traceback
        print(traceback.format_exc())
        pass

def Story():
    session = InstaPy (username= 'hellophpwotld',
                         password = 'world@@@')

    try:
        with  smart_run(session):
            session.story_by_users(['zehn.ir'])
    except :
        import traceback
        print(traceback.format_exc())
        pass

def GroupFollow():
    session = InstaPy (username= 'hellophpwotld',
                         password = 'world@@@')

    try:
        with  smart_run(session):
            follow_by_list(followlist=['samantha3', 'larry_ok'], times=1, sleep_delay=600, interact=False)
    except :
        import traceback
        print(traceback.format_exc())
        pass

def FollowCommenters():
    session = InstaPy (username= 'hellophpwotld',
                         password = 'world@@@')

    try:
        with  smart_run(session):
            session.follow_commenters(['user1', 'user2', 'user3'], amount=100, daysold=365, max_pic = 100, sleep_delay=600, interact=False)
    except :
        import traceback
        print(traceback.format_exc())
        pass

def Intrectphoto():
    session = InstaPy (username= 'testforibstabot',
                         password = 'SV$3sA8Mcgs6C7z')

    try:
        with  smart_run(session):
            session.set_do_follow(enabled=True, percentage=100)
            session.set_comments(["Cool", "Super!"])
            session.set_do_comment(enabled=True, percentage=100)
            session.set_do_like(True, percentage=100)
            session.set_do_story(enabled = True, percentage = 100, simulate = False)
            session.interact_by_users(usernames=['sadaftaheriann'], amount=5, randomize=True, media='Photo')
    except :
        import traceback
        print(traceback.format_exc())
        pass

def Intrectvideo():
    session = InstaPy (username= 'testforibstabot',
                         password = 'SV$3sA8Mcgs6C7z')

    try:
        with  smart_run(session):
            session.set_do_follow(enabled=True, percentage=100)
            session.set_comments(["Cool", "Super!"])
            session.set_do_comment(enabled=True, percentage=100)
            session.set_do_like(True, percentage=100)
            session.set_do_story(enabled = True, percentage = 100, simulate = False)
            session.interact_by_users(usernames=['sadaftaheriann'], amount=5, randomize=True, media='Video')
    except :
        import traceback
        print(traceback.format_exc())
        pass


def Intrectphoto():
    session = InstaPy (username= 'testforibstabot',
                         password = 'SV$3sA8Mcgs6C7z')

    try:
        with  smart_run(session):
            session.set_do_follow(enabled=True, percentage=100)
            session.set_comments(["Cool", "Super!"])
            session.set_do_comment(enabled=True, percentage=100)
            session.set_do_like(True, percentage=100)
            session.set_do_story(enabled = True, percentage = 100, simulate = False)
            session.interact_by_users(usernames=['sadaftaheriann'], amount=5, randomize=True, media='Photo')
    except :
        import traceback
        print(traceback.format_exc())
        pass

def Intrectcarousel():
    session = InstaPy (username= 'testforibstabot',
                         password = 'SV$3sA8Mcgs6C7z')

    try:
        with  smart_run(session):
            session.set_do_follow(enabled=True, percentage=100)
            session.set_comments(["Cool", "Super!"])
            session.set_do_comment(enabled=True, percentage=100)
            session.set_do_like(True, percentage=100)
            session.set_do_story(enabled = True, percentage = 100, simulate = False)
            session.interact_by_users(usernames=['sadaftaheriann'], amount=5, randomize=True, media='Carousel')
    except :
        import traceback
        print(traceback.format_exc())
        pass


Intrectphoto()
print('DONE 1') 
Intrectcarousel()
print('DONE 2') 
Intrectvideo()
print('DONE 3') 