from . import Access

class ClassMethod:

    def __init__(self, name, access=Access.DEFAULT, return_type='void', parameters=[], exceptions=[]):
        self.name = name
        self.access = access
        self.return_type = return_type
        self.parameters = parameters
        self.exceptions = exceptions
