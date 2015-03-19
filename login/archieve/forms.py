#-*- coding: utf-8 -*-
from django import forms
from captcha.fields import CaptchaField

class UserForm(forms.Form):
    surname = forms.CharField(max_length=30, label="Фамилия")
    name =  forms.CharField(max_length=30, label="Имя")
    login = forms.CharField(max_length=30, label="Логин")
    password = forms.CharField(min_length=5, max_length=30, help_text="(Введите пароль 5-30 символов)", 
                                label="Пароль", widget=forms.PasswordInput())
    conf_password = forms.CharField(min_length=5, max_length=30, label="Подтвердтие пароль",
                                    widget=forms.PasswordInput())
    email = forms.EmailField(label="Почта")
    dob = forms.DateField(help_text="(Введите дату в формате: ГГГГ-ММ-ДД)", 
                           label="Дата рождения")
    mobile = forms.RegexField(r'^[0-9]{3}-[0-9]{7}$', label="Мобильный телефон",
                        help_text="(Введите телефон в формате: ***-*******)")
    captcha = CaptchaField(label="Защита от спама")

    def get_user(self, user_id):
       try:
          return User.objects.get(pk=user_id)
       except User.DoesNotExist:
          return None