# Generated by Django 2.0.2 on 2018-06-22 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='t_blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_id', models.IntegerField()),
                ('title', models.CharField(max_length=256)),
                ('subtitle', models.CharField(max_length=256)),
                ('body', models.CharField(max_length=1024)),
                ('ups_date', models.DateTimeField()),
                ('ins_date', models.DateTimeField()),
                ('d_flg', models.BooleanField()),
            ],
        ),
    ]