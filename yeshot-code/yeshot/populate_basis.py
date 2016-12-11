import os
os.environ.setdefault('Yeshot_SETTINGS_MODULE', 'yeshot.settings')

import django
django.setup()

from basis.models import Userprofile, Photostype, Photos, Likes, Posts, Comments]

def populate():
	python_cat = add_cat('Python')
	
	