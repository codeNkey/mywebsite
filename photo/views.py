from django.shortcuts import render
from .

# Create your views here.
def photo_list(request):
  return render(request, 'photo/photo_list.html', {'photos': photos})