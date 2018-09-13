# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('yandex_money', '0002_lazy_defaults'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='user',
            field=models.ForeignKey(
                verbose_name='\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c',
                blank=True,
                to=settings.AUTH_USER_MODEL,
                null=True,
                related_name='yandex_payments',
                on_delete=models.SET_NULL,
            )
        ),
    ]
