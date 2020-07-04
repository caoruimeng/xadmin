from django.db import models

# Create your models here.


class CleanSite(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'站点名', blank=True, null=True)
    desc = models.TextField(verbose_name='描述', blank=True, null=True)
    phone = models.CharField(verbose_name='联系方式',max_length=12, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=5, verbose_name='经度')
    dimension = models.DecimalField(max_digits=9, decimal_places=5, verbose_name='维度')

    class Meta:
        verbose_name = u'站点信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

