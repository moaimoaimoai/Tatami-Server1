# Generated by Django 3.0.7 on 2023-05-22 07:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_monopost_repostingfromuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageAttribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attributeName', models.CharField(max_length=50)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('userCreate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userAttribute', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserIntAttribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('intAttributeId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='intAttributeId', to='api.PageAttribute')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='useIntAttributeId', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]