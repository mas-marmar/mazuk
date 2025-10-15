from django.shortcuts import HttpResponse

# https://example.org/sum?a=5&b=7
# http://127.0.0.1:8000/sum

def sum_view(request):
    first_compoud = float (request.GET.get('a', 0))
    second_compoud = float (request.GET.get('b', 0))
    result = first_compoud + second_compoud

    return HttpResponse(str(result))

def substract_view(request):
    first_substract = float (request.GET.get('a', 0))
    second_substract = float (request.GET.get('b', 0))
    result = second_substract - first_substract
    return HttpResponse(str(result))

def divide_view(request):
    first_divide = float (request.GET.get('a', 0))
    second_divide = float (request.GET.get('b', 0))
    result = second_divide / first_divide
    return HttpResponse(str(result))
