from django.urls import path

from recipes.views import contato, home, sobre

# dominio/recipes/
urlpatterns = [
    path('', home),  # home
    path('sobre/', sobre),  # /contato/
    path('contato/', contato),  # /sobre/

]
