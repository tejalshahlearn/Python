# Example of Classes 
class testclass():
    def testclassmethod1 (self):
        print("testclassmethod1")
    def testclassmethod2 (self,somestr):
        print("testclassmethod2"+somestr)

class testclass2(testclass):
    def testclass2method1 (self):
        testclass.testclassmethod1(self)
        print("testclassmethod1")
    def testclass2method2 (self,somestr):
        print("testclassmethod2")

def main(): 
    test = testclass()
    test2 = testclass2()
    test2.testclass2method1()
    test2.testclass2method2("tet")
    test.testclassmethod1()
    test.testclassmethod2("strings jksadk")
    print("Hello world main ")
if __name__ == "__main__" :
  main()