from django.conf import settings
from django.db import models
from django.utils import timezone


# Create your models here.
class SoNo(models.Model):
    # id = models.IntegerField(primary_key=True)
    ten_so_no = models.CharField(max_length=200, blank=True, null=True)
    so_tien = models.IntegerField(blank=True, null=True)
    doi_tac = models.CharField(max_length=200, blank=True, null=True)
    loai = models.IntegerField(blank=True, null=True)
    ngay_vay = models.DateTimeField(blank=True, null=True)
    ngay_tra = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField(default=0)
    auth_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sono')

    def __str__(self):
        return self.ten_so_no

    def is_due_date(self):
        if self.ngay_tra == timezone.now():
            return True
        else:
            return False

    class Meta:
        # managed = False
        db_table = 'so_no'