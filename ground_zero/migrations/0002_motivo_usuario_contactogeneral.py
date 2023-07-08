# Generated by Django 4.1.2 on 2023-07-07 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ground_zero', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Motivo',
            fields=[
                ('id_motivo', models.AutoField(db_column='idMotivo', primary_key=True, serialize=False)),
                ('motivo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.AutoField(db_column='idUsuario', primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=100, null=True, unique=True)),
                ('contraseña', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ContactoGeneral',
            fields=[
                ('id_contactoGeneral', models.AutoField(db_column='idContactoGeneral', primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=80)),
                ('email', models.EmailField(blank=True, max_length=100, null=True, unique=True)),
                ('mensaje', models.CharField(max_length=500)),
                ('imagen', models.ImageField(null=True, upload_to='ground_zero')),
                ('id_motivo', models.ForeignKey(db_column='idMotivo', on_delete=django.db.models.deletion.CASCADE, to='ground_zero.motivo')),
            ],
        ),
    ]
