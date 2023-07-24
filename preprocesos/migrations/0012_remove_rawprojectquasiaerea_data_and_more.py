# Generated by Django 4.2.2 on 2023-07-18 23:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("preprocesos", "0011_rawprojectquasiterreno_origen_coordenadas_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="rawprojectquasiaerea",
            name="data",
        ),
        migrations.RemoveField(
            model_name="rawprojectquasiterreno",
            name="data",
        ),
        migrations.AddField(
            model_name="rawdataquasiaerea",
            name="data",
            field=models.ForeignKey(
                blank=True,
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="proyectos_crudos_quasi_geoidales",
                to="preprocesos.rawprojectquasiaerea",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="rawdataquasiterreno",
            name="nomenclatura",
            field=models.CharField(default=None, max_length=20, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="rawdataquasiterreno",
            name="project",
            field=models.ForeignKey(
                blank=True,
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="proyectos_crudos_quasi_geoidales",
                to="preprocesos.rawprojectquasiterreno",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="rawprojectquasiterreno",
            name="origen_coordenadas",
            field=models.CharField(
                choices=[
                    ("original", "Original"),
                    ("nivelacion", "Coordenadas de nivelación"),
                    ("gravedad", "Coordenadas de gravedad"),
                ],
                default="original",
                max_length=20,
            ),
        ),
    ]
