
#
# Read and write files using the built-in Python file methods
#

def main():  
  # Open a file for writing and create it if it doesn't exist
  file1 =open("testfile1.txt", "w+" )
   # write some lines of data to the file
  for i in range(10):
    file1.write("this is test lines  "+str(i)+"\r\n")
  # close the file when done
  file1.close()
  
  
  # Open the file for appending text to the end
  file2 =open("testfile1.txt", "a" )
   # write some lines of data to the file
  for i in range(10):
    file2.write("this is test lines  "+str(i)+"\r\n")
  # close the file when done
  file2.close()
 
  # Open the file back up and read the contents
  file3 =open("testfile1.txt", "r" )
  if file3.mode == 'r':
    contents=file3.read()
    print(contents)
  
  file3.close()
  #read line by line 
  file4 =open("testfile1.txt", "r" )
  if file4.mode == 'r':
    contentline=file4.readlines()
    for x in contentline:
      print(x)
  file4.close()

  
 
 

    
if __name__ == "__main__":
  main()
