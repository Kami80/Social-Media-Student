from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField('نام',  max_length=200, blank=True, null=True)
    email = models.EmailField('ایمیل',max_length=500, blank=True, null=True)
    username = models.CharField('نام کاربری', max_length=200, blank=True, null=True)
    location = models.CharField('دانشگاه', max_length=200, blank=True, null=True)
    short_intro = models.CharField('رشته', max_length=200, blank=True, null=True)
    bio = models.TextField('بیوگرافی', blank=True, null=True)
    profile_image = models.ImageField('عکس پروفایل',
        null=True, blank=True, upload_to='profiles/', default="profiles/user-default.png")
    social_github = models.CharField('لینک صفحه اینستاگرام', max_length=200, blank=True, null=True)
    social_twitter = models.CharField('لینک صفحه توییتر', max_length=200, blank=True, null=True)
    social_linkedin = models.CharField('لینک صفحه لینکدین', max_length=200, blank=True, null=True)
    social_youtube = models.CharField('لینک صفحه یوتوب', max_length=200, blank=True, null=True)
    social_website = models.CharField('لینک وب‌سایت شخصی', max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.username)

    class Meta:
        ordering = ['created']

    @property
    def imageURL(self):
        try:
            url = self.profile_image.url
        except:
            url = ''
        return url


class Skill(models.Model):
    owner = models.ForeignKey(
        Profile, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField('نام', max_length=200, blank=True, null=True)
    description = models.TextField('توضیحات', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)


class Message(models.Model):
    sender = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, null=True, blank=True)
    recipient = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, null=True, blank=True, related_name="messages")
    name = models.CharField('نام', max_length=200, null=True, blank=True)
    email = models.EmailField('ایمیل', max_length=200, null=True, blank=True)
    subject = models.CharField('عنوان', max_length=200, null=True, blank=True)
    body = models.TextField('متن پیام', null=True, blank=True)
    is_read = models.BooleanField(default=False, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.subject

    class Meta:
        ordering = ['is_read', '-created']
