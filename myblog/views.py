from django.shortcuts import render


def blog(request):
    context = {
        'title': 'Blog',
        'subtitle': 'Selamat datang',
        'nav': [
            ['/', 'Home'],
            ['/myblog', 'Blog'],
            ['/mycontent', 'Konten']
        ]
    }
    return render(request, 'myblog/index.html', context)
