# Generated by Django 4.1.7 on 2023-05-15 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("superviseur", "0002_project_dat_deb_project_dat_fin"),
    ]

    operations = [
        migrations.AddField(
            model_name="point",
            name="RSSI",
            field=models.FloatField(null=True),
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("temperature", models.BigIntegerField()),
                ("humidity", models.BigIntegerField()),
                ("published_date", models.DateTimeField(blank=True, null=True)),
                (
                    "node",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="superviseur.point",
                    ),
                ),
            ],
        ),
    ]
