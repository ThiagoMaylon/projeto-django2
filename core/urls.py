from django.urls import path
from .views import index, contato, produto

urlpatterns = [
    path('', index, name='index'),
    path('produto/', produto, name='produto'),
    path('contato/', contato, name='contato')
]
