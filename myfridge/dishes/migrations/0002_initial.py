# Generated by Django 4.2.1 on 2023-07-23 21:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("dishes", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="dish",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="dish",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="dishes.dishcategory"
            ),
        ),
        migrations.AddField(
            model_name="dish",
            name="country",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="dishes.country"
            ),
        ),
        migrations.AddField(
            model_name="dish",
            name="level",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="dishes.difficultylevel"
            ),
        ),
        migrations.AddField(
            model_name="dish",
            name="main_ingredient",
            field=models.ManyToManyField(to="dishes.mainingredient"),
        ),
        migrations.AddField(
            model_name="dish",
            name="other_ingredients",
            field=models.ManyToManyField(to="dishes.otheringredient"),
        ),
        migrations.AddField(
            model_name="dish",
            name="time_to_make",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="dishes.timetomake"
            ),
        ),
    ]
