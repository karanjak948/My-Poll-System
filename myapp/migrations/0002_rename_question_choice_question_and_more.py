# Generated by Django 5.1.3 on 2024-11-15 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='Question',
            new_name='question',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='Question_text',
            new_name='question_text',
        ),
    ]
