from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .forms import NumbersForm

# Create your views here.
def index(request):
    result = None
    if request.method == 'POST':
        form = NumbersForm(request.POST)
        if form.is_valid():
            x = form.cleaned_data['num1']
            y = form.cleaned_data['num2']
            z = form.cleaned_data['num3']
            x1 = x
            x += y
            x2 = x
            x -= z
            x3 = x
            x *= y
            x4 = x
            x %= z
            x5 = x
            x /= z
            x6 = x
            sum = x + y + z
            result = [x1, y, z, x2, x3, x4, x5, x6, sum]
    else:
        form = NumbersForm()
    context = {
        'form': form,
        'result': result,
    }  
    return render(request, "app/index.html", context)