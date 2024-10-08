# Generated by Django 5.1.1 on 2024-09-30 19:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lawyer_app', '0002_client_profile_complete_lawyer_profile_complete_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cases', to='lawyer_app.client'),
        ),
        migrations.AlterField(
            model_name='case',
            name='lawyer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cases', to='lawyer_app.lawyer'),
        ),
    ]
