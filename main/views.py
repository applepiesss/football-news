from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406495584',
        'name': 'Nadia Aisyah Fazila',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)