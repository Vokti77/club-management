# Generated by Django 4.2 on 2023-04-13 11:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="MemberProfile",
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
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=100)),
                ("contact", models.CharField(max_length=100)),
                ("department", models.CharField(max_length=50)),
                ("batch", models.CharField(max_length=30)),
                ("address", models.CharField(max_length=100)),
                ("image", models.FileField(upload_to="image/")),
                ("cv", models.FileField(upload_to="cv/")),
                (
                    "status",
                    models.CharField(
                        choices=[("1", "Approved"), ("2", "Pending")],
                        default="2",
                        max_length=2,
                        null=True,
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DonorProfile",
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
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=100)),
                ("contact", models.CharField(max_length=100)),
                ("address", models.CharField(max_length=100)),
                ("image", models.FileField(upload_to="image/")),
                (
                    "blood",
                    models.CharField(
                        choices=[
                            ("A+", "A+"),
                            ("B+", "B+"),
                            ("O+", "O+"),
                            ("AB+", "AB+"),
                            ("AB-", "AB-"),
                            ("A-", "A-"),
                            ("B-", "B-"),
                        ],
                        default="B+",
                        max_length=5,
                        null=True,
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
