from django.shortcuts import render
from .forms import JobForm
from .utils import final_prediction

def home(request):
    result = None
    flags = []

    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['description']
            result, flags = final_prediction(text)
    else:
        form = JobForm()

    return render(request, 'detector/index.html', {
        'form': form,
        'result': result,
        'flags': flags
    })