from django.shortcuts import render, get_object_or_404
from .models import Drawing

def drawing_list(request):
    drawings = Drawing.objects.all().order_by('-pinned', '-created_at')
    return render(request, 'drawings/drawing_list.html', {'drawings': drawings})

def drawing_detail(request, pk):
    drawing = get_object_or_404(Drawing, pk=pk)
    return render(request, 'drawings/drawing_detail.html', {'drawing': drawing})
