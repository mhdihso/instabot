from django.db import models

class Account(models.Model):
    is_managerdb = models.BooleanField(default=False)
    username = models.CharField(max_length=100)
    api_key = models.CharField(max_length=500)
    api_secret_key = models.CharField(max_length=500)
    access_token = models.CharField(max_length=500)
    access_token_secret = models.CharField(max_length=500)

    def __str__(self):
        return self.username
class TweetMedia(models.Model):
    file1 = models.FileField(null=True , blank=True)
    file2 =models.FileField(null=True , blank=True)
    file3 = models.FileField(null=True , blank=True)
    file4 = models.FileField(null=True , blank=True)
    text = models.CharField(max_length=500 , null=True , blank=True )

class searchlike(models.Model):
    args = models.CharField(max_length=100)

class searchreply(models.Model):
    args = models.CharField(max_length=100)
    texts = models.CharField(max_length=500)

class searchretweet(models.Model):
    args = models.CharField(max_length=100)

class searchfollow(models.Model):
    args = models.CharField(max_length=100)

class searchintraction(models.Model):
    args = models.CharField(max_length=100)
    text_for_reply = models.CharField(max_length=500)

class searchdirectmassage(models.Model):
    args = models.CharField(max_length=100)
    text_direct = models.CharField(max_length=500)