from django.urls import path
from . import views

urlpatterns = [
    path('', views.UploadView.as_view(), name='upload'),
    path('files/<int:file_id>', views.detail, name='detail')
]