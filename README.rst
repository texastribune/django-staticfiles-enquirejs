django-staticfiles-enquirejs
==============================
`enquire.js`_ meets Django staticfiles


Usage
-----
This application is meant to be used with `django-staticfiles`_.  Make sure
that staticfiles setup and configured, then install this application using
`pip`_:

::

	pip install django-staticfiles-enquirejs

Finally, make sure that `enquirejs` is listed in your ``INSTALLED_APPS``.  You
can use this oneliner to add it as well:

::

	INSTALLED_APPS += ['enquirejs', ]


Build
-----

Using `make`:

1. Set VERSION to the target version to build
2. Run ``make``

makefile example::

    echo "1.5.6" > VERSION
    make

Using `build.py`:

1. Run `python support/build.py <version>` to build that version of enquirejs.
   This will also update the VERSION file.

build.py example::

    python support/build.py 1.5.6


.. _enquire.js: http://wicky.nillia.ms/enquire.js/
.. _django-staticfiles: https://github.com/jezdez/django-staticfiles
.. _pip: http://www.pip-installer.org/
