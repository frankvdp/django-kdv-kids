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
