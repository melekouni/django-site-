# Generated by Django 4.1.7 on 2023-05-25 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0019_delete_client"),
        ("superviseur", "0003_point_rssi_post"),
    ]

    operations = [
        migrations.AddField(
            model_name="client",
            name="superviseur",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="home.supervisor",
            ),
        ),
    ]