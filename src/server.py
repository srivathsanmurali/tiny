#!/usr/bin/python3
from http.server import HTTPServer, CGIHTTPRequestHandler
import sys

def serveAtPort(PORT):
    try:
        host_name = "localhost"
        httpd =  HTTPServer((host_name, PORT) , CGIHTTPRequestHandler)
        print ("Serving at port ", PORT)
        print ("<ctrl-C> to Quit")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print ("Server closed at port ", PORT)
        sys.exit(0)
