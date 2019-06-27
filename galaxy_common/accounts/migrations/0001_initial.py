# Generated by Django 2.2.2 on 2019-06-27 20:55

import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.utils.timezone
import galaxy_common.models.mixins
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(help_text='Required. 30 characters or fewer. Letters, numbers and @/./+/-/_ characters', max_length=30, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[a-zA-Z0-9_.@+-]+$'), 'Enter a valid username.', 'invalid')], verbose_name='username')),
                ('full_name', models.CharField(blank=True, max_length=254, verbose_name='full name')),
                ('short_name', models.CharField(blank=True, max_length=30, verbose_name='short name')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(db_index=True, default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('avatar_url', models.CharField(blank=True, max_length=256, verbose_name='avatar URL')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=(models.Model, galaxy_common.models.mixins.DirtyMixin),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
