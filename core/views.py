from django.shortcuts import render

# The request parameter represents an HTTP request object sent by the client to the server.
# It contains information about the request, such as HTTP headers, query parameters, and 
# POST data.
def index(request):
    return render(request, 'core/index.html')

def contact(request):
    return render(request, 'core/contact.html')