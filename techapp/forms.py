from django import forms
from .models import Category, Pref, User, Review,Tag
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .widgets import CustomCheckboxSelectMultiple
from django.conf import settings
"""
from django.core.mail import BadHeadError, send_mail
from django.http import HttpResponse
"""

class SearchForm(forms.Form):
    selected_pref = forms.ModelChoiceField(
        label='都道府県',
        required=False,
        queryset=Pref.objects,
    )
    selected_category = forms.ModelChoiceField(
        label='業態',
        required=False,
        queryset=Category.objects,
    )
    freeword = forms.CharField(min_length = 2, max_length = 100, label='', required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        selected_pref = self.fields['selected_pref']
        selected_category = self.fields['selected_category']

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['score', 'comment', 'info']

class SampleForm(forms.Form):
    tags = forms.ModelMultipleChoiceField(
        label='タグ', queryset=Tag.objects, required=False,
        widget=CustomCheckboxSelectMultiple,
    )
    a = forms.MultipleChoiceField

class ContactForm(forms.Form):
    name=forms.CharField(
        label='',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':"お名前",
        })
    )

    email=forms.EmailField(
        label='',
        widget=forms.EmailInput(attrs={
            'class':'form-control',
            'placeholder':"メールアドレス",
        })
    )

    message=forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'class':'form-control',
            'placeholder':"お問い合わせ内容",
        })
    )

    def send_email(self):
        subject="お問い合わせ"
        message=self.cleaned_data['message']
        name=self.cleaned_data['name']
        email=self.cleaned_data['email']
        from_email='{name}<{email}>'.format(name=name,email=email)
        recipient_list=[settings.EMAIL_HOST_USER]
        try:
            send_mail(subject,message,from_email,recipient_list)
        except BadHeadError:
            return HttpResponse("無効なヘッダが検出されました。")
