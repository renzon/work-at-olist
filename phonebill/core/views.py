from django.http import JsonResponse


def bill(request):
    reference_period = request.GET['reference_period']
    content = {
        'subscriber': request.GET['subscriber_phone'],
        'reference_period': reference_period,
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

    return JsonResponse(content)
