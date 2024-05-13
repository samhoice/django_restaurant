# Django Restaurant API

## Creation Steps

- create a virtual env
    - `python -m venv venv`
- create requirements.txt
- install requirements
    - `source ./venv/bin/activate`
    - `pip install -r requirements.txt`
- Create Django Project
    - `django-admin startproject django_restaurant`
    - The top level directory can be whatever name
        - This is the git repo
        - has the requirements.txt
        - the django project is `django_restaurant`
            - this will have app directories
            - this will have an app-like directory called project name
- Create Django App
    - `cd django_restaurant`
    - `./manage.py startapp restaurant`
- Attach app to project
    - settings.py
    - `INSTALLED_APPS`
    - add our app at the end - `restaurant`
- Create Models
    - restaurant/models.py
    - Models should inherit from class `Model` from `django.db.models`
    - Model fields such as `CharField` are also defined in `django.db.models`
- Create Migrations
    - `./manage.py makemigrations`
- Apply Migrations
    - `./manage.py migrate`

## Notes to this point

I created the Restaurant and Dish already, but they aren't needed until later. Probably need to talk about the data modeling involved in the restaurant metaphor. Start by assuming it's one dish to the restaurant. Then you can do One To Many. After that, you can talk about Many To Many. Goal now should be to give us a random dish from the restaurant.

Now we can use the repl to explore our `Dish` model.

`./manage.py shell`

This will open a python repl that has the django settings pre-loaded. So it's a django shell. Now we can import our models.

`from restaurant.models import Dish`

From here we can create a model instance:

`d = Dish(title="Soup", cuisine_type="All", category="DI", description="It's soup", price=12.99, spicy_level=1)`

and save it.

`d.save()`

Then it exists in the db. You can retrieve it with:

`Dish.objects.get(id=d.id)`

Objects is a model manager, and it lets you do interesting things with Django models. You can create and save in one step like SQL INSERT:

`Dish.objects.create(title="Sandwich", cuisine_type="All", category="LU", description="It's a sandwich", price=14.99, spicy_level=1)`

You can retrieve objects of that type, like SQL SELECT:

`Dish.objects.all()`

You can filter like a WHERE clause:

`Dish.objects.filter(title='Soup')`

Note that `.all()` and `.filter()` return querysets, which are iterables like lists. There are other methods like `.get()` that return a single object or throw.

`d = Dish.object.get(title='Soup')`

Now `d` is an instance of class Dish, and can be used like any object. Get the title:

`d.title`


## Running ORM commands from a script

You can use the Object Relational Mapper (ORM) from a management command or a standalone script. For management commands see:

`./management/commmands/custom_command.py`

for the simplest possible command and

`./management/commmands/orm_playground.py`

for an example of importing your data. For a standalone python script see:

`./standalone_script.py`

## An API endpoint

As an example I created an API endpoint using Django JsonResponse. It's in views dishview, and is wired into the urls.py


## Django Rest Framework

- djangorestframework should be in the requirements.txt
- add `rest_framework` to installed apps
- create serializers.py in `restaurant` app
    - `Meta` class is used in django to define certain infrastructure relationships rather than data relationships (like a foreign key)
- viewsets
    - Like views in regular django
    - Group together various parts of requests that often work together in CRUD APIs
    - viewset is to serializer as view is to template
- urls
    - several things going on
    - mostly though, you're creating a router and adding your viewsets to it
    - the router is responsible for handling the various HTTP methods your viewset accepts

At this point we can start our server and see our rest framework in the api browser at [localhost:8000/](http://localhost:8000/).

Authentication is already set up. If you add this line:

`permission_classes = [permissions.IsAuthenticated]`

into your serializer class it will require authentication to load your data (serializer). There is no login endpoint yet, but you can always log in through the admin. Note that `IsAuthenticated` only means you logged in as a valid user. Authorization and permissions are a separate thing.


## Deploy on fly

TODO: Install flyctl

In the app:

`fly launch`

- create the fly.toml
- create the dockerfile

`fly volume create <name>`

add [mounts] to fly.toml

`fly secrets set DATABASE_URL=sqlite3:///mnt/name/production.sqlite`

## CSRF

Cross Site Request Forgery (CSRF) - add this to settings.py

This allows requests from both fly and local.

```python
CSRF_TRUSTED_ORIGINS = [f'https://{APP_NAME}.fly.dev', 'http://localhost:8000']
```

## Whitenoise

`pip install whitenoise`

set STATIC_ROOT in settings

- `STATIC_ROOT = BASE_DIR / "staticfiles"`

Add WhiteNoise middleware to settings MIDDLEWARE immediately after SecurityMiddleware

    `"whitenoise.middleware.WhiteNoiseMiddleware",`

Add STORAGES block to settings.py to enable compression

```python
STORAGES = {
    # ...
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}
```

Don't forget to run `./manage.py collectstatic` before deploy.
