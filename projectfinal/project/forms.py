from django.forms import ModelForm
from django.contrib.auth import get_user_model
from .models import *


user = get_user_model()



class Projectform(ModelForm):
    class Meta:
        model = courses
        fields = ['title', 'price','body']


class Archiveform(ModelForm):
    class Meta:
        model = courses
        fields = ['archive']

