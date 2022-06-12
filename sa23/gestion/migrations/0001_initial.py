# Generated by Django 4.0.3 on 2022-06-12 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enseignant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100, null=True)),
                ('groupe', models.CharField(max_length=100, null=True)),
                ('photo', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(default=None, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Examens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('date', models.DateField(blank=True, null=True)),
                ('coefficient', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ressources',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_ressource', models.CharField(max_length=100)),
                ('nom', models.CharField(max_length=100)),
                ('descriptif', models.CharField(max_length=100)),
                ('coefficient', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(null=True)),
                ('nom', models.CharField(max_length=100)),
                ('semestre', models.IntegerField(null=True)),
                ('credit', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.IntegerField(null=True)),
                ('appreciation', models.CharField(max_length=100)),
                ('etudiant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gestion.etudiant')),
                ('examens', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gestion.examens')),
            ],
        ),
        migrations.AddField(
            model_name='examens',
            name='ressources',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gestion.ressources'),
        ),
    ]
