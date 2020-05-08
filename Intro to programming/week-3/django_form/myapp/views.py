from django.shortcuts import render
from django.http import HttpResponse
from .form import Form

# Create your views here.

def form(request):

    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            company_name = form.cleaned_data['company_name']
            fiber_cost = form.cleaned_data['fiber_cost']

            if fiber_cost >= 100 and fiber_cost < 249:
                totalCost = fiber_cost * .80
            elif fiber_cost >= 250 and fiber_cost < 499:
                totalCost = fiber_cost * .70
            elif fiber_cost >= 500:
                totalCost = fiber_cost * .50
            elif fiber_cost < 100:
                totalCost = fiber_cost * .87

            print('Hello ' + company_name + ', ' + 'the total cost of your fiber order is ' + str(totalCost))

    form = Form()
    return render(request, 'form.html', { 'form': form })
