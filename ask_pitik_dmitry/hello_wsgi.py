def simple_app(environ, start_response):
    """Simplest possible application object"""
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return ['Hello world!\n']



def app(environ, start_response):
    start_response('200 OK', [('Content-type', 'text/html')])
    sorted_keys = environ.keys()
    sorted_keys.sort()
    result = ['<li> %s => %s</li>' % (str(k), str(environ[k])) for k in sorted_keys]
    return result