#
# Example file for working with filesystem shell methods
#
import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile


def main():
  # make a duplicate of an existing file
  if path.exists("testfile1.txt"):
    # get the path to the file in the current directory
    src = path.realpath("testfile1.txt")
    print("path exist ",src)
    
    # let's make a backup copy by appending "bak" to the name
    dest = src + ".bak"
    print("dest path ",dest)
    
    # copy over the permissions, modification times, and other info
    shutil.copy(src, dest)
    shutil.copystat(src, dest)
    
    # rename the original file
    os.rename("testfile1.txt","testfile2.txt")
  
    
    # now put things into a ZIP archive
  if path.exists("Ex_Files_Learning_Python_Upd"):
    get the path to the file in the current directory
    srcdir = path.realpath("Ex_Files_Learning_Python_Upd")
    print("path exist ",srcdir)
    rootdir, filename =path.split(srcdir)
    shutil.make_archive("archive","zip",rootdir)

    # more fine-grained control over ZIP files
    with ZipFile("zipfile1.zip","w") as newzip:
      newzip.write("D:\Python\Ex_Files_Learning_Python_Upd\Ex_Files_Learning_Python_Upd\Exercise Files\Ch2")
      newzip.write("testfile2.txt")
      
if __name__ == "__main__":
  main()
