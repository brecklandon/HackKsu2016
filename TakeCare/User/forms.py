from django import forms
from passwords.fields import PasswordField
from django.contrib.auth import get_user_model


class UserSignup(forms.ModelForm):
    password1 = PasswordField()
    password2 = PasswordField()

    class Meta:
        model = get_user_model()
        fields = ['email', 'first_name', 'last_name', 'phone_number', 'user_type']

    def clean(self):
        cleaned_data = super(UserSignup, self).clean()
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError("Passwords don't match. Please enter both fields again.")
        self.cleaned_data['first_name'] = self.cleaned_data['first_name'].capitalize()
        self.cleaned_data['last_name'] = self.cleaned_data['last_name'].capitalize()
        return self.cleaned_data

    def save(self, commit=True):
        user = super(UserSignup, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
