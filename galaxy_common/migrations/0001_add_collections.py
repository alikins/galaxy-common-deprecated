# Generated by Django 2.2.2 on 2019-06-25 21:29

import django.contrib.postgres.fields.jsonb
import django.contrib.postgres.indexes
import django.contrib.postgres.search
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import galaxy_common.fields
import galaxy_common.models.mixins


class Migration(migrations.Migration):

    dependencies = [
        ('galaxy', 'v1_0_0'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('namespace',
                 models.CharField(db_index=True, max_length=512, unique=True)),
                ('name', models.CharField(max_length=64)),
                ('deprecated', models.BooleanField(default=False)),
                ('download_count', models.IntegerField(default=0)),
                ('community_score', models.FloatField(null=True)),
                ('community_survey_count', models.IntegerField(default=0)),
                ('search_vector',
                 django.contrib.postgres.search.SearchVectorField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id',
                 models.AutoField(auto_created=True,
                                  primary_key=True,
                                  serialize=False,
                                  verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('description',
                 galaxy_common.fields.TruncatingCharField(blank=True,
                                                          default='',
                                                          max_length=255)),
                ('active', models.BooleanField(db_index=True, default=True)),
                ('name',
                 models.CharField(db_index=True, max_length=512, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Tags',
                'ordering': ['name'],
            },
            bases=(models.Model, galaxy_common.models.mixins.DirtyMixin),
        ),
        migrations.CreateModel(
            name='CollectionVersion',
            fields=[
                ('id',
                 models.AutoField(auto_created=True,
                                  primary_key=True,
                                  serialize=False,
                                  verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('version', models.CharField(max_length=64)),
                ('hidden', models.BooleanField(default=False)),
                ('metadata',
                 django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                ('contents',
                 django.contrib.postgres.fields.jsonb.JSONField(default=list)),
                ('quality_score',
                 models.FloatField(null=True,
                                   validators=[
                                       django.core.validators.MinValueValidator(0.0),
                                       django.core.validators.MaxValueValidator(5.0)])),
                ('readme_mimetype',
                 models.CharField(blank=True, max_length=32)),
                ('readme_text', models.TextField(blank=True)),
                ('readme_html', models.TextField(blank=True)),
                ('collection',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   related_name='versions',
                                   to='galaxy.Collection')),
            ],
            options={
                'unique_together': {('collection', 'version')},
            },
        ),
        migrations.AddField(
            model_name='collection',
            name='latest_version',
            field=models.ForeignKey(null=True,
                                    on_delete=django.db.models.deletion.SET_NULL,
                                    related_name='+',
                                    to='galaxy.CollectionVersion'),
        ),
        migrations.AddField(
            model_name='collection',
            name='tags',
            field=models.ManyToManyField(to='galaxy.Tag'),
        ),
        migrations.AddIndex(
            model_name='collection',
            index=django.contrib.postgres.indexes.GinIndex(
                fields=['search_vector'],
                name='galaxy_coll_search__a27ecf_gin'),
        ),
        migrations.AlterUniqueTogether(
            name='collection',
            unique_together={('namespace', 'name')},
        ),
    ]