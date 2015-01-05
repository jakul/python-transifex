import os
from setuptools import setup, find_packages
import sys

from transifex import VERSION

if sys.argv[-1] == 'publish-to-pypi':
    os.system("python setup.py sdist upload -r pypi")
    os.system("git tag -a %s -m 'version %s'" % (VERSION, VERSION))
    os.system("git push --tags")
    sys.exit()

setup(
    name='python-transifex',
    version=VERSION,
    description='A python api to transifex',
    author='Craig Blaszczyk',
    author_email='masterjakul@gmail.com',
    url='https://github.com/jakul/python-transifex',
    license='BSD',
    packages=find_packages(),
    tests_require=['mock',
    ],
    install_requires=['requests',
    ],
    include_package_data=True,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
