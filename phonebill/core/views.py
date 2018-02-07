from django.http import JsonResponse


def bill(request):
    content = {
        'subscriber': request.GET['subscriber_phone'],
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

    return JsonResponse(content)
