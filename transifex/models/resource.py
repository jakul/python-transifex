import pprint

class Resource(object):
#    properties = [
#        'feed', 'source_language_code', 'description', 'tags', 'homepage',
#        'created', 'long_description', 'outsource', 'teams', 'bug_tracker',
#        'anyone_submit', 'maintainers', 'owner', 'trans_instructions', 'slug',
#        'resources', 'name'
#    ]

    
    def __init__(self, api, project, slug):
#        self._resources = {}
        self._api = api
        self._info = {}
        self._source_language_content = None
        self.slug = slug
        self.project = project
        
    def _populate(self):
        self._info = self._api.resource_details(self.project.slug, self.slug)
        print(self._info)

    def __getattr__(self, name):
        """
        Return the value of the field.
        """
        if name in self._info:
            return self._info[name]
        else:
            msg = "%s has no attribute %s" % (self.__class__.__name__, name)
            raise AttributeError(msg)
        
    def _get_source_language_content(self):
        if self._source_language_content is None:
            self._source_language_content = \
                self._api.get_source_translation(self.project.slug, self.slug)
        return self._source_language_content
    
    def _set_source_language_content(self, value):
        self._source_language_content = value
    
    source_language_content = property(
        _get_source_language_content, _set_source_language_content
    )