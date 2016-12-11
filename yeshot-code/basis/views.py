from django.shortcuts import render
from django.contrib.auth.models import User
from basis.models import Photostype, Posts,Userprofile,Comments,Photos,Likes
from basis.forms import RegisterForm, LoginForm, PhotostypeForm, ChangepwdForm, ShowaccountForm, NewtopicForm, UserproregisterForm, TypechoiceForm, UploadForm,NewcommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse,HttpResponseRedirect
from datetime import datetime
import os
from django.contrib.auth.models import AnonymousUser

def index(request):
	context_dict = {'welcome':"悦摄，开始你的摄影旅程"}
	return render(request,'basis/index.html',context_dict)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	
def studio(request):
	photoid = request.GET.get('photo')
	likedid = request.GET.get('liked')
	if photoid and likedid:
		if request.user.id:
			#upgrade the Photos.likedquantity
			liked = Photos.objects.get(id=photoid)
			liked.likedquantity += 1
			liked.save()
			#upgrade the userprofile.belikedquantity,mylikesquantity,
			beliked = Userprofile.objects.get(user_id=likedid)
			beliked.belikedquantity += 1
			beliked.save()
			userid = request.user.id
			mylikes = Userprofile.objects.get(user_id=userid)
			mylikes.mylikesquantity += 1
			mylikes.save()
			#update the likes model
			obj = Likes(photos_id = photoid,userprofile_id = likedid,user_id = userid)
			obj.save()
		else:
			return HttpResponseRedirect('/basis/account/')
	phototypes = Photostype.objects.all()
	typeid = request.GET.get('type')
	if typeid != '0':
		photos = Photos.objects.filter(type_id = typeid)
	else:
		photos = Photos.objects.all().order_by('-date')
	for photo in photos:
		newphoto = '../media/'+str(photo.photo)
		photo.photo = newphoto
	return render(request,'basis/studio.html',{'phototypes':phototypes,'photos':photos,'typeid':typeid,'photoid':photoid})
	
def shoter(request):
	shot = Userprofile.objects.all()[0:5]
	username=[]
	photos=[]
	belikes=[]
	likes=[]
	for line in shot:
		userid=line.user_id
		newusername = User.objects.get(id = userid)
		newuserprofile = Userprofile.objects.get(user_id=userid)
		newphotos = newuserprofile.photosquantity
		newbelikes = newuserprofile.belikedquantity
		newlikes = newuserprofile.mylikesquantity
		username.append(newusername)
		photos.append(newphotos)
		belikes.append(newbelikes)
		likes.append(newlikes)
	context_dict = {'shot':shot,'username':username,'photos':photos,'belikes':belikes,'likes':likes}
	return render(request,'basis/shoter.html',context_dict)

def forum(request):
	topics = Posts.objects.all()
	user = []
	for topic in topics:
		discrib = topic.discribtion[:16]+'...'
		topic.discribtion = discrib
		newuser = topic.user.username
		user.append(newuser)
	return render(request,'basis/forum.html',{'topics':topics,'user':user})

def comment(request):
	topicid = int(request.GET.get('comment'))
	comment = Comments.objects.filter(posts_id=topicid)
	content=[]
	date = []
	usercomment=[]
	for comm in comment:
		contentd = comm.content
		userid = int(comm.user_id)
		dated = comm.date
		usercommentd = User.objects.get(id=userid)
		content.append(contentd)
		date.append(dated)
		usercomment.append(usercommentd)
	return render(request,'basis/comment.html',{'content':content,'usercomment':usercomment,'date':date,'topicid':topicid})

def mylogin(request):
	if request.method == 'POST':
		data=request.POST
		username=data['username']
		password=data['password']
		user = authenticate(username=username,password=password)
		if user:
			if user.is_active:
				login(request,user)
				return HttpResponseRedirect('/basis/account/')
	return render(request, 'basis/mylogin.html')
	
def register(request):
	registered = False
	if request.method == 'POST':
		register_form = RegisterForm(data=request.POST)
		userproregister_form = UserproregisterForm(data=request.POST)
		data=request.POST
		if register_form.is_valid():
			register = register_form.save()
			register.set_password(register.password)
			register.save()
			userpro = userproregister_form.save(commit=False)
			userpro.user = register
			userpro.save()
			registered = True
		else:
			print(register_form.errors,userproregister_form.errors)
	else:
		register_form = RegisterForm()
	return render(request, 'basis/register.html',{'register_form':register_form,'registered':registered})

@login_required
def account(request):
	if request.method == 'GET':
		userid = request.user.id
		usernow = User.objects.get(id = userid)
		user = Userprofile.objects.get(user_id=userid)
		photos = user.photosquantity
		likes = user.mylikesquantity
		belikes = user.belikedquantity
	else:
		usernow='Nobody'
		photos = 0
		likes = 0
		belikes = 0
	return render(request,'basis/account.html',{'usernow':usernow,'photos':photos,'likes':likes,'belikes':belikes})

def mylogout(request):
	logout(request)
	return HttpResponseRedirect('/basis/account/')

@login_required
def newtopic(request):
	if request.method == 'POST':
		form = NewtopicForm(data=request.POST)
		requestid=request.user.id
		if form.is_valid():
			topic = form.save(commit=False)
			topic.user_id=requestid
			topic.save()
			return HttpResponseRedirect('/basis/forum/')
		else:
			print(form.errors)
	else:
		form = NewtopicForm()
	return render(request,'basis/newtopic.html',{'newtopic':form})

def newcomment(request):
	topicid = int(request.GET.get('topic'))
	if request.method == 'POST':
		form = NewcommentForm(data=request.POST)
		requestid=request.user.id
		if form.is_valid():
			comment = form.save(commit=False)
			comment.user_id=requestid
			comment.posts_id=topicid
			comment.save()
			return HttpResponseRedirect('/basis/forum/comment/?comment=%d'%topicid)
		else:
			print(form.errors)
	else:
		form = NewcommentForm()
	return render(request,'basis/newcomment.html',{'newcomment':form,'topicid':topicid})
	
def changepwd(request):
	if request.method == 'GET':
		form = ChangepwdForm()
		return render(request, 'basis/changepwd.html',{'form': form,})
	else:
		form = ChangepwdForm(request.POST)
		if form.is_valid():
			username = request.user.username
			oldpassword = request.POST.get('oldpassword', '')
			user = auth.authenticate(username=username, password=oldpassword)
			if user is not None and user.is_active:
				newpassword = request.POST.get('newpassword1', '')
				user.set_password(newpassword)
				user.save()
				return render(request, 'basis/index.html',{'changepwd_success':True})
			else:
				return render(request, 'basis/changepwd.html',{'form': form,'oldpassword_is_wrong':True})
		else:
			return render(request, 'basis/changepwd.html',{'form': form,})

@login_required
def upload(request):
	uploaded=False
	types = Photostype.objects.all()
	if request.method == 'POST':
		form = UploadForm(data=request.POST)
		typeid = request.POST.get("typeselect",1)
		userid = request.user.id
		if not userid:
			userid = 1
		if form.is_valid():
			upload = form.save(commit=False)
			upload.type_id=typeid
			upload.user_id=userid
			if 'photo' in request.FILES:
				upload.photo = request.FILES['photo']
			upload.save()
			uploaded=True
		else:
			print(form.errors)
	else:
		form=UploadForm()
	return render(request,'basis/upload.html',{'form':UploadForm,'types':types,'uploaded':uploaded})