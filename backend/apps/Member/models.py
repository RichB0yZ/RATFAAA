from django.db import models
from django.utils.translation import gettext_lazy as _

class Status(models.TextChoices):
    AIRFORCE = 'AF', _('กองทัพอากาศ')
    MILLITARY = 'MT', _('กลาโหม')
    RETIRE = 'RT', _('เกษียณ')
    RESIGN = 'RS', _('ลาออก')
    DEATH = 'DT', _('เสียชีวิต')

class Member(models.Model):
    
    class_year = models.IntegerField(verbose_name = 'รุ่น', null=True, blank = True)
    title = models.CharField(verbose_name="คำนำหน้า", null=True, blank=True,max_length = 20)
    full_name = models.CharField(verbose_name = 'ชื่อ-นามสกุล', max_length = 150)
    position =  models.CharField(verbose_name="ตำแหน่ง", max_length = 100,null = True, blank=True)
    corps =  models.CharField(verbose_name="เหล่า", max_length = 50,null = True, blank=True)
    unit =  models.CharField(verbose_name="หน่วยงาน", max_length = 50,null = True, blank=True)
    mobile  = models.CharField(verbose_name = 'เบอร์มือถือ', max_length = 20)
    status = models.CharField(verbose_name = 'สถานะ',max_length = 5, choices = Status.choices, default = Status.AIRFORCE, null = True, blank = True)
    date_retire=models.DateField(verbose_name='วัน/เดือน/ปี ที่เกษียณ')
    
    def __str__(self):
        return f"{self.class_year} {self.title} {self.full_name}"

    class Meta:
        verbose_name_plural = "สมาชิก" 
        
class Event(models.Model):
    
    members=models.ManyToManyField(Member)

