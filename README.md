# What is this?

Code for the **Blog app** in this tutorial: https://www.wdtutorials.com/django/forms-with-modelform

Video available here: https://www.youtube.com/watch?v=gMM1rtTwKxE

# Installation

- Setup a basic Django project: https://www.wdtutorials.com/django/minimal-project/
- Go to the project root and clone this repo there:

```
git clone https://github.com/WDTutorials/django-forms-with-modelform blog
```

Now you should have this kind of folder structure:


```
├── blog
│   ├── __init__.py
│   ├── __pycache__
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations
│   ├── models.py
│   ├── templates
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── manage.py
└── mysite
    ├── __init__.py
    ├── __pycache__
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

- Open **settings** file: 

```
vim mysite/settings.py 
```

and add **blog** app to **INSTALLED_APPS**:

```
'django.contrib.staticfiles',
'blog', # -- here --
```

- Open main **urls.py** file:

```
vim mysite/urls.py
```

Import **include** add **blog.urls** patterns:

```
from django.conf.urls import url, include # -- here --
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('blog.urls')), # -- here --
]
```
