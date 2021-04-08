from Collection import Collection
from Iterator import Iterator
class PythonDeveloper:
    name = None
    skills = []
    def __init__(self, name : str, skills : list):
        self.name = name
        self.skills = skills
    def getName(self) -> str:
        return self.name
    def setName(self, name):
        self.name = name
    def getSkills(self)-> list:
        return self.skills

    def setSkills(self, skills: list):
        self.skills = skills
    def getIterator(self):
        return self.SkillsIterator(self)

    class SkillsIterator(Iterator):
        index = 0
        outer = None
        def __init__(self,outer):
            self.outer = outer
        def hasNext(self) -> bool:
            if self.index < len(self.outer.skills) - 1:
                return True
            return False
        def next(self) -> object :
            self.index += 1 
            return self.outer.skills[self.index]
