from django.shortcuts import render, render_to_response
from myfriend.models import Friend

# Create your views here.

def main(request):
    return render_to_response('main.html')
    
def friend(request):
    return render_to_response('friend.html',{'friends':Friend.objects.all()})