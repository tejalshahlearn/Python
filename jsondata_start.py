# 
# Example file for parsing and processing JSON
#
import urllib.request
import json

def printResults(data):
  # Use the json module to load the string data into a dictionary
  theJSON = json.loads(data)
  
  # now we can access the contents of the JSON like any other Python object
  if "title" in theJSON["metadata"]:
    print(theJSON["metadata"]["title"],"json title ")
  
  # output the number of events, plus the magnitude and each event name  
    count =theJSON["metadata"]["count"]
    print(count)
  
  # for each event, print the place where it occurred
  for i in theJSON["features"]:
    print(i["properties"]["place"])
  print("---------\n")

  # print the events that only have a magnitude greater than 4
  for i in theJSON["features"]:
    if i["properties"]["mag"] >= 4.0:
      print("%2.1f" % i["properties"]["mag"], i["properties"]["place"])
  print("---------\n")
  # print only the events where at least 1 person reported feeling something
  for i in theJSON["features"]:
    feltreports=i["properties"]["felt"]
    if  feltreports != None:
      if i["properties"]["felt"] > 0:
        print("%2.1f" % i["properties"]["felt"], i["properties"]["place"])
  print("---------\n")
  
def main():
  # define a variable to hold the source URL
  # In this case we'll use the free data feed from the USGS
  # This feed lists all earthquakes for the last day larger than Mag 2.5
  urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

  # Open the URL and read the data
  webUrl = urllib.request.urlopen(urlData)
  urlcode= webUrl.getcode()
  print ("result code: " + str(urlcode))
  if (urlcode == 200):
    data=webUrl.read()
    #print(data)
  else:
    print("recived error"+urlcode)
  printResults(data)

if __name__ == "__main__":
  main()
 