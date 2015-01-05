# python-transifex
A python API to the Transifex translation service (www.transifex.com). This API wrapper makes it easier to communicate with Transifex. The wrapper does not expose all of the underlying functionality of the Transifex API.

This wrapper is compatible with both www.transifex.com and Transifex Community Edition (self hosted).

## Usage

### Authentication


To connect to transifex:

    In [2]: from transifex.api import TransifexAPI
    
    In [3]: t = Tr
    TransifexAPI  True          
    
    # Replace `username` and `password` here with your own username and password
    In [3]: t = TransifexAPI('username', 'password', 'http://transifex.com')
    
    In [4]: t.ping()
    Out[4]: True
