from django.db import models
from django.urls import reverse
from datetime import datetime

class ConsVals(models.Model):
    consultant_name = models.CharField(max_length=256, blank=True)
    def __str__(self):
        return self.consultant_name

class ReqVals(models.Model):
    requester_dept = models.CharField(max_length=256, blank=True)
    def __str__(self):
        return self.requester_dept

class StatVals(models.Model):
    status = models.CharField(max_length=256, blank=True)
    def __str__(self):
        return self.status
        
class SiteVals(models.Model):
    site_case = models.CharField(max_length=256, blank=True)
    def __str__(self):
        return self.site_case
        
class BuilVals(models.Model):
    building = models.CharField(max_length=256, blank=True)
    def __str__(self):
        return self.building
        
class ActVals(models.Model):
    action_taken = models.CharField(max_length=256, blank=True)
    def __str__(self):
        return self.action_taken
        
class StarVals(models.Model):
    star_site = models.CharField(max_length=256, blank=True)
    def __str__(self):
        return self.star_site
        
class SiteData(models.Model):
    
    #UserInput
    site_id = models.CharField(max_length=256)

    consultant_name = models.ForeignKey(ConsVals,on_delete=models.DO_NOTHING, default='')
    requester_dept = models.ForeignKey(ReqVals,on_delete=models.DO_NOTHING, default='')
    status = models.ForeignKey(StatVals,on_delete=models.DO_NOTHING, default='')
    site_case = models.ForeignKey(SiteVals,on_delete=models.DO_NOTHING, default='')
    building = models.ForeignKey(BuilVals,on_delete=models.DO_NOTHING, default='')
    action_taken = models.ForeignKey(ActVals,on_delete=models.DO_NOTHING, default='')
    star_site = models.ForeignKey(StarVals,on_delete=models.DO_NOTHING, default='')

    remarks = models.CharField(max_length=256, default='')
    mail_name = models.CharField(max_length=256, default='')
    project_name = models.CharField(max_length=256, default='')
    max_rating_in = models.CharField(max_length=256, default='')
    consultant_recommendations = models.CharField(max_length=256, default='')
    new_requirement = models.TextField(default='')
    request_date = models.DateField(default=datetime.today().strftime('%Y-%m-%d'))
    last_visit = models.DateField(default=datetime.today().strftime('%Y-%m-%d'))
    feedback = models.DateField(default=datetime.today().strftime('%Y-%m-%d'))
    max_rating_per = models.FloatField(max_length=256, default='0.1')
    updated_at = models.DateTimeField(auto_now=True)

    #Auto
    in_progress_date = models.CharField(max_length=256, blank=True)
    done_date = models.CharField(max_length=256, blank=True)
    email_address = models.CharField(max_length=256, default='')
    staff_id = models.CharField(max_length=256, default='')
    area = models.CharField(max_length=256, default='')
    rt_gf = models.CharField(max_length=256, default='')
    str_type = models.CharField(max_length=256, default='')
    height = models.CharField(max_length=256, default='')

    def get_absolute_url(self):
        return reverse('home')

    def __str__(self):
        return self.site_id



class SiteInfo(models.Model):
    site_id = models.CharField(max_length=256)
    email_address = models.CharField(max_length=256, default='')
    staff_id = models.CharField(max_length=256, default='')
    area = models.CharField(max_length=256, default='')
    rt_gf = models.CharField(max_length=256, default='')
    str_type = models.CharField(max_length=256, default='')
    height = models.CharField(max_length=256, default='')

    def __str__(self):
        return self.site_id
