from django.http import JsonResponse
def index(request):
    return JsonResponse({"Message":"Hello World"})