#
# Example file for working with os.path module
#
import os
import platform
from os import path
import datetime
from datetime import date, time, timedelta
import time


def main():
  # Print the name of the OS
  print(os.name)
  print(platform.system(), platform.release())

  
  # Check for item existence and type
  print("Item exists: "+ str(path.exists("testfile1.txt")))
  print("Item is file: "+ str(path.isdir("testfile1.txt")))
  print("Item is file: "+ str(path.isfile("testfile1.txt")))
  # Work with file paths
  print("Item is file: "+ str(path.realpath("testfile1.txt")))
  print("Item is file: "+ str(path.split(path.realpath("testfile1.txt"))))
  
  # Get the modification time
  t = time.ctime(path.getmtime("testfile1.txt"))
  print(t)
  print(datetime.datetime.fromtimestamp(path.getmtime("testfile1.txt")))
  
  # Calculate how long ago the item was modified
  timeago= datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("testfile1.txt"))
  print(timeago)
  print(timeago.total_seconds())
  
if __name__ == "__main__":
  main()
