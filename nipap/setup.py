#!/usr/bin/env python

from distutils.core import setup

import nipap

long_desc = open('README.rst').read()
short_desc = long_desc.split('\n')[0].split(' - ')[1].strip()

setup(
    name = 'nipapd',
    version = nipap.__version__,
    description = short_desc,
    long_description = long_desc,
    author = nipap.__author__,
    author_email = nipap.__author_email__,
    license = nipap.__license__,
    url = nipap.__url__,
    packages = ['nipap'],
    keywords = ['nipap'],
    requires = ['twisted', 'ldap', 'sqlite3', 'IPy', 'psycopg2'],
    data_files = [
				('/etc/nipap/', ['nipap.conf']),
				('/usr/sbin/', ['nipapd'])
	],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Telecommunications Industry',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.6',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware'
    ]
)