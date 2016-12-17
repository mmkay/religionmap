=====
religionmap
=====

religionmap is a simple Django app to show which religion is popular in area.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "map" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'map',
    ]

2. Include the polls URLconf in your project urls.py like this::

    url(r'^map/', include('map.urls')),

3. Run `python manage.py migrate` to create the map models.

4. Visit http://127.0.0.1:8000/map/ to use the map.
