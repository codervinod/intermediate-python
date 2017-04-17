#!/usr/bin/python
import cgi
import cgitb; cgitb.enable()

print "Content-Type: text/html"     # HTML is following
print                               # blank line, end of headers

print "<TITLE>CGI script output</TITLE>"
form = cgi.FieldStorage()
print '<h1>What you submitted</h1>'
print '<table><tbody>'
for k in form.keys():
    v = form.getvalue(k)
    print '<tr><th>{}</th><td>{}</td></tr>'.format(k, v)
print '</tbody></table>'

print '<a href="/">Return to index</a>'
