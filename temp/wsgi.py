from cgi import parse_qs
import os

def application(environ, start_response):
    answer = ""
    o = parse_qs(environ['QUERY_STRING'])
    answer = answer +"get parameters = "+ str(o) + "<br>\n"
    start_response('200 OK', [('content-type', 'text/html')])
    try:
        request_body_size = int(environ.get('CONTENT_LENGTH', 0))
        request_body = environ['wsgi.input'].read(request_body_size)
        post_param = parse_qs(request_body)
        answer = answer + "post parameters = " + str(post_param) + "\n"
    except (ValueError):
        request_body_size = 0
    return iter( [ answer] )



