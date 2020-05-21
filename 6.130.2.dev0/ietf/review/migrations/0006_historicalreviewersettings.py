# Copyright The IETF Trust 2018-2020, All Rights Reserved
# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-09 08:31


from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import ietf.utils.models
import ietf.utils.validators
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0003_groupfeatures_data'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('person', '0008_auto_20181014_1448'),
        ('review', '0005_set_secdir_notify_ad_when'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalReviewerSettings',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('min_interval', models.IntegerField(blank=True, choices=[(7, 'Once per week'), (14, 'Once per fortnight'), (30, 'Once per month'), (61, 'Once per two months'), (91, 'Once per quarter')], null=True, verbose_name='Can review at most')),
                ('filter_re', models.CharField(blank=True, help_text='Draft names matching this regular expression should not be assigned', max_length=255, validators=[ietf.utils.validators.RegexStringValidator()], verbose_name='Filter regexp')),
                ('skip_next', models.IntegerField(default=0, verbose_name='Skip next assignments')),
                ('remind_days_before_deadline', models.IntegerField(blank=True, help_text="To get an email reminder in case you forget to do an assigned review, enter the number of days before review deadline you want to receive it. Clear the field if you don't want a reminder.", null=True)),
                ('expertise', models.TextField(blank=True, default='', help_text="Describe the reviewer's expertise in this team's area", max_length=2048, verbose_name="Reviewer's expertise in this team's area")),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('person', ietf.utils.models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='person.Person')),
                ('team', ietf.utils.models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='group.Group')),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical reviewer settings',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
