from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms
# 注册表单
class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")

# class RegisterForm(UserCreationForm):
#     username = forms.CharField(label='用户名', max_length=100)
#     password = forms.CharField(label='密码', widget=forms.PasswordInput())
#     password2 = forms.CharField(label='确认密码', widget=forms.PasswordInput())
#     class Meta(UserCreationForm.Meta):
#         model = User
#         fields = ("username", "email")
#     def clean(self):
#         if not self.is_valid():
#             raise forms.ValidationError('所有项都为必填项')
#         elif self.cleaned_data['password2'] != self.cleaned_data['password']:
#             raise forms.ValidationError('两次输入密码不一致')
#         else:
#             cleaned_data = super(RegisterForm, self).clean()
#         return cleaned_data



# 登录表单
class LoginForm(forms.Form):
    username = forms.CharField(label='用户名',widget=forms.TextInput(attrs={"placeholder": "用户名", "required": "required",}),
                               max_length=50, error_messages={"required": "username不能为空",})
    password = forms.CharField(label='密码',widget=forms.PasswordInput(attrs={"placeholder": "密码", "required": "required",}),
                               max_length=20, error_messages={"required": "password不能为空",})