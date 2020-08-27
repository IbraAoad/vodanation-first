from django.db import models

# Create your models here.

class general_info(models.Model):

    Alex = "Alex"

    Cairo = "Cairo"

    Delta = "Delta"

    Giza = "Giza"

    Upper = "Upper"

    region_choice = [(Alex,"Alex"),(Cairo,"Cairo"),(Delta,"Delta"),(Giza,"Giza"),(Upper,"Upper")]

 

    site_id=models.CharField(blank=False, max_length=30)

    option=models.CharField(blank=False, max_length=1)

    region=models.CharField(max_length=30,

                            choices=region_choice,

                            blank=False, null=True)

    sub_region=models.CharField(blank=False, max_length=30)

    longitude=models.FloatField(null=True, blank=True, default=None)

    latitude=models.FloatField(null=True, blank=True, default=None)

    site_type=models.CharField(blank=False, max_length=30)

    structure_type=models.CharField(blank=False, max_length=30)

    cluster_avg=models.FloatField(null=True, blank=True, default=None)

 

    def __str__(self):

        return self.site_id