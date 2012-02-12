import pprint

class Project(object):
#    properties = [
#        'feed', 'source_language_code', 'description', 'tags', 'homepage',
#        'created', 'long_description', 'outsource', 'teams', 'bug_tracker',
#        'anyone_submit', 'maintainers', 'owner', 'trans_instructions', 'slug',
#        'resources', 'name'
#    ]
    
    def __init__(self, api, slug):
        self._resources = {}
        self._api = api
        self._info = {}
        self.slug = slug
        
    def _populate(self):
        self._info = self._api.project_details(self.slug)
        
#    def save
    
#    @property
#    def resources(self):
#        return self._resources
    
#    def _getremoteattr(self):
#        import pdb; pdb.set_trace()
#        print self.__name__
#        
#        return 'a'
#    
#    owner = property(_getremoteattr)

    def __getattr__(self, name):
        """
        Return the value of the field.
        """
        if name in self._info:
            return self._info[name]
        else:
            msg = "%s has no attribute %s" % (self.__class__.__name__, name)
            raise AttributeError(msg)