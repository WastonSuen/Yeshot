from django import forms
from django.contrib.auth.models import User
from basis.models import Userprofile,Photostype,Photos,Likes,Posts,Comments

class RegisterForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	
	class Meta:
		model = User
		fields = ('first_name','last_name','username','email','password',)
		
class LoginForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = User
		fields = ('username','password',)
		
class UserproregisterForm(forms.ModelForm):
	class Meta:
		model = Userprofile
		fields = ()
		
class PhotostypeForm(forms.ModelForm):
	class Meta:
		model = Photostype
		fields = ('type',)

class TypechoiceForm(forms.Form):
	typed = Photostype.objects.all().values('type')
	length = len(typed)
	types=[]
	for i in range(length):
		typechoice=typed[i]['type']
		types.append((i,typechoice))
	type = forms.ChoiceField(choices=types,label='图片类型')
	

class UploadForm(forms.ModelForm):
	class Meta:
		model = Photos
		fields = ('photo','photosay',)

class ChangepwdForm(forms.Form):
	oldpassword = forms.CharField(
		required=True,
		label=u"原密码",
		error_messages={'required': u'请输入原密码'},
		widget=forms.PasswordInput(
			attrs={
				'placeholder':u"原密码",
			}
		),
	) 
	newpassword1 = forms.CharField(
		required=True,
		label=u"新密码",
		error_messages={'required': u'请输入新密码'},
		widget=forms.PasswordInput(
			attrs={
				'placeholder':u"新密码",
			}
		),
	)
	newpassword2 = forms.CharField(
		required=True,
		label=u"确认密码",
		error_messages={'required': u'请再次输入新密码'},
		widget=forms.PasswordInput(
			attrs={
			'placeholder':u"确认密码",
			}
		),
	)
	def clean(self):
		if not self.is_valid():
			raise forms.ValidationError(u"所有项都为必填项")
		elif self.cleaned_data['newpassword1'] != self.cleaned_data['newpassword2']:
			raise forms.ValidationError(u"两次输入的新密码不一样")
		else:
			cleaned_data = super(ChangepwdForm, self).clean()
		return cleaned_data
		
class ShowaccountForm(forms.ModelForm):
	class Meta:
		model = Userprofile
		fields = ('mylikesquantity','photosquantity',)
		
class NewtopicForm(forms.ModelForm):
	class Meta:
		model = Posts
		fields = ('title','discribtion',)
		
class NewcommentForm(forms.ModelForm):
	class Meta:
		model = Comments
		fields = ('content',)