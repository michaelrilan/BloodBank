# Generated by Django 4.0.6 on 2023-05-29 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainbb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='add_reqblood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('patientname', models.CharField(max_length=100)),
                ('patientage', models.DecimalField(decimal_places=0, max_digits=3)),
                ('sex', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('healthfac', models.CharField(max_length=200)),
                ('healthfacadd', models.CharField(max_length=200)),
                ('contactnum', models.DecimalField(decimal_places=0, max_digits=11)),
                ('disease', models.CharField(max_length=100)),
                ('unit', models.DecimalField(decimal_places=0, max_digits=3)),
                ('bloodtype', models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], max_length=4)),
                ('status', models.CharField(choices=[('Request Sent', 'Request Sent'), ('Reject', 'Reject'), ('Approved', 'Approved')], max_length=20, null=True)),
                ('date_request', models.DateField(null=True)),
                ('remarks', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='add_reqdonate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('fullname', models.CharField(max_length=100)),
                ('age', models.DecimalField(decimal_places=0, max_digits=3)),
                ('sex', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('add', models.CharField(max_length=200)),
                ('contactnum', models.DecimalField(decimal_places=0, max_digits=11)),
                ('weight', models.DecimalField(decimal_places=0, max_digits=3)),
                ('disease', models.CharField(max_length=100)),
                ('unit', models.DecimalField(decimal_places=0, max_digits=3, null=True)),
                ('bloodtype', models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], max_length=4)),
                ('status', models.CharField(choices=[('Request Sent', 'Request Sent'), ('Pending', 'Pending'), ('Reject', 'Reject'), ('Approved', 'Approved')], max_length=20, null=True)),
                ('date_request', models.DateField(null=True)),
                ('remarks', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='blood_counter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Apos', models.DecimalField(decimal_places=0, max_digits=9)),
                ('Aneg', models.DecimalField(decimal_places=0, max_digits=9)),
                ('Bpos', models.DecimalField(decimal_places=0, max_digits=9)),
                ('Bneg', models.DecimalField(decimal_places=0, max_digits=9)),
                ('ABpos', models.DecimalField(decimal_places=0, max_digits=9)),
                ('ABneg', models.DecimalField(decimal_places=0, max_digits=9)),
                ('Opos', models.DecimalField(decimal_places=0, max_digits=9)),
                ('Oneg', models.DecimalField(decimal_places=0, max_digits=9)),
            ],
        ),
        migrations.CreateModel(
            name='reg_admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('pword', models.CharField(max_length=50)),
                ('fullname', models.CharField(max_length=100)),
                ('profession', models.CharField(choices=[('Medical Technologist', 'Medical Technologist'), ('Physician', 'Physician'), ('Nurse', 'Nurse')], max_length=30)),
                ('sex', models.CharField(max_length=6)),
                ('contactnum', models.DecimalField(decimal_places=0, max_digits=11)),
            ],
        ),
        migrations.AlterField(
            model_name='reg_donor_patient',
            name='age',
            field=models.DecimalField(decimal_places=0, max_digits=3),
        ),
        migrations.AlterField(
            model_name='reg_donor_patient',
            name='sex',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10),
        ),
    ]