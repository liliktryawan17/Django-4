from django.shortcuts import render


def konten(request):
    context = {
        'title': 'Konten',
        'subtitle': 'Selamat datang',
        'nav': [
            ['/', 'Home'],
            ['/myblog', 'Blog'],
            ['/mycontent', 'Konten'],
            ['/mycontent/new', 'Konten Terbaru'],
            ['/mycontent/popular', 'Konten Populer']
        ]
    }
    return render(request, 'mycontent/index.html', context)


def new(request):
    context = {
        'title': 'Konten Terbaru',
        'subtitle': 'Selamat datang',
        'nav': [
            ['/', 'Home'],
            ['/mycontent', 'Konten'],
            ['/mycontent/new', 'Konten Terbaru'],
            ['/mycontent/popular', 'Konten Populer']
        ]
    }
    return render(request, 'mycontent/index.html', context)


def popular(request):
    context = {
        'title': 'Konten Terpopuler',
        'subtitle': 'Selamat datang',
        'nav': [
            ['/', 'Home'],
            ['/mycontent', 'Konten'],
            ['/mycontent/new', 'Konten Terbaru'],
            ['/mycontent/popular', 'Konten Populer']
        ]
    }
    return render(request, 'mycontent/populer.html', context)
