from django.shortcuts import render

# Create your views here.

def profile(request):
    """ A view to return the profile page. """
    return render(request, 'profiles/profiles.html')