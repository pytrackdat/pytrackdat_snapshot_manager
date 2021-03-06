# Generated by Django 2.2.9 on 2020-02-02 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Snapshot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdt_created_at', models.DateTimeField(auto_now_add=True)),
                ('pdt_modified_at', models.DateTimeField(auto_now=True)),
                ('snapshot_type', models.TextField(choices=[('auto', 'Automatic'), ('manual', 'Manual')], default='manual', help_text='Created by whom?', max_length=6)),
                ('name', models.TextField(help_text='Name of snapshot file', max_length=127)),
                ('reason', models.TextField(blank=True, default='Manually created', help_text='Reason for snapshot creation', max_length=127)),
                ('size', models.IntegerField(help_text='Size of database (in bytes)')),
            ],
        ),
    ]
