import urllib.request

req = urllib.request.urlopen("http://www.google.com")
print(req.read())
