from django.contrib import admin
from django.urls import path

from core.views import index, contact

# Each URL pattern is defined using the path function and consists of three main components:
#    The URL pattern (a string representing the URL path)
#    The view or view function that handles the request
#    An optional name for the URL pattern (used for reverse URL resolution)
urlpatterns = [
    # path function is used to define URL patterns for routing HTTP requests 
    # to views or view functions.
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('admin/', admin.site.urls),
]
