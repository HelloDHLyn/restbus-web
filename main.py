from tinyweb.tinyweb import Route, start

routes = [
    Route('/', 'index.html'),
    Route('/stations', 'stations.html', ctx_path='https://apis.lynlab.co.kr/v1/bus/stations'),
    Route('/arrivals', 'arrivals.html', ctx_path='https://apis.lynlab.co.kr/v1/bus/arrivals')
]

if __name__ == '__main__':
    start(__name__, routes=routes, host='0.0.0.0')
