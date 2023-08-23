from django import forms
from Client.models import ClientModel

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = ClientModel
        fields = ['first_name', 'last_name', 'email', 'password', 'cuit', 'work_line', 'interest', 'province', 'city', 'area_code', 'avatar', 'is_seller', 'is_buyer']
