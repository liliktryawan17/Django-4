from django.shortcuts import render


def home(request):
    context = {
        'title': 'Beranda',
        'subtitle': 'Selamat datang',
        'nav': [
            ['/', 'Home'],
            ['/myblog', 'Blog'],
            ['/mycontent', 'Konten'],
            ['/mycontent/new', 'Konten Terbaru'],
            ['/mycontent/popular', 'Konten Populer']
        ]
    }
    return render(request, 'index.html', context)
