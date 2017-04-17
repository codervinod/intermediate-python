import urllib, urllib2

url = 'http://isithackday.com/arrpi.php?'
data = urllib.urlencode(dict(text='Hello World'))
resp = urllib2.urlopen(url + data)

print resp.read()
