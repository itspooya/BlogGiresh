from django import forms
class Subscribe(forms.Form):
    Name = forms.CharField()
    Email = forms.EmailField()
    Subject = forms.CharField()
    Message = forms.Textarea()
    def __str__(self):
        return self.Email