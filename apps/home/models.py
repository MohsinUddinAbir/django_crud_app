from django.db import models

class Population(models.Model):
   slug = models.SlugField(max_length=200, db_index=True)
   country = models.CharField(max_length=200)
   population = models.IntegerField()
   yearly_change = models.FloatField()
   net_change = models.IntegerField()
   density = models.IntegerField()
   land_area = models.IntegerField()
   migrants = models.IntegerField()
   fert_rate = models.FloatField()
   med_age = models.IntegerField()
   urban_pop = models.IntegerField()
   world_share = models.FloatField()
   class Meta:
      ordering = ['country']

   def __str__(self):
        return self.country