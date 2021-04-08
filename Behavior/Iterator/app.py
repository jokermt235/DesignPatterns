from Collection import Collection
from PythonDeveloper import PythonDeveloper
dev1 = PythonDeveloper("Antonio Conte",["DJANGO","FLASK","REST","MESR"])

iterator = dev1.getIterator()
print(dev1.getName())
while(iterator.hasNext()):
    print("Skills : " + str(iterator.next()))