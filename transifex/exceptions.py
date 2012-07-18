class TransifexException(Exception):
    pass

class TransifexAPIException(TransifexException):
    def __init__(self, response=None):
        super(TransifexAPIException, self).__init__(response)
        self.response = response

    def __str__(self):
        if self.response is None:
            return super(TransifexAPIException, self).__str__()
        return '%s: %s' % (
            self.response.status_code, self.response.content
            )

class InvalidSlugException(TransifexException):
    pass