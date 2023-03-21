# Generated by Django 3.2.18 on 2023-03-21 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('map_vis', '0004_delete_refugeedata'),
    ]

    operations = [
        migrations.CreateModel(
            name='MapVisRefugeedata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_field', models.IntegerField(blank=True, db_column='Year                                                                                                                                              ', null=True)),
                ('country_of_origin_field', models.TextField(blank=True, db_column='Country of origin                                           ', null=True)),
                ('country_of_origin_iso_field', models.TextField(blank=True, db_column='Country of origin (ISO) ', null=True)),
                ('country_of_asylum_field', models.TextField(blank=True, db_column='Country of asylum                                    ', null=True)),
                ('country_of_asylum_iso_field', models.TextField(blank=True, db_column='Country of asylum (ISO) ', null=True)),
                ('refugees_under_unhcr_s_mandate_field', models.IntegerField(blank=True, db_column="Refugees under UNHCR's mandate ", null=True)),
                ('asylum_seekers_field', models.IntegerField(blank=True, db_column='Asylum-seekers ', null=True)),
                ('other_people_in_need_of_international_protection_field', models.TextField(blank=True, db_column='Other people in need of international protection ', null=True)),
                ('stateless_persons_field', models.IntegerField(blank=True, db_column='Stateless persons ', null=True)),
                ('host_community_field', models.TextField(blank=True, db_column='Host Community ', null=True)),
                ('others_of_concern', models.IntegerField(blank=True, db_column='Others of concern', null=True)),
                ('total_refugees', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'map_vis_refugeedata',
                'managed': False,
            },
        ),
    ]
