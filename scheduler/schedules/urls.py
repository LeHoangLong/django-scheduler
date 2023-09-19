from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.TaskView.as_view(http_method_names=['get']))
]