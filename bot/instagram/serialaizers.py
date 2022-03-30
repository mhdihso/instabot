from rest_framework import serializers
from . import models

class AccountSerialaizer(serializers.ModelSerializer):
    class Meta:
        model = models.accounts
        fields = '__all__'

class BotSerialaizer(serializers.ModelSerializer):
    account = AccountSerialaizer(many=True)
    class Meta:
        model = models.Bot
        fields = ('bot','name', 'account')

class FolloweTagsSerialaizer(serializers.ModelSerializer):
    account = AccountSerialaizer(many=True)
    class Meta:
        model = models.FolloweTags
        fields = ('bot','name', 'account')

class FolloweLocationsSerialaizer(serializers.ModelSerializer):
    account = AccountSerialaizer(many=True)
    class Meta:
        model = models.FolloweLocations
        fields = ('bot','name', 'account')

class FolloweUsernamesSerialaizer(serializers.ModelSerializer):
    account = AccountSerialaizer(many=True)
    class Meta:
        model = models.FolloweUsernames
        fields = ('bot','name', 'account')

class FollowFollowerSerialaizer(serializers.ModelSerializer):
    account = AccountSerialaizer(many=True)
    class Meta:
        model = models.FollowFollower
        fields = ('bot','name', 'account')

class FollowFollowingSerialaizer(serializers.ModelSerializer):
    account = AccountSerialaizer(many=True)
    class Meta:
        model = models.FollowFollowing
        fields = ('bot','name', 'account')

class FollowLikersSerialaizer(serializers.ModelSerializer):
    account = AccountSerialaizer(many=True)
    class Meta:
        model = models.FollowLikers
        fields = ('bot','name', 'account')

class FollowCommentersSerialaizer(serializers.ModelSerializer):
    account = AccountSerialaizer(many=True)
    class Meta:
        model = models.FollowCommenters
        fields = ('bot','name', 'account')

class FollowAndInntractFollowersSerialaizer(serializers.ModelSerializer):
    account = AccountSerialaizer(many=True)
    class Meta:
        model = models.FollowAndInntractFollowers
        fields = ('bot','name', 'account')

class FollowAndInntractFollowingSerialaizer(serializers.ModelSerializer):
    account = AccountSerialaizer(many=True)
    class Meta:
        model = models.FollowAndInntractFollowing
        fields = ('bot','name', 'account')

class CommentLocationsSerialaizer(serializers.ModelSerializer):
    account = AccountSerialaizer(many=True)
    class Meta:
        model = models.CommentLocations
        fields = ('bot','name', 'account')

class IntractionUrlSerialaizer(serializers.ModelSerializer):
    account = AccountSerialaizer(many=True)
    class Meta:
        model = models.IntractionUrl
        fields = ('bot','name', 'account')

class IntractionUserSerialaizer(serializers.ModelSerializer):
    account = AccountSerialaizer(many=True)
    class Meta:
        model = models.IntractionUser
        fields = ('bot','name', 'account')

class IntractionTagsSerialaizer(serializers.ModelSerializer):
    account = AccountSerialaizer(many=True)
    class Meta:
        model = models.IntractionTags
        fields = ('bot','name', 'account')

class IntractionFollowersSerialaizer(serializers.ModelSerializer):
    account = AccountSerialaizer(many=True)
    class Meta:
        model = models.IntractionFollowers
        fields = ('bot','name', 'account')

class IntractionFollowingSerialaizer(serializers.ModelSerializer):
    account = AccountSerialaizer(many=True)
    class Meta:
        model = models.IntractionFollowing
        fields = ('bot','name', 'account')

class IntractionCommentersSerialaizer(serializers.ModelSerializer):
    account = AccountSerialaizer(many=True)
    class Meta:
        model = models.IntractionCommenters
        fields = ('bot','name', 'account')

class IntractionLikersSerialaizer(serializers.ModelSerializer):
    account = AccountSerialaizer(many=True)
    class Meta:
        model = models.IntractionLikers
        fields = ('bot','name', 'account')

class LikeTagsSerialaizer(serializers.ModelSerializer):
    account = AccountSerialaizer(many=True)
    class Meta:
        model = models.LikeTags
        fields = ('bot','name', 'account')

class LikeLocationsSerialaizer(serializers.ModelSerializer):
    account = AccountSerialaizer(many=True)
    class Meta:
        model = models.LikeLocations
        fields = ('bot','name', 'account')

class StoryTagsSerialaizer(serializers.ModelSerializer):
    account = AccountSerialaizer(many=True)
    class Meta:
        model = models.StoryTags
        fields = ('bot','name', 'account')

class StoryUsersSerialaizer(serializers.ModelSerializer):
    account = AccountSerialaizer(many=True)
    class Meta:
        model = models.StoryUsers
        fields = ('bot','name', 'account')
