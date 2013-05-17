"""
django-xe-currencies
-----------------

Django-based currency exchange app synced with XE currencies API

"""
from setuptools import setup, find_packages


setup(
    name='django-xe-currencies',
    version='0.0.1',
    url='https://github.com/aisayko/django-xe-currencies',
    license='MIT License',
    author='Alex Isayko',
    author_email='alex.isayko@gmail.com',
    description='Django-based currency exchange app synced with XE currencies API.',
    keywords = "django currency XE sync",
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[
        'django-tastypie'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
