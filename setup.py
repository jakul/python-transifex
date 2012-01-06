from setuptools import setup, find_packages

setup(
    name='python-transifex',
    version='0.0.1-dev',
    description='A python api to transifex',
    long_description=open('README.rst').read(),
    author='Craig Blaszczyk',
    author_email='masterjakul@gmail.com',
    url='https://github.com/jakul/python-transifex',
    download_url='https://github.com/jakul/python-transifex/downloads',
    license='BSD',
    packages=find_packages(),
    tests_require=[
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