# declare a varaibles 
test1="0"
#print (test1)
#Re-declaring of var works 
#test1="abc"
#print (test1)
# error : diff type var cannot concanate 
#print ("test 1 is a var " + str(123))
#global vs local  vars 
def testfun():
  test1 ="local"
  print(test1 +" this is a local func")
testfun()
print(test1 + "this is  a global ")