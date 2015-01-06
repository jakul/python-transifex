# python-transifex
A python API to the Transifex translation service (www.transifex.com). This API wrapper makes it easier to communicate with Transifex. The wrapper does not expose all of the underlying functionality of the Transifex API.

This wrapper is compatible with both www.transifex.com and Transifex Community Edition (self hosted).

## Usage

### Authentication
To connect to transifex:

    In [2]: from transifex.api import TransifexAPI
    
    # Replace `username` and `password` here with your own username and password
    In [3]: t = TransifexAPI('username', 'password', 'http://transifex.com')
    
    In [4]: t.ping()
    Out[4]: True

### Projects
#### Create a new public project

Public projects require a `repository_url`. This can be any valid URL. 
Private projects do mnot require this, but you must have a Transifex plan 
which allows private projects.

    In [3]: t.new_project('helloworld5', repository_url='http://gmail.com')
    
#### Check if a project already exists

    In [9]: t.project_exists('helloworld5')
    Out[9]: True
    
    In [10]: t.project_exists('helloworld44345')
    Out[10]: False

### Resources
#### List resources

    In [13]: t.list_resources('helloworld5')
    Out[13]: 
    [{u'categories': None,
      u'i18n_type': u'PO',
      u'name': u'pofilepo',
      u'priority': u'1',
      u'slug': u'pofilepo',
      u'source_language_code': u'en_GB'}]


#### Create a resource

    In [16]: t.new_resource('helloworld5', '/src/python-transifex/pofile.po', resource_slug='anotherpofile')            
    t.new_translation('helloworld5, 'pofilepo', 'pt-br','/src/python-transifex/pofile.po'):

#### Delete a resource

    In [17]: t.delete_resource('helloworld5', 'anotherpofile')

#### List the languages this resource is translated into

    In [20]: t.list_languages('helloworld5', 'pofilepo')
    Out[20]: [u'en_GB']


#### Uploading translations to Transifex

    In [22]: t.new_translation('helloworld5', 'pofilepo', 'pt-br','/src/python-transifex/pofile.po')
    Out[22]: 
    {u'redirect': u'/projects/p/helloworld5/resource/pofilepo/',
     u'strings_added': 0,
     u'strings_delete': 0,
     u'strings_updated': 0}


#### Downloading translations from Transifex

    In [23]: t.get_translation('helloworld5', 'pofilepo', 'pt-br', '/src/python-transifex/pofile_ptbr.po')

