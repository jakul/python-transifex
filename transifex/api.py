"""
Transifex API
"""
import codecs
import requests
import json
import os
from transifex.exceptions import TransifexAPIException, InvalidSlugException
from transifex.util import slugify

class TransifexAPI(object):
    def __init__(self, username, password, host):
        """
        @param username the username to use when connecting
        @param password the password to use when connecting
        @param host the host string
        """            
        self._username = username
        self._password = password
        self._host = host
            
        if self._host.endswith('/'):
            self._host = self._host[:-1]
        
        self._auth = (self._username, self._password)
        self._base_api_url = '%s/api/2' % (self._host)

    def new_project(self, slug, name=None, source_language_code=None,
                    outsource_project_name=None):
        """
        Create a new project on transifex
        
        @param slug
            the project slug
        @param name (optional)
            the project name, defaults to the project slug
        @param source_language_code (optional)
            the source language code, defaults to 'en-gb'
        @param outsource_project_name (optional)
            the name of the project to outsource translation team management to
            
        @returns None
           
        @raises `TransifexAPIException`
           if project was not created properly
        """
        
        if slug != slugify(slug):
            raise InvalidSlugException('%r is not a valid slug' % (slug))
        if name is None:
            name = slug
        if source_language_code is None:
            source_language_code = 'en-gb'
        
        url = '%s/projects/' % self._base_api_url
        headers = {'content-type': 'application/json'}
        data = {
            'name': name, 'slug': slug,
            'source_language_code': source_language_code, 'description': name
        }
        if outsource_project_name is not None:
            data['outsource'] = outsource_project_name
#        description
#        long_description
#        private
#        homepage
#        feed
#        anyone_submit
#        hidden
#        bug_tracker
#        trans_instructions
#        tags
#        maintainers
        
        response = requests.post(
             url, data=json.dumps(data), auth=self._auth, headers=headers,
             
        )
        
        if response.status_code != requests.codes['CREATED']:
            raise TransifexAPIException(response)
     
    def list_resources(self, project_slug):
        """
        List all resources in a project
        
        @param project_slug
            the project slug
            
        @returns list of dictionaries with resources info
            each dictionary may contain
                category
                i18n_type
                source_language_code
                slug
                name
           
        @raises `TransifexAPIException`
        """
        url = '%s/project/%s/resources/' % (self._base_api_url, project_slug)
        response = requests.get(url, auth=self._auth)
        
        if response.status_code != requests.codes['OK']:
            raise TransifexAPIException(response)
        
        return json.loads(response.content)
        
    def new_resource(self, project_slug, path_to_pofile, resource_slug=None,
                     resource_name=None):
        """
        Creates a new resource with the specified slug from the given file.
        
        @param project_slug
            the project slug
        @param path_to_pofile
            the path to the pofile which will be uploaded
        @param resource_slug (optional)
            the resource slug, defaults to a sluggified version of the filename
        @param resource_name (optional)
            the resource name, defaults to the resource name
            
        @return None
        
        @raises `TransifexAPIException`
        @raises `IOError`
        """
        url = '%s/project/%s/resources/' % (self._base_api_url, project_slug)
        content = open(path_to_pofile, 'r').read()

        __, filename = os.path.split(path_to_pofile)
        if resource_slug is None:
            resource_slug = slugify(filename)
        else:
            if resource_slug != slugify(resource_slug):
                raise InvalidSlugException(
                    '%r is not a valid slug' % (resource_slug)
                )
            
        if resource_name is None:
            resource_name = resource_slug
        
        headers = {'content-type': 'application/json'}
        data = {
            'name': resource_name, 'slug': resource_slug, 'content': content,
            'i18n_type': 'PO'
        }
#        slug
#        name
#        accept_translations
#        source_language
#        mimetype
#        content (in case of sending the content as one string)
#        category

        response = requests.post(
             url, data=json.dumps(data), auth=self._auth, headers=headers,
        )
        if response.status_code != requests.codes['CREATED']:
            raise TransifexAPIException(response)
        
    def update_source_translation(self, project_slug, resource_slug,
                                  path_to_pofile):
        """
        Update the source translation for a give resource
        
        @param project_slug
            the project slug
        @param resource_slug
            the resource slug
        @param path_to_pofile
            the path to the pofile which will be uploaded

        @return dictionary with info
            Info may include keys
                strings_added
                strings_updated
                redirect
        
        @raises `TransifexAPIException`
        @raises `IOError`
        """
        url = '%s/project/%s/resource/%s/content/' % (
            self._base_api_url, project_slug, resource_slug
        )
        content = open(path_to_pofile, 'r').read()
        headers = {'content-type': 'application/json'}
        data = {'content': content}
        response = requests.put(
             url, data=json.dumps(data), auth=self._auth, headers=headers,
        )
        
        if response.status_code != requests.codes['OK']:
            raise TransifexAPIException(response)
        else:
            return json.loads(response.content)
        
    def delete_resource(self, project_slug, resource_slug):
        """
        Deletes the given resource
        
        @param project_slug
            the project slug
        @param resource_slug
            the resource slug

        @return None
        
        @raises `TransifexAPIException`
        """
        url = '%s/project/%s/resource/%s/' % (
            self._base_api_url, project_slug, resource_slug
        )
        response = requests.delete(url, auth=self._auth)
        if response.status_code != requests.codes['NO_CONTENT']:
            raise TransifexAPIException(response)        
            
    def new_translation(self, project_slug, resource_slug, language_code,
                        path_to_pofile):
        """
        Creates or updates the translation for the specified language
        
        @param project_slug
            the project slug
        @param resource_slug 
            the resource slug
        @param language_code
            the language_code of the file
        @param path_to_pofile
            the path to the pofile which will be uploaded
            
        @return dictionary with info
            Info may include keys
                strings_added
                strings_updated
                redirect
            
        @raises `TransifexAPIException`
        @raises `IOError`
        """
        url = '%s/project/%s/resource/%s/translation/%s/' % (
            self._base_api_url, project_slug, resource_slug, language_code
        )
        content = open(path_to_pofile, 'r').read()
        headers = {'content-type': 'application/json'}
        data = {'content': content}
        response = requests.put(
             url, data=json.dumps(data), auth=self._auth, headers=headers,
        )
        
        if response.status_code != requests.codes['OK']:
            raise TransifexAPIException(response)
        else:
            return json.loads(response.content)
            
    def get_translation(self, project_slug, resource_slug, language_code,
                        path_to_pofile):
        """
        Returns the requested translation, if it exists. The translation is
        returned as a serialized string, unless the GET parameter file is
        specified.
        
        @param project_slug
            The project slug
        @param resource_slug 
            The resource slug
        @param language_code
            The language_code of the file.
            This should be the *Transifex* language code
        @param path_to_pofile
            The path to the pofile which will be saved
            
        @return None
            
        @raises `TransifexAPIException`
        @raises `IOError`
        """
        url = '%s/project/%s/resource/%s/translation/%s/' % (
            self._base_api_url, project_slug, resource_slug, language_code
        )
        output_path = path_to_pofile
        query = {
            'file': ''         
        }
        response = requests.get(url, auth=self._auth, params=query)
        if response.status_code != requests.codes['OK']:
            raise TransifexAPIException(response)
        else:
            handle = open(output_path, 'w')
            for line in response.iter_content():
                handle.write(line)
            handle.close()
            
    def list_languages(self, project_slug, resource_slug):
        """
        List all the languages available for a given resource in a project
        
        @param project_slug
            The project slug
        @param resource_slug
            The resource slug
            
        @returns list
            The language codes which this resource has translations 
           
        @raises `TransifexAPIException`
        """
        url = '%s/project/%s/resource/%s/' % (
            self._base_api_url, project_slug, resource_slug
        )
        response = requests.get(url, auth=self._auth, params={'details':''})
        
        if response.status_code != requests.codes['OK']:
            raise TransifexAPIException(response)
        
        content = json.loads(response.content)
        languages = [
            language['code'] for language in content['available_languages']
        ]
        return languages

    def project_exists(self, project_slug):
        """
        Check if there is a project with the given slug registered with 
        Transifex
        
        @param project_slug
            The project slug
            
        @return Boolean
           True is project exists
           False if not
        """
        url = '%s/project/%s/' % (
            self._base_api_url, project_slug
        )
        response = requests.get(url, auth=self._auth)
        if response.status_code == requests.codes['OK']:
            return True
        elif response.status_code == requests.codes['NOT_FOUND']:
            return False
        else:
            raise TransifexAPIException(response)

    def ping(self):
        """
        Check the connection to the server and the auth credentials
        """
        url = '%s/projects/' % (self._base_api_url)
        response = requests.get(url, auth=self._auth)
        return response.status_code == requests.codes['OK']
        