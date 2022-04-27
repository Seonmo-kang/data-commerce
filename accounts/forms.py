from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User, UserManager

from django.contrib.auth import get_user_model
#For using customized User model, we need a funtion : get_user_model
User = get_user_model()

class UserCreationForm(forms.ModelForm):
    # 사용자 생성 폼
    email = forms.EmailField(
        label=('Email'),
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': ('Email address'),
                'required': 'True',
            }
        )
    )
    password1 = forms.CharField(
        label=('Password'),
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': ('Password'),
                'required': 'True',
            }
        )
    )
    password2 = forms.CharField(
        label=('Password confirmation'),
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': ('Password confirmation'),
                'required': 'True',
            }
        )
    )
    firstName = forms.CharField(
        label=('First Name'),
        required=True,
        max_length=255
    )
    lastName = forms.CharField(
        label=('Last Name'),
        required=True,
        max_length=255
    )
    isSeller = forms.BooleanField(
        label=('Is Seller'),
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    class Meta:
        model = User
        fields = ('email', 'firstName', 'lastName','isSeller')

    def clean_password2(self):
        # 두 비밀번호 입력 일치 확인
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.email = UserManager.normalize_email(self.cleaned_data['email'])
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    # 비밀번호 변경 폼
    password = ReadOnlyPasswordHashField(
        label=('Password')
    )

    class Meta:
        model = User
        fields = ('email', 'password', 'lastName', 'firstName', 'is_active', 'is_superuser')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]