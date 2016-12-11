from django.db import models
from django.contrib.auth.models import User

#creat tables
class Userprofile(models.Model):
	user = models.OneToOneField(User)
	head = models.ImageField(upload_to='head',null=True,blank=True)
	mylikesquantity = models.IntegerField(default=0)
	belikedquantity= models.IntegerField(default=0)
	photosquantity = models.IntegerField(default=0)
	
	def __str__(self):
		return self.profileuser.username
	
	class Meta:
		ordering = ['-belikedquantity']
		
class Photostype(models.Model):
	type = models.CharField(default='Others',max_length=23)
	quantity = models.IntegerField(default = 0)
	
	def __str__(self):
		return self.type
		
	class Meta:
		ordering = ['-quantity']
		
class Photos(models.Model):
	photo = models.ImageField(upload_to = 'photo',blank = True,null=False)
	date = models.DateTimeField(auto_now=True)
	photosay = models.CharField(max_length = 128)
	likedquantity = models.IntegerField(default = 0)
	user = models.ForeignKey(User)
	type = models.ForeignKey(Photostype)
	
	def __str__(self):
		return self.user.username
		
	class Meta:
		ordering = ['-likedquantity']
		
class Likes(models.Model):
	user = models.ForeignKey(User)
	photos = models.ForeignKey(Photos)
	userprofile = models.ForeignKey(Userprofile)
	date = models.DateTimeField(auto_now=True)
	
	def __str__(self):
		return self.likedphoto.photosay
		
class Posts(models.Model):
	title = models.CharField(null = False,max_length=24)
	discribtion = models.CharField(null = False,max_length = 120)
	date = models.DateTimeField(auto_now=True)
	commentsquantity = models.IntegerField(default = 0)
	user = models.ForeignKey(User)
	
	def __str__(self):
		self.title
		
	class Meta:
		ordering = ['-commentsquantity']
		
class Comments(models.Model):
	content = models.CharField(max_length=300)
	date = models.DateTimeField(auto_now=True)
	user = models.ForeignKey(User)
	posts = models.ForeignKey(Posts)
	
	def __str__(self):
		return self.content