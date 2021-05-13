from django import forms
from .models import Code
class CodeForm(forms.ModelForm):
    class Meta:
        number = forms.CharField(label='Code', help_text='Enter sms verification code')
        model = Code
        fields = ('number',)