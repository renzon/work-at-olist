import json

import pytest


@pytest.fixture
def expected_output():
    return {
        'subscriber': '122345678',
        'reference_period': '12/2017',
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


@pytest.mark.parametrize('phone', ['122345678', '1298765432'])
@pytest.mark.parametrize('year', [2017, 2016])
@pytest.mark.parametrize('month', list(range(1, 13)))
def test_bill_get(client, year, month, phone, expected_output):
    reference_period = f'{month}/{year}'
    data = {'subscriber_phone': phone, 'reference_period': reference_period}
    response = client.get('/api/phone-bill', data)
    unparsed_data = json.loads(response.content, encoding='utf8')
    expected_output['subscriber'] = phone
    expected_output['reference_period'] = reference_period
    assert expected_output == unparsed_data
