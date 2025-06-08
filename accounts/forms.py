from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import User
from .utils import send_verification_email  

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        print("[DEBUG] Email entered:", email)
        if not email:
            raise forms.ValidationError("Email is required.")
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        print("[DEBUG] Password entered:", password)
        if not password:
            raise forms.ValidationError("Password is required.")
        return password

    def clean(self):
        cleaned_data = super().clean()
        print("[DEBUG] Cleaned data (LoginForm):", cleaned_data)
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if not email or not password:
            raise forms.ValidationError("Both email and password are required.")

        return cleaned_data


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'name', 'role')

    def clean_password2(self):
        pw1 = self.cleaned_data.get("password1")
        pw2 = self.cleaned_data.get("password2")
        print(f"[DEBUG] Password1: {pw1}, Password2: {pw2}")
        if pw1 and pw2 and pw1 != pw2:
            raise forms.ValidationError("Passwords don't match")
        return pw2

    def save(self, commit=True):
        print("[DEBUG] Saving UserCreationForm...")

        try:
            raw_pw = self.cleaned_data.get("password1")
            print(f"[DEBUG] Raw password before hashing: {raw_pw}")
        except Exception as e:
            print(f"[ERROR] Exception while getting password1: {e}")
            return None

        user = super().save(commit=False)
        user.set_password(raw_pw)
        print(commit, '[DEBUG] Commit status:', commit)
        # if commit:
        try:
            print("[DEBUG] Committing user creation...")
            print("[DEBUG] User details:", user.email, user.name, user.role)
            user.save()
            print("[DEBUG] User saved:", user)
            print("[DEBUG] Sending password reset link to:", user.email)
            send_verification_email(user)
        except Exception as e:
            print("[ERROR] Exception during commit block:", str(e))
            raise
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'name', 'password', 'is_active', 'is_staff', 'role')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(f"[DEBUG] Editing user: {self.instance.email if self.instance else 'N/A'}")
