from rest_framework import serializers
from .models import UploadInfoTb

class UploadInfoTbSerizalizer(serializers.ModelSerializer):
    class Meta:
        model = UploadInfoTb
        fields = [
            'user_id',
            # 'file_name',
            'file_path',
            # 'file_size',
            # 'mime_type',
            # 'extension',
        ]

class UploadInfoTbSerizalizer_List(serializers.ModelSerializer):
    class Meta:
        model = UploadInfoTb
        fields = '__all__'