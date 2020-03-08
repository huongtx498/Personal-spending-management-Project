from django.conf import settings
from django.db import models


# Create your models here.
class ViCaNhan(models.Model):
    # id = models.IntegerField(primary_key=True)
    ten = models.CharField(max_length=45, blank=True, null=True)
    dinh_muc = models.IntegerField(blank=True, null=True)
    so_du = models.IntegerField(blank=True, null=True)
    auth_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_deleted = models.IntegerField(default=0)
    # 0 - chưa xóa, 1 - đã xóa

    def __str__(self):
        return self.ten

    class Meta:
        # managed = False
        db_table = 'vi_ca_nhan'


class LinhVuc(models.Model):
    # id = models.IntegerField(primary_key=True)
    ten = models.CharField(max_length=45, blank=True, null=True)
    loai = models.IntegerField(blank=True, null=True) # 1 là tiêu 0 là thu
    linh_vuc = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    auth_user = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.ten

    class Meta:
        # managed = False
        db_table = 'linh_vuc'


# class AuthUserHasLinhVuc(models.Model):
#     auth_user = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, primary_key=True)
#     linh_vuc = models.ForeignKey('LinhVuc', models.DO_NOTHING)
#
#     class Meta:
#         # managed = False
#         db_table = 'auth_user_has_linh_vuc'
#         unique_together = (('auth_user', 'linh_vuc'),)
