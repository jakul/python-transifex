# python-transifex
[![build-status-image]][travis-url]

**A Python API to the Transifex translation service (www.transifex.com).**

This API wrapper makes it easier to communicate with Transifex. The wrapper does not expose all of the underlying functionality of the Transifex API. This wrapper is compatible with both www.transifex.com and Transifex Community Edition (self hosted).


## Usage

### Authentication
To connect to transifex:

    In [1]: from transifex.api import TransifexAPI

    # Replace `username` and `password` here with your own username and password
    In [2]: t = TransifexAPI('username', 'password', 'http://transifex.com')

    In [3]: t.ping()
    Out[3]: True

### Projects
#### Create a new public project
Public projects require a `repository_url`. This can be any valid URL.
Private projects do mnot require this, but you must have a Transifex plan
which allows private projects.

    In [4]: t.new_project('helloworld5', repository_url='http://gmail.com')

#### Check if a project already exists

    In [5]: t.project_exists('helloworld5')
    Out[5]: True

    In [6]: t.project_exists('helloworld44345')
    Out[6]: False

### Resources
A resource is a set of strings which need to be translated into one or more
other languages.

#### Create a resource

    In [7]: t.new_resource('helloworld5', '/src/python-transifex/pofile.po', resource_slug='anotherpofile')

#### List resources

    In [8]: t.list_resources('helloworld5')
    Out[8]:
    [{u'categories': None,
      u'i18n_type': u'PO',
      u'name': u'anotherpofile',
      u'priority': u'1',
      u'slug': u'anotherpofile',
      u'source_language_code': u'en_GB'}]


#### Delete a resource

    In [9]: t.delete_resource('helloworld5', 'anotherpofile')


#### List the languages this resource is translated into

    # First, recreate the resource on the Tranisfex server
    in [10]: t.new_resource('helloworld5', '/src/python-transifex/pofile.po')

    In [11]: t.list_languages('helloworld5', 'pofilepo')
    Out[11]: [u'en_GB']


#### Uploading translations to Transifex
If you have up to date translations in your codebase, you should update them to
Transifex so that the translators don't have to translate everything from
scratch.

    In [12]: t.new_translation('helloworld5', 'pofilepo', 'pt-br','/src/python-transifex/pofile.po')
    Out[12]:
    {u'redirect': u'/projects/p/helloworld5/resource/pofilepo/',
     u'strings_added': 0,
     u'strings_delete': 0,
     u'strings_updated': 0}


#### Downloading translations from Transifex
To download the translations and store them in a local file run the following:

    In [13]: t.get_translation('helloworld5', 'pofilepo', 'pt-br', '/src/python-transifex/pofile_ptbr.po')

#### Working with translations directly
To list all the translations via the api:
    In [14]: t.list_translation_strings('helloworld5', 'resourceName', 'pt-br')

To get a single translation
    In [15]: t.get_translation_string('helloworld5', 'resourceName', 'pt-br', "Some untranslated text")

To upload a single translation
    In [16]: t.put_translation_string('helloworld5', 'resourceName', 'pt-br', "Some untranslated text", "Some translated text")

[build-status-image]: https://travis-ci.org/jakul/python-transifex.svg?branch=master
[travis-url]: https://travis-ci.org/jakul/python-transifex

