from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(label='Type in your username', max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    repassword = forms.CharField(label="Password (again)", max_length=100, widget=forms.PasswordInput)

class LoginForm(forms.Form):
    username = forms.CharField(label='Type in your username', max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    
class PostForm(forms.Form):
    content = forms.CharField(label="Type your message here", widget=forms.Textarea(attrs={'v-model': 'contenido'}))

class ThreadForm(forms.Form):
    title = forms.CharField(label="Type in the title of the thread", max_length=200)
    description = forms.CharField(widget=forms.Textarea)