# Generated by Django 4.1.4 on 2022-12-27 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("todo_list", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="task",
            old_name="don_or_not",
            new_name="done_or_not",
        ),
    ]
