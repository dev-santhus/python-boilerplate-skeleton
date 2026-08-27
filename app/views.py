from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello from ${{ values.name }}", content_type="text/plain")
