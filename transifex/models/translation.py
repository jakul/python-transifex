import pprint

class Translation(object):

    def __init__(self, api, project, resource, language_code):
        self._api = api
        self.info = None
#        self._mimetype = None
#        self._populated = False
        self.resource = resource
        self.project = project
        self.language_code = language_code
        
    def _populate(self):
        self._info = self._api.get_translation(
            self.project.slug, self.resource.slug, self.language_code
        )

#    def __setattr__(self, name, value):
#        """
#        Set the value of a field.
#        """
#        if name in self._info:
#            return self._info[name]
#        else:
#            msg = "%s has no attribute %s" % (self.__class__.__name__, name)
#            raise AttributeError(msg)
        
    def _get_content(self):
        if self._content is None:
            self._populate()
            
        return self._info['content']
    
    def _set_content(self, value):
        self._info['content'] = value
        self._modified = True
    
    content = property(_get_content, _set_content)
        
    def _get_mimetype(self):
        if self._mimetype is None:
            self._populate()
            
        return self._info['mimetype']
    
    def _set_mimetype(self, value):
        self._info['mimetype'] = value
        self._modified = True
    
    mimetype = property(_get_mimetype, _set_mimetype)
    
    def save(self):
        if self._modified:
            self._api.new_translation(
                self.project.slug, self.resource.slug, self.language_code,
                content=self.content
            )