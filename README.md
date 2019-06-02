This is a project manager app, based on  based on [Django](https://docs.djangoproject.com/en/2.2/).

You can test the sample at [https://django-project-manager.appspot.com](https://django-project-manager.appspot.com), with admin:adminy and password:password.

## For who?
If you are looking for simple task management tool that can share the project issues and related tasks, this is for you.

## How to test locally?
In the folder where `manage.py` locates, run the following command
`$python manage.py runserver`

## How to upload the app to the server?
The test site is hosted with Google Cloud App engine.
- [Google Cloud](https://cloud.google.com/python/django/appengine)
- [AWS](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html)

## Which file to customized?
Followins are the list of which file to modify
- Database structure (Issue, Tasks..): `dashboard/models.py`
- What to show, how function in the admin site: `dashboard/admin.py`
- Admin site css: `static/admin/css/`
- Admin site template html: `templates/admin/`
css and html files are copied from Django source files and copied to the app directory. You can find your source files by running the folloing comannd
```
$ python -c "import django; print(django.__path__)"
```
Foe example, to find the templates sources, navigate to `django/contrib/admin/templates`

## How to add/remove users from terminal?
- Add users
```
$python manage.py createsuperuser
```
- Remove users
```
$ python manage.py shell
$ from django.contrib.auth.models import User
$ User.objects.get(username="[TARGET_USERNAME]", is_superuser=True).delete()
```


