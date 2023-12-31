# Generated by Django 4.2.1 on 2023-08-20 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tennisApp', '0003_rename_fp_img_firstsection_fo_img_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thirdsection',
            name='four',
        ),
        migrations.RemoveField(
            model_name='thirdsection',
            name='three',
        ),
        migrations.RemoveField(
            model_name='thirdsection',
            name='two',
        ),
        migrations.AddField(
            model_name='fourthsection',
            name='fo_img',
            field=models.ImageField(blank=True, null=True, upload_to='photos'),
        ),
        migrations.AddField(
            model_name='fourthsection',
            name='four',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='fourthsection',
            name='three',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
