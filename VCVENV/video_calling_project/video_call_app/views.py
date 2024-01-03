from django.shortcuts import render


from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def video_call(request):
    return render(request, 'video_call.html')

