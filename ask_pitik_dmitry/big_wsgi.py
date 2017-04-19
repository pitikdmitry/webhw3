import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ask_pupkin.settings")


def append_body_answer(output_message):
    output_message.append(b'<html lang="en">'
                          b'<head><meta charset="UTF-8"><title>Title</title></head>'
                          b'<body>'
                          b'<h4>GET</h4>'
                          b'<form method="GET">'
                          b'<input type="text" size="20" name="get_space" value="">'
                          b'<input type="submit" value="Send">'
                          b'</form>'
                          b'<h4>POST</h4>'
                          b'<form method="POST">'
                          b'<input type="text" size="20" name="post_space" value="">'
                          b'<input type="submit" value="Send">'
                          b'</form>')


def append_end_body_answer(output_message):
    output_message.append(b'</body>'
                          b'</html>')


def append_answer(output_message, method, query, answer):
    output_message.append(b'<h4>METHOD:</h4>')
    output_message.append(method)
    output_message.append(b'<h4>QUERY STRING:</h4>')
    output_message.append(query)
    output_message.append(b'<h4>Answer:</h4>')
    output_message.append(answer)


def simple_app(environ, start_response):
    """Simplest possible application object"""
    status = '200 OK'
    print("============================================================")
    for a in environ:
        print(a, environ[a])

    output_message = [b'<!DOCTYPE html>']
    append_body_answer(output_message)

    if environ['REQUEST_METHOD'] == 'POST':
        query_string = environ['QUERY_STRING']
        print("query_string = ", query_string)

        body_post = environ['wsgi.input']
        body_byte_post = body_post.read()
        print("body_byte_post = ", body_byte_post)

        if body_byte_post != b'':
            append_answer(output_message, b'POST', body_byte_post, body_byte_post)
        else:
            append_answer(output_message, b'POST', b'Empty input',  b'Empty answer')

    if environ['REQUEST_METHOD'] == 'GET':
        query_string = environ['QUERY_STRING']
        print("query_string = ", query_string)

        body_get = environ['wsgi.input']
        body_byte_get = body_get.read()
        print('body_byte: ', body_byte_get)

        if query_string != '':
            append_answer(output_message, b'GET', bytes(query_string.encode()), b'Hello, my friend!!!')
        else:
            append_answer(output_message, b'GET', b'Empty query', b'Hello, my friend!!!')

    append_end_body_answer(output_message)

    response_headers = [('Content-type', 'text/html')]
    start_response(status, response_headers)

    return output_message


def say_hello(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    hello = b'Hello world!'
	return [hello]
