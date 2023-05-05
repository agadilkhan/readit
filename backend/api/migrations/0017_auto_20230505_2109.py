# Generated by Django 3.2.18 on 2023-05-05 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_auto_20230505_2102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookimage',
            name='image_url',
        ),
        migrations.AddField(
            model_name='bookimage',
            name='image_path',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bookimage',
            name='image',
            field=models.ImageField(upload_to='books'),
        ),
    ]