from django.conf import settings
from django.db import models
from qlct_nhom.models import ViNhom
from qlct_ca_nhan.models import LinhVuc, ViCaNhan


# Create your models here.
class HoaDon(models.Model):
    # id = models.IntegerField(primary_key=True)
    ten_hoa_don = models.CharField(max_length=45, blank=True, null=True)
    so_tien = models.IntegerField(blank=True, null=True)
    ghi_chu = models.CharField(max_length=500, blank=True, null=True)
    thoi_gian_giao_dich = models.DateTimeField(blank=True, null=True)
    vi_nhom = models.ForeignKey(ViNhom, models.DO_NOTHING, blank=True, null=True)
    linh_vuc = models.ForeignKey(LinhVuc, models.DO_NOTHING)
    vi_ca_nhan = models.ForeignKey(ViCaNhan, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.ten_hoa_don

    class Meta:
        # managed = False
        db_table = 'hoa_don'
