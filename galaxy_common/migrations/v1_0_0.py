from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
