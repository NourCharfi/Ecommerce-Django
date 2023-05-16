from django.shortcuts import render

from django.contrib.auth.decorators import login_required


from django.shortcuts import render
from django.contrib.auth import logout

@login_required
def index(request):
    if request.user.is_authenticated:
        request.session['username'] = request.user.username
        logout(request)
    return render(request, 'index.html')
    
