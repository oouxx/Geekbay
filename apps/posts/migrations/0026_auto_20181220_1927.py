# Generated by Django 2.0 on 2018-12-20 19:27

from django.db import migrations, models
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0025_auto_20181220_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opensource',
            name='description',
            field=mdeditor.fields.MDTextField(verbose_name='描述'),
        ),
        migrations.AlterField(
            model_name='software',
            name='type',
            field=models.CharField(choices=[('All', 'All'), ('Windows', 'Windows'), ('Android', 'Android'), ('IOS', 'IOS'), ('MAC', 'MAC'), ('Linux', 'Linux')], default='All', max_length=10, verbose_name='软件分类'),
        ),
    ]
