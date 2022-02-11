from django.contrib.gis.db import models
from django.contrib.gis.db import models as geomodels
from jsonfield import JSONField

# Create your models here.


class prove_geognostiche(models.Model):
    tipo_prova = models.CharField(max_length=254, blank=True, null=True)
    committente = models.CharField(max_length=254, blank=True, null=True)
    luogo = models.CharField(max_length=254, blank=True, null=True)
    indirizzo = models.CharField(max_length=254, blank=True, null=True)
    nome_prova = models.CharField(max_length=254, blank=True, null=True)
    stato = models.CharField(max_length=255, blank=True, null=True)
    geom = geomodels.PointField()
    input_data = JSONField()
    output_data = JSONField()
    ipl_rw = models.FloatField(blank=True, null=True)
    ipl_ib = models.FloatField(blank=True, null=True)
    stratigraphy_data = JSONField()
    commessa = models.CharField(max_length=255, blank=True, null=True)

    @property
    def lat_lng_gt(self):
        return list(getattr(self.geom, 'coords', [])[::-1])

    def get_json_data(self):
        return json.dumps(self.input_data)

    class Meta:
        verbose_name_plural = 'prove_geognostiche'