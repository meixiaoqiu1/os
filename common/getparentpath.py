import os

class GetParentPath():
    def get_parent_path(self):
        parent_path=os.path.split(os.path.realpath(__file__))[0]
        return parent_path
    def get_project_path(self):
        path=os.path.dirname(self.get_parent_path())
        return path




