# coding: utf-8

from setuptools import setup, find_packages

package_name = 'dancestar'

setup(
    name=package_name,
    author='dmirain',
    author_email='dmirain@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            '%s = %s.manage:django_main' % (package_name, package_name),
        ]
    },
)
