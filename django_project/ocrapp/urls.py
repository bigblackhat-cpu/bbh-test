from django.urls import path
from .views import UploadFile,UploadFileList,CreateTask

urlpatterns =[
    path('upload_file/',UploadFile.as_view(),name='upload_file'),
    path('upload_file/list/',UploadFileList.as_view(),name='upload_file_list'),
    path('send_task/',CreateTask.as_view(),name='send_task')
]