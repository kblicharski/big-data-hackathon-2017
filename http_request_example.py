# You aren't limited to using raw sockets to make network connections.
# Python can make HTTP requests quite easily.

# First you'll need to import the urllib2 module.
import urllib2

# Then you need to open the URL:
response = urllib2.urlopen("http://127.0.0.1:8080")

# Now you just need to read the contents of the response:
html = response.read()
print(html)

# CHALLENGE 1: Make a connection to: 127.0.0.1:8080/winning and print
#              the response.
response = urllib2.urlopen("http://127.0.0.1:8080/winning")
html = response.read()
print(html)

