from django.db import models


class Quakes(models.Model):
    a = models.DecimalField(max_digits=7, decimal_places=5)
    dd = models.TextField(db_column='dD', blank=True, null=True)  # Field name made lowercase.
    dl = models.TextField(db_column='dL', blank=True, null=True)  # Field name made lowercase.
    dr = models.TextField(db_column='dR', blank=True, null=True)  # Field name made lowercase.
    dep = models.TextField(blank=True, null=True)
    lat = models.TextField(blank=True, null=True)
    lon = models.TextField(blank=True, null=True)
    q = models.TextField(blank=True, null=True)
    s = models.DecimalField(max_digits=3, decimal_places=1)
    t = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quakes'
