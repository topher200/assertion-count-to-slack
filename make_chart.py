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
            'columns': [
                [1,2,3,4],
                [5,6,7,8],
            ]
        }
    }
    res = requests.post(CHART_REQUEST_URL % API_KEY, request_data)
    print res

