# Generated by Django 3.0.5 on 2020-04-22 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('self_introductions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='self_introductions_notes_text',
            name='category',
            field=models.CharField(choices=[('subtitle', 'subtitle'), ('code', 'code'), ('content', 'content'), ('IMAGE', 'IMAGE')], default='content', max_length=20),
        ),
    ]
