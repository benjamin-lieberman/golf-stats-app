from django.db import models
from apps.reference.models import Club

class Round(models.Model):
 date=models.DateField()
 course_name=models.CharField(max_length=255)
 tee_name=models.CharField(max_length=100,blank=True)
 notes=models.TextField(blank=True)
 is_complete=models.BooleanField(default=False)

class HoleStat(models.Model):
 round=models.ForeignKey(Round,on_delete=models.CASCADE,related_name="holes")
 hole_number=models.IntegerField()
 par=models.IntegerField()
 distance_in_yards=models.IntegerField(default=0)
 gir_hit=models.BooleanField(default=False)

class Putt(models.Model):
 hole_stat=models.ForeignKey(HoleStat,on_delete=models.CASCADE,related_name="putts")
 putt_number=models.IntegerField()
 distance_ft=models.DecimalField(max_digits=6,decimal_places=1)
 made=models.BooleanField(default=False)
