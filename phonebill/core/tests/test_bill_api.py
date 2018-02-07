import json

import pytest


@pytest.fixture
def expected_output():
    return {
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


@pytest.mark.parametrize(
    'phone', ['122345678', '1298765432'])
def test_bill_get(client, phone, expected_output):
    data = {'subscriber_phone': phone, 'reference_period': '12/2017'}
    response = client.get('/api/phone-bill', data)
    unparsed_data = json.loads(response.content, encoding='utf8')
    expected_output['subscriber'] = phone
    assert expected_output == unparsed_data
