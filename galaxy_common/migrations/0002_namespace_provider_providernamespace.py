# Generated by Django 2.2.2 on 2019-06-27 18:39

from django.db import migrations, models
import django.db.models.deletion
import galaxy_common.fields
import galaxy_common.models.mixins


class Migration(migrations.Migration):

    dependencies = [
        ('galaxy', '0001_auto_20190625_2129'),
    ]

    operations = [
        migrations.CreateModel(
            name='Namespace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('description', galaxy_common.fields.TruncatingCharField(blank=True, default='', max_length=255)),
                ('active', models.BooleanField(db_index=True, default=True)),
                ('name', models.CharField(db_index=True, max_length=512, unique=True)),
                ('avatar_url', models.CharField(blank=True, max_length=256, null=True, verbose_name='Avatar URL')),
                ('location', models.CharField(blank=True, max_length=256, null=True, verbose_name='Location')),
                ('company', models.CharField(blank=True, max_length=256, null=True, verbose_name='Company Name')),
                ('email', models.CharField(blank=True, max_length=256, null=True, verbose_name='Email Address')),
                ('html_url', models.CharField(blank=True, max_length=256, null=True, verbose_name='Web Site URL')),
                ('is_vendor', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('name',),
            },
            bases=(models.Model, galaxy_common.models.mixins.DirtyMixin),
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('description', galaxy_common.fields.TruncatingCharField(blank=True, default='', max_length=255)),
                ('active', models.BooleanField(db_index=True, default=True)),
                ('name', models.CharField(db_index=True, max_length=512, unique=True)),
                ('download_url', models.CharField(max_length=256, null=True)),
            ],
            options={
                'ordering': ('name',),
            },
            bases=(models.Model, galaxy_common.models.mixins.DirtyMixin),
        ),
        migrations.CreateModel(
            name='ProviderNamespace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('description', galaxy_common.fields.TruncatingCharField(blank=True, default='', max_length=255)),
                ('active', models.BooleanField(db_index=True, default=True)),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
                ('display_name', models.CharField(blank=True, editable=False, max_length=256, null=True, verbose_name='Display Name')),
                ('avatar_url', models.CharField(blank=True, max_length=256, null=True, verbose_name='Avatar URL')),
                ('location', models.CharField(blank=True, max_length=256, null=True, verbose_name='Location')),
                ('company', models.CharField(blank=True, max_length=256, null=True, verbose_name='Company Name')),
                ('email', models.CharField(blank=True, max_length=256, null=True, verbose_name='Email Address')),
                ('html_url', models.CharField(blank=True, max_length=256, null=True, verbose_name='Web Site URL')),
                ('followers', models.IntegerField(null=True, verbose_name='Followers')),
                ('namespace', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='provider_namespaces', to='galaxy.Namespace', verbose_name='Namespace')),
                ('provider', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='provider_namespaces', to='galaxy.Provider', verbose_name='Provider')),
            ],
            options={
                'ordering': ('provider', 'name'),
                'unique_together': {('namespace', 'provider', 'name'), ('provider', 'name')},
            },
            bases=(models.Model, galaxy_common.models.mixins.DirtyMixin),
        ),
    ]