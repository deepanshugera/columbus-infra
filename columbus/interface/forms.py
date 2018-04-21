from django import forms
class CodeForm(forms.Form):
    code = forms.CharField(label='code', max_length=1000)