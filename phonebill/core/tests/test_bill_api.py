import json

EXPECTED_BILL_API_OUTPUT = {
    'subscriber': '122345678',
    'month': 12,
    'year': 2017,
    'records': [
        {
            'destination': '128765432',
            'start_date': '01/12/2017',
            'start_time': '22:00:00',
            'duration': '7h59m59s',
            'price': 'R$ 0,36'
        }
    ]
}


def test_bill_get(client):
    data = {'subscriber_phone': '122345678', 'reference_period': '12/2017'}
    response = client.get('/api/phone-bill', data)
    unparsed_data = json.loads(response.content, encoding='utf8')
    assert EXPECTED_BILL_API_OUTPUT == unparsed_data
