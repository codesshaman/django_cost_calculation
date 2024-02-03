from django.shortcuts import render


# Create your views here.
def home(request):
    template = 'pages/index.html'
    context = {
        'title': 'Расчёт доходности'
    }
    return render(request, template, context)


def rules(request):
    template = 'pages/rules.html'
    context = {
        'title': 'Правила'
    }
    return render(request, template, context)


def loss(request):
    template = 'pages/loss.html'
    context = {
        'title': 'Скидки и потери'
    }
    return render(request, template, context)
