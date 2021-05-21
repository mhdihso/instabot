from django.db import models
from django.contrib.auth.models import User

class accounts(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Bot(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    accs_info = models.ManyToManyField(accounts)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class FolloweTags(models.Model):
    bot = models.ForeignKey(Bot, on_delete= models.CASCADE)
    name = name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class FolloweLocations(models.Model):
    bot = models.ForeignKey(Bot, on_delete= models.CASCADE)
    name = name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class FolloweUsernames(models.Model):
    bot = models.ForeignKey(Bot, on_delete= models.CASCADE)
    name = name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class FollowFollower(models.Model):
    bot = models.ForeignKey(Bot, on_delete= models.CASCADE)
    name = name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class FollowFollowing(models.Model):
    bot = models.ForeignKey(Bot, on_delete= models.CASCADE)
    name = name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class FollowLikers(models.Model):
    bot = models.ForeignKey(Bot, on_delete= models.CASCADE)
    name = name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class FollowCommenters(models.Model):
    bot = models.ForeignKey(Bot, on_delete= models.CASCADE)
    name = name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class FollowAndInntractFollowers(models.Model):
    bot = models.ForeignKey(Bot, on_delete= models.CASCADE)
    name = name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class FollowAndInntractFollowing(models.Model):
    bot = models.ForeignKey(Bot, on_delete= models.CASCADE)
    name = name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CommentLocations(models.Model):
    bot = models.ForeignKey(Bot, on_delete= models.CASCADE)
    name = name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class IntractionUrl(models.Model):
    bot = models.ForeignKey(Bot, on_delete= models.CASCADE)
    name = name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Comments(models.Model):
    comment  = models.CharField(max_length=100)

    def __str__(self):
        return self.comment


class IntractionUser(models.Model):
    bot = models.ForeignKey(Bot, on_delete= models.CASCADE)
    name = name = models.CharField(max_length=100)


    def __str__(self):
        return self.name


class IntractionTags(models.Model):
    bot = models.ForeignKey(Bot, on_delete= models.CASCADE)
    name = name = models.CharField(max_length=100)


    def __str__(self):
        return self.name


class IntractionFollowers(models.Model):
    bot = models.ForeignKey(Bot, on_delete= models.CASCADE)
    name =  models.CharField(max_length=100)

    def __str__(self):
        return self.name


class IntractionFollowing(models.Model):
    bot = models.ForeignKey(Bot, on_delete= models.CASCADE)
    name = name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class IntractionCommenters(models.Model):
    bot = models.ForeignKey(Bot, on_delete= models.CASCADE)
    name = models.CharField(max_length=100)
    reply = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class IntractionLikers(models.Model):
    bot = models.ForeignKey(Bot, on_delete= models.CASCADE)
    name =  models.CharField(max_length=100)

    def __str__(self):
        return self.name


class LikeTags(models.Model):
    bot = models.ForeignKey(Bot, on_delete= models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class LikeLocations(models.Model):
    bot = models.ForeignKey(Bot, on_delete= models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class StoryTags(models.Model):
    bot = models.ForeignKey(Bot, on_delete= models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class StoryUsers(models.Model):
    bot = models.ForeignKey(Bot, on_delete= models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class createstory(models.Model):
    type = models.SmallIntegerField()
    template = models.ImageField()
    text1 = models.TextField()
    photoup = models.ImageField()
    photobut = models.ImageField()

class createpost(models.Model):
    type = models.SmallIntegerField()
    template = models.ImageField()
    text1 = models.TextField()
    photoup = models.ImageField()
    photobut = models.ImageField()

class story(models.Model):
    photo = models.ImageField()

class post(models.Model):
    photo = models.ImageField()
    caption = models.CharField(max_length=100)