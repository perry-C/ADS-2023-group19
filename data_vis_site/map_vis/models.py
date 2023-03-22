# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class MapVisRefugeedata(models.Model):
    # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    year = models.IntegerField(
        db_column='Year', blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    country_of_origin = models.TextField(
        db_column='Country of origin', blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    country_of_origin_iso = models.TextField(
        db_column='Country of origin (ISO)', blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    country_of_asylum = models.TextField(
        db_column='Country of asylum', blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    country_of_asylum_iso = models.TextField(
        db_column='Country of asylum (ISO)', blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    refugees_under_unhcr_s_mandate = models.IntegerField(
        db_column="Refugees under UNHCR's mandate", blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    asylum_seekers = models.IntegerField(
        db_column='Asylum-seekers', blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    other_people_in_need_of_international_protection = models.TextField(
        db_column='Other people in need of international protection', blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    stateless_persons = models.IntegerField(
        db_column='Stateless persons', blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    host_community = models.TextField(
        db_column='Host Community', blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    others_of_concern = models.IntegerField(
        db_column='Others of concern', blank=True, null=True)
    total_refugees = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'map_vis_refugeedata'
