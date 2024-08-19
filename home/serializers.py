from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Team, Ideas, Articles, Company, Commites, Category, UserLogin, Xizmatlar, Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('yourname', 'youremail', 'yourphone', 'iteananme', 'companyname', 'message')


class IdeasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ideas
        fields = ('title', 'description', 'image')


class ArticlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = ('title', 'purpose', 'description', 'category', 'image', 'created_at')


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('name', 'image', 'description', 'phone_number', 'adress', 'email', 'google_accaunt')


class CommitesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commites
        fields = ('description', 'image', 'name', 'status', 'jobs', 'username', 'created_at')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLogin
        fields = ('user', 'ip_address')


class XizmatlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Xizmatlar
        fields = ('title', 'description', 'image', 'employee', 'commit')


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('name', 'image', 'jobs', 'category', 'telegram_link', 'instagram_link', 'linkden_link', 'fesbook_link')




