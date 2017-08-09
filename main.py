from tinyweb.tinyweb import Route, start

routes = [
    Route('/', 'index.html')
]

if __name__ == '__main__':
    start(__name__, routes=routes, host='0.0.0.0')
