 import os
2 os.environ.setdefault('DJANGO_SETTINGS_MODULE',
3 'tango_with_django_project.settings')
4 5
import django
6 django.setup()
7 from rango.models import Category, Page
8 9
def populate():
10 # First, we will create lists of dictionaries containing the pages
11 # we want to add into each category.
12 # Then we will create a dictionary of dictionaries for our categories.
13 # This might seem a little bit confusing, but it allows us to iterate
14 # through each data structure, and add the data to our models.
15
16 python_pages = [
17 {"title": "Official Python Tutorial",
18 "url":"http://docs.python.org/2/tutorial/"},
19 {"title":"How to Think like a Computer Scientist",
20 "url":"http://www.greenteapress.com/thinkpython/"},
21 {"title":"Learn Python in 10 Minutes",
22 "url":"http://www.korokithakis.net/tutorials/python/"} ]
23
24 django_pages = [
25 {"title":"Official Django Tutorial",
26 "url":"https://docs.djangoproject.com/en/1.9/intro/tutorial01/"},
27 {"title":"Django Rocks",
28 "url":"http://www.djangorocks.com/"},
29 {"title":"How to Tango with Django",
30 "url":"http://www.tangowithdjango.com/"} ]
31
32 other_pages = [
33 {"title":"Bottle",
34 "url":"http://bottlepy.org/docs/dev/"},
35 {"title":"Flask",
36 "url":"http://flask.pocoo.org"} ]
37
38 cats = {"Python": {"pages": python_pages},
39 "Django": {"pages": django_pages},
40 "Other Frameworks": {"pages": other_pages} }
41
42 # If you want to add more catergories or pages,
43 # add them to the dictionaries above.
44
45 # The code below goes through the cats dictionary, then adds each category,
46 # and then adds all the associated pages for that category.
47 # if you are using Python 2.x then use cats.iteritems() see
48 # http://docs.quantifiedcode.com/python-anti-patterns/readability/
49 # for more information about how to iterate over a dictionary properly.
50
51 for cat, cat_data in cats.items():
52 c = add_cat(cat)
53 for p in cat_data["pages"]:
54 add_page(c, p["title"], p["url"])
55
56 # Print out the categories we have added.
57 for c in Category.objects.all():
58 for p in Page.objects.filter(category=c):
59 print("- {0} - {1}".format(str(c), str(p)))
60
61 def add_page(cat, title, url, views=0):
62 p = Page.objects.get_or_create(category=cat, title=title)[0]
63 p.url=url
64 p.views=views
65 p.save()
66 return p
67
68 def add_cat(name):
69 c = Category.objects.get_or_create(name=name)[0]
70 c.save()
71 return c
72
73 # Start execution here!
74 if __name__ == '__main__':
75 print("Starting Rango population script...")
76 populate()