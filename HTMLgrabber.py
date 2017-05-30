## Trawler that opens a URL of your choice and reads out the information on that page
## Written by Milton Li (March '17)

import urllib.request

# Change this to trawl the URL you want
myURL = ""

# Name of the output file goes here
myfile = "myfile.txt"

# Opens the URL and reads the input
fp = urllib.request.urlopen(myURL)
mybytes = fp.read()

# Writes the input to a target file
target = open(myfile, "wb")
target.write(mybytes)

fp.close()

print(mybytes)