# Generated by Django 4.0 on 2022-03-28 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_post_mazmuni'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Post', 'verbose_name_plural': 'Postlar'},
        ),
        migrations.RemoveField(
            model_name='post',
            name='mazmuni',
        ),
        migrations.AddField(
            model_name='post',
            name='daromadi',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
