from django.db import models


class Tracker(models.Model):
    summary = models.CharField(max_length=100, null=False, blank=False, verbose_name='Summary')
    description = models.TextField(max_length=2500, null=True, blank=True, verbose_name='Description')
    status = models.ForeignKey('webapp.Status', related_name='tracker', on_delete=models.PROTECT, verbose_name='Status')
    type = models.ForeignKey('webapp.Type', related_name='tracker', on_delete=models.PROTECT, verbose_name='Type')
    project_id = models.ForeignKey('webapp.Project', related_name='tracker', on_delete=models.PROTECT, verbose_name='Project', blank=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Added time')

    def __str__(self):
        return self.summary

class Status(models.Model):
    status = models.CharField(max_length=30, null=False, blank=False, verbose_name='Status')

    def __str__(self):
        return self.status


class Type(models.Model):
    type = models.CharField(max_length=30, null=False, blank=False, verbose_name='Type')

    def __str__(self):
        return self.type


class Project(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name='Title')
    description = models.TextField(max_length=2500, null=True, blank=True, verbose_name='Description')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')

    def __str__(self):
        return self.title