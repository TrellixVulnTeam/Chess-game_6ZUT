# Generated by Django 2.0.2 on 2018-03-23 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chesslogic', '0002_chesspiecemove_sidee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chesspiecemove',
            name='side',
        ),
    ]
