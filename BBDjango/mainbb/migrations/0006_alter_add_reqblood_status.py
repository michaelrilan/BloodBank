# Generated by Django 3.2.8 on 2021-12-09 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainbb', '0005_auto_20211209_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_reqblood',
            name='status',
            field=models.CharField(choices=[('Request Sent', 'Request Sent'), ('Reject', 'Reject'), ('Approved', 'Approved')], max_length=20, null=True),
        ),
    ]