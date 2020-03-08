from django.conf import settings
from django.db import models


# Create your models here.
class NhomUser(models.Model):
    auth_user = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING)
    nhom = models.ForeignKey('Nhom', on_delete=models.DO_NOTHING)
    dinh_muc = models.IntegerField(null=True)
    is_leader = models.IntegerField(default=0)

    class Meta:
        # managed = False
        db_table = 'nhom_user'
        unique_together = (('auth_user', 'nhom'),)


class Nhom(models.Model):
    ten = models.CharField(max_length=50, default='Test')
    dinh_muc = models.IntegerField()
    is_deleted = models.IntegerField(default=0)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, through=NhomUser)

    def __str__(self):
        return self.ten

    class Meta:
        # managed = False
        db_table = 'nhom'


class ViNhom(models.Model):
    # id = models.IntegerField(primary_key=True)
    ten = models.CharField(max_length=45, blank=True, null=True)
    dinh_muc = models.IntegerField(blank=True, null=True)
    so_du = models.IntegerField(blank=True, null=True)
    auth_group = models.ForeignKey(Nhom, on_delete=models.CASCADE)

    def __str__(self):
        return self.ten

    class Meta:
        # managed = False
        db_table = 'vi_nhom'
