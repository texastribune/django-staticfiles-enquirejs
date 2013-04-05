from setuptools import setup


setup(
    name='django-staticfiles-enquirejs',
    version=open("./VERSION").read(),
    description='enquire.js meets Django staticfiles',
    long_description=open('README.rst').read(),
    author='The Texas Tribune',
    author_email='tech@texastribune.org',
    maintainer_email='cchang@texastribune.org',
    url='http://github.com/texastribune/django-staticfiles-enquirejs/',
    packages=['enquirejs'],
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: JavaScript',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
)
