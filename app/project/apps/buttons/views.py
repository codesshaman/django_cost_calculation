from django.shortcuts import render

# Create your views here.
def test(request):
    template = 'pages/index.html'
    context = {
        'title': 'Расчёт доходности'
    }
    return render(request, template, context)