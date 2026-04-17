from django.shortcuts import render, redirect
from .forms import SearchForm

def search(request):
    if request.method == "POST":
        form = SearchForm(request.POST, request.FILES)  # ✅ important
        if form.is_valid():
            form.save()
            return redirect('search')  # ✅ prevents resubmission
    else:
        form = SearchForm()  # ✅ correct way

    return render(request, 'search.html', {'form': form})
