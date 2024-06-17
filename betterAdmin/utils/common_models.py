from django.db import models


class NewModel(models.Model):

    created_by = models.CharField(max_length=32, blank=False, null=False, verbose_name='Created By')
    updated_by = models.CharField(max_length=32, blank=False, null=False, verbose_name='Updated By')
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='Created At')
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name='Updated At')
    is_deleted = models.BooleanField(default=False, blank=False, null=False, verbose_name='Is Deleted')

    class Meta:
        abstract = True
