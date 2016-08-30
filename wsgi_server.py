

from wsgiref.simple_server import make_server

from wsgi_hello import application

port = 3000
httpd = make_server('', port, application)

print "Server HTTP On Port %d..." %(port)

httpd.serve_forever()
