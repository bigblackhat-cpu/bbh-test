from django.db import models

# Create your models here.

class UploadInfoTb(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()        
    file_name = models.CharField(max_length=255)
    file_path = models.FileField(max_length=512,upload_to=r'uploads/%Y/%m/%d/')
    file_size = models.BigIntegerField()
    mime_type = models.CharField(max_length=100)
    extension = models.CharField(max_length=10)
    upload_time = models.DateTimeField(blank=True, null=True,auto_now_add=True)
    status = models.IntegerField(blank=True, null=True)
    is_deleted = models.IntegerField(blank=True, null=True)
    hash = models.CharField(max_length=64, blank=True, null=True)
    storage_provider = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'upload_info_tb'

        
