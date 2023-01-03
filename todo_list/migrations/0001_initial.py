# Generated by Django 4.1.4 on 2023-01-03 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tag",
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
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Task",
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
                ("content", models.CharField(max_length=600)),
                ("datetime", models.DateTimeField(auto_now=True)),
                ("deadline", models.DateTimeField(blank=True, null=True)),
                ("done_or_not", models.BooleanField()),
                (
                    "tags",
                    models.ManyToManyField(related_name="tasks", to="todo_list.tag"),
                ),
            ],
        ),
    ]
