from django.shortcuts import render


def profile(request):
    context = {
        'fullName': 'Andreas Amundsen',
        'username': 'testomundsen',
        'email': 'roids@biceps.com',

    }

    return render(request, 'profile_page/profile_view.html', context)
