========
KDV Kids
========

KDV Kids is a module for the Dutch Kinderdagverblijf kids. 
It makes groups, teachers, parents and kids.

Quick start
-----------

1. Add "polls" to your INSTALLED_APPS setting like this::

      INSTALLED_APPS = (
          ...
          'kdv_kids',
      )

2. Include the polls URLconf in your project urls.py like this::

      url(r'^kdv_kids/', include('kids.urls')),

3. Run `python manage.py syncdb` to create the kdv kids models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).