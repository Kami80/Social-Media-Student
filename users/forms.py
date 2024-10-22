from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Skill, Message
from django.contrib.auth import password_validation

from django.utils.html import format_html
from django.contrib.auth.password_validation import password_validators_help_texts

def _custom_password_validators_help_text_html():
    """
    Return an HTML string with all help texts of all configured validators
    in an <ul>.
    """
    help_texts = ['رمز عبور شما نمی تواند خیلی شبیه سایر اطلاعات شخصی شما باشد.', 'رمز عبور شما باید حداقل 8 کاراکتر داشته باشد.',
                'رمز عبور شما نمی تواند یک رمز عبور رایج باشد.', 'رمز عبور شما نمی تواند کاملاً عددی باشد.']
    help_items = [format_html(u'<li>{}</li>', help_text) for help_text in help_texts]
    #<------------- append your hint here in help_items  ------------->
    return format_html('<ul>%s</ul>' % ''.join(help_items) if help_items else '')





class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
    label="کلمه عبور",
    strip=False,
    widget=forms.PasswordInput,
    help_text= _custom_password_validators_help_text_html())
    password2 = forms.CharField(
    label="تکرار کلمه عبور",
    strip=False,
    widget=forms.PasswordInput,
    help_text= ''
    )

    class Meta:
        model = User
        fields = ['first_name', 'email', 'username']
        
        help_texts = {
            'username': 'شماره دانشجویی شما برای کاربران نمایش داده نمی‌شود'
        }
        
        labels = {
            

            'first_name': 'نام',
            'email': 'ایمیل',
            'username': 'شماره دانشجویی',
            
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)


        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email', 'username',
                  'location', 'bio', 'short_intro', 'profile_image',
                  'social_github', 'social_linkedin', 'social_twitter',
                  'social_youtube', 'social_website']
        labels = {'username':'شماره دانشجویی'}
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'
        exclude = ['owner']

    def __init__(self, *args, **kwargs):
        super(SkillForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'subject', 'body']

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
