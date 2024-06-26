# Generated by Django 4.1.7 on 2023-03-26 19:22

import datetime
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
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tile_id', models.IntegerField()),
                ('commodity', models.TextField()),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='No Name')),
                ('creation_date', models.DateTimeField(default=datetime.datetime(2023, 3, 26, 19, 22, 23, 381164, tzinfo=datetime.timezone.utc))),
            ],
        ),
        migrations.CreateModel(
            name='Graph',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('node1_id', models.IntegerField()),
                ('node2_id', models.IntegerField()),
                ('edge_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invite_accept_status', models.IntegerField(default=0)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.game')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Nodes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('node_id', models.IntegerField()),
                ('tile1_id', models.IntegerField()),
                ('tile2_id', models.IntegerField()),
                ('tile3_id', models.IntegerField()),
                ('board_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.board')),
                ('player_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='game.player')),
            ],
        ),
        migrations.AddField(
            model_name='board',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.game'),
        ),
    ]
