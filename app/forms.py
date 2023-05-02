

from django import forms


from app.models import *

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        # fields=['Username','Email address','Password']
        fields=['username','email','password','last_name','first_name']
        #fields='__all__'
        widgets={'password':forms.PasswordInput}

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['add','profile_pic']
        #fields='__all__'

