from django.conf.urls import url
from basis import views

urlpatterns = [
	url(r'^$',views.index,name='index'),
	url(r'^index/',views.index, name='index'),
	url(r'^studio',views.studio,name='studio'),
	url(r'^studio/$',views.studio,name='studio'),
	
	url(r'^upload',views.upload,name='upload'),
	url(r'^shoter',views.shoter,name='shorter'),
	url(r'^forum/$',views.forum,name='forum'),
	
	url(r'^account/',views.account,name='account'),
	url(r'^mylogin',views.mylogin,name='login'),
	url(r'^mylogin/$',views.mylogin,name='login'),
	url(r'^register',views.register,name='register'),
	url(r'^changepwd',views.changepwd,name='changepwd'),
	url(r'^mylogout',views.mylogout,name='logout'),
	
	url(r'^forum/newtopic',views.newtopic,name='newtopic'),
	url(r'^forum/comment/$',views.comment,name='comment'),
	url(r'^forum/newcomment/$',views.newcomment,name='newcomment'),
	
]