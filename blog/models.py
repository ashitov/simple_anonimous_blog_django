from django.db import models


class Note(models.Model):
    id = models.IntegerField(primary_key=True, null=False)
    text = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'note'
