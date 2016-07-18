import requests

import config

CHART_REQUEST_URL = "https://charturl.com/short-urls.json?api_key=%s"


def make_chart(_):
    """
        Calls a remote service to make a chart.

        @param data: TODO
        @type data: TODO
    """
    API_KEY = config.get_credentials().get('charturl', 'api_key')

    request_data = {
        'template': 'assertion-count-timeseries',
        'options': {
            'data': {
                'columns': [
                    ["x",
                     "2013-01-01",
                     "2013-01-02",
                     "2013-01-03",
                     "2013-01-04",
                     "2013-01-05",
                     "2013-01-06"],
                    ['data1', 1, 2, 3, 4],
                    ['data2', 5, 6, 7, 8],
                ]
            }
        }
    }

    request_url = CHART_REQUEST_URL % API_KEY
    print 'making call to %s with %s' % (request_url, request_data)
    res = requests.post(request_url, json=request_data)
    if not res.ok:
        print 'request failed'
        print res.content

    chart_url = res.json()['short_url']
    print 'chart_url: ', chart_url


if __name__ == '__main__':
    make_chart(None)

