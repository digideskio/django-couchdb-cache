from setuptools import setup, find_packages

PACKAGE_VERSION = '0.1'

setup(
    name='django-couchdb-cache',
    author='ShuttleCloud Corp',
    author_email='dev@shuttlecloud.com',
    description='CouchDB cache application for Django',
    url='https://github.com/shuttlecloud/django-couchdb-cache.git',
    version=PACKAGE_VERSION,
    packages=find_packages(),
    include_package_data=False,
    zip_safe=False,
    scripts=[],
    install_requires=[
        'Django<=1.7.4',
        'CouchDB==0.10',
        'python-memcached'
    ],
    dependency_links=[
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 2',
    ]
)
