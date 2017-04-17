#!/usr/bin/python
import os
import cgi
import json
import cgitb; cgitb.enable()

print "Content-Type: application/json"
print

form = cgi.FieldStorage()
resp = {'HTTP_METHOD': os.environ['REQUEST_METHOD']}
for k in form.keys():
    resp[k] = form.getvalue(k)

print json.dumps(resp)