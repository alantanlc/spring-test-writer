
from tkinter import W
from . import ClassFile
from . import ClassVariable
from . import ClassMethod

class ClassFilerParser:

    def parse(self, file_name):
        """ Parse """
        classFile = ClassFile(file_name)
        with open(file_name, 'r') as f:
            content = f.readlines()
            classFile.file_name = file_name
            classFile.package = self.get_package(content)
            classFile.name = self.get_name(content)
            classFile.variables = self.get_variables(content)
            classFile.methods = self.get_methods(content)
        return classFile

    def get_package(self, content):
        return 'package'

    def get_name(self, content):
        return 'name'

    def get_variables(self, content):
        variable = ClassVariable()
        return [variable]

    def get_methods(self, content):
        method = ClassMethod()
        return [method]
