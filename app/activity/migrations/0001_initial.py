# Generated by Django 2.2.7 on 2019-12-22 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_name', models.CharField(max_length=300)),
                ('category', models.CharField(choices=[('health', 'health'), ('general', 'general'), ('sales', 'sales'), ('project', 'project'), ('social', 'social'), ('retirement', 'retirement'), ('fulfillment', 'fulfillment'), ('other', 'other')], default=('general', 'general'), max_length=300)),
                ('priority', models.CharField(choices=[('low', 'low'), ('moderate', 'moderate'), ('high', 'high')], default=('low', 'low'), max_length=300)),
            ],
            options={
                'verbose_name_plural': 'activities',
            },
        ),
    ]
