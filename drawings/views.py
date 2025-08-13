from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Drawing


def drawing_list(request):
    drawings_qs = Drawing.objects.all().order_by('-pinned', '-created_at')
    paginator = Paginator(drawings_qs, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    total_pages = paginator.num_pages
    current = page_obj.number

    def make_window(total, current, radius=1):
        start = max(1, current - radius)
        end = min(total, current + radius)
        return list(range(start, end + 1))

    context = {
        'drawings': page_obj,
        'total_pages': total_pages,
        'current': current,
        'page_window': make_window(total_pages, current),
    }

    return render(request, 'drawings/drawing_list.html', context)


def drawing_detail(request, pk):
    drawing = get_object_or_404(Drawing, pk=pk)
    return render(request, 'drawings/drawing_detail.html', {'drawing': drawing})

def server_error(request):
    return render(request, "500.html", status=503)
