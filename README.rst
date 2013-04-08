django-staticfiles-enquirejs
==============================
`enquire.js`_ meets Django staticfiles


About enquire.js
----------------

`enquire.js`_ is a lightweight, pure javascript library (with no dependencies)
for programmatically responding to media queries.


Usage
-----
This application is meant to be used with `django.contrib.staticfiles`_ or
`django-staticfiles`_.  Make sure that staticfiles is set up and configured,
then install this application using `pip`_::

	pip install django-staticfiles-enquirejs

Finally, make sure that `enquirejs` is listed in your ``INSTALLED_APPS``.  You
can use this oneliner to add it as well::

	INSTALLED_APPS += ['enquirejs', ]

Adding enquire.js to your Django templates:

* Using `django.contrib.staticfiles`_ or `django-staticfiles`_ with a
  templatetag::

    {% load static from staticfiles %}
    <script src="{% static 'enquirejs/enquire.min.js' %}"></script>

* or the context variable ``STATIC_URL``::

    <script src="{{ STATIC_URL }}enquirejs/enquire.min.js"></script>

Build
-----

Using ``make``:

1. Set VERSION to the target version to build
2. Run ``make``

makefile example::

    echo "1.5.6" > VERSION
    make

Using `build.py`:

1. Run ``python support/build.py <version>`` to build that version of enquirejs.
   This will also update the VERSION file.

build.py example::

    python support/build.py 1.5.6


.. _license:

License
```````

This software is licensed under the `Apache Software License`. See the
``LICENSE`` file in the top distribution directory for the full license text.

`enquire.js`_ is licensed MIT (http://www.opensource.org/licenses/mit-license.php)

.. _enquire.js: http://wicky.nillia.ms/enquire.js/
.. _django.contrib.staticfiles: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/
.. _django-staticfiles: https://github.com/jezdez/django-staticfiles
.. _pip: http://www.pip-installer.org/
