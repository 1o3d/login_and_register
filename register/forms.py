from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms.fields import IntegerField

from register.models import Clipboard


# class RegistrationForm(UserCreationForm):
#     email = forms.EmailField()
#     phone_number = IntegerField()
#
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'phone_number', 'password1', 'password2']


class PersonalQuestionsForm(forms.Form):
    choices = [
        (1, 'What is your mother\'s maiden name?'),
        (2, 'What was your first pet\'s name?'),
        (3, 'What city was your father born in?'),
    ]
    question = forms.ChoiceField(label='Select the question', choices=choices)
    answer = forms.CharField(label='Enter your answer', widget=forms.TextInput)
    user = User.username


class ClipboardForm(forms.Form):
    text1 = forms.CharField(label='Text1')
    text2 = forms.CharField(label='Text2')
    text3 = forms.CharField(label='Text3')
    user = User.username

    class Meta:
        fields = ['text1', 'text2', 'text3']
        widgets = {'text1': forms,
                   'text2': forms,
                   'text3': forms,
                   }
        model = Clipboard
    # def save(self):
    #     text1 = self.cleaned_data['text1']
    #     text2 = self.cleaned_data['text2']
    #     text3 = self.cleaned_data['text3']
    #     user = self.cleaned_data['user']
    #     us = Clipboard(user=User, text1=text1, text2=text2, text3=text3)
    #     us.save()
