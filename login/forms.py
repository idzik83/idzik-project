#-*- coding: utf-8 -*-
from django import forms
from models import UserModel
from captcha.fields import CaptchaField

class UserForm(forms.ModelForm):

    captcha = CaptchaField(label="Защита от спама")
    conf_password = forms.CharField(min_length=5, max_length=30, label="Подтвердтие пароль",
                                     widget=forms.PasswordInput())
    class Meta:
        model = UserModel
        fields = ('last_name', 'first_name', 'login', 'password', 'email', 'dob', 'mobile', 'avatar')
        labels = {'last_name': "Фамилия",
                  'first_name': "Имя",
                  'login': "Логин",
                  'password': "Пароль",
                  'email': "Почта",
                  'dob': "Дата рождения",
                  'mobile': "Мобильный телефон",
        }
        help_text = {'password': "(Введите пароль 5-30 символов)",
                     'dob': "(Введите дату в формате: ГГГГ-ММ-ДД)",
                     'mobile': "(Введите телефон в формате: ***-*******)"
        }
        widgets = {'password': forms.PasswordInput()}
        min_length = {'password': 5}

    def clean(self):
        data = super(UserForm, self).clean()
        password = self.data.get('password')
        conf_password = self.data.get('conf_password')

        if password != conf_password:
            raise forms.ValidationError('Пароли не совпадают')
        return self.cleaned_data

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=True)
        user.email=self.cleaned_data['email']
        user.first_name=self.cleaned_data['first_name']
        user.last_name=self.cleaned_data['last_name']
        user.dob=self.cleaned_data['dob']
        user.login=self.cleaned_data['login']
        user.mobile=self.cleaned_data['mobile']
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
