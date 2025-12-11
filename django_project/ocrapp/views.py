from django.shortcuts import render
from .serializers import UploadInfoTbSerizalizer,UploadInfoTbSerizalizer_List
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework import generics
from .models import UploadInfoTb




class UploadFile(APIView):
    def post(self,request,*args,**kwargs):

        serizalizer = UploadInfoTbSerizalizer(data = request.data)
        
        if serizalizer.is_valid():
                extra_data = {
                    #  'user_id':1,
                    'file_name':serizalizer.validated_data['file_path'].name,
                    'file_size':serizalizer.validated_data['file_path'].size,
                    'mime_type':serizalizer.validated_data['file_path'].content_type,
                    'extension':serizalizer.validated_data['file_path'].name.split('.')[-1]
                }
                
                # 这里有一些需要自动化的操作
                '''
                id 数据库自动递增
                user_id 根据请求来源,拿到request.user 的信息存入
                file_name file_size mime_type extension  由请求方完成提供，我这边获取request.data['file']这个对象，对这个对象取名字
                file_path 请求放方，存入request.data['file']？
                upload_time 数据库自动存入
                status is_deleted 数据层自动写
                hash 业务层计算，并且需要在save之前比对一下？
                storage_provider 默认值，读管理员设置的库

                '''
                print(type(serizalizer.validated_data['file_path']))
                instance = serizalizer.save(**extra_data)
        else:
             print(serizalizer.errors)
            # print(type(request.user.username))

        return Response('success')


class UploadFileList(generics.ListAPIView):
     queryset = UploadInfoTb.objects.all()
     serializer_class = UploadInfoTbSerizalizer_List


class CreateTask(APIView):
     def post(self,request,*args,**kwargs):
          """
          接受请求，请求参数入到task里，task发起请求。
          """
          


          return Response('success')

     