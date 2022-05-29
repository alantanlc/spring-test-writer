

class ClassFile:

    def __init__(self, name, variables = [], classes = []):
        print(f'TestFile')
        self.name = name
        self.variables = variables
        self.classes = classes

    def load(self):
        """ Load contents of file """
        content = ""
        return content

    def parse(self, content):
        """ Parse content """
        self.variables = self.get_variables(content)
        self.classes = self.get_classes(content)

    def get_variables(self, content):
        """ Get variables """
        
    def get_class_methods(self, content):
        """ Get class methods """
