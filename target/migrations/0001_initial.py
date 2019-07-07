# Generated by Django 2.2.2 on 2019-07-03 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Labeling',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='添加时间', verbose_name='添加时间')),
                ('create_user_id', models.CharField(help_text='创建人id', max_length=255, verbose_name='创建人id')),
                ('title', models.CharField(max_length=255)),
                ('frameNum', models.IntegerField(default=0)),
                ('nfft', models.IntegerField(default=4410)),
                ('current_frame', models.IntegerField(default=0)),
                ('manual_pos', models.IntegerField(default=-1)),
                ('extend_rad', models.IntegerField(default=60)),
                ('tone_extend_rad', models.IntegerField(default=60)),
                ('vad_thrart_EE', models.FloatField(default=0.1)),
                ('vad_thrart_RMSE', models.FloatField(default=0.1)),
                ('vad_throp_EE', models.FloatField(default=0.1)),
                ('filter_rad', models.FloatField(default=30)),
                ('fs', models.IntegerField(default=44100)),
                ('play_fs', models.IntegerField(default=44100)),
                ('primary_ref', models.CharField(default='combDescan', max_length=255)),
                ('medium_resampling', models.BooleanField(default=True)),
            ],
            options={
                'unique_together': {('title', 'create_user_id', 'nfft')},
            },
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='添加时间', verbose_name='添加时间')),
                ('create_user_id', models.CharField(help_text='创建人id', max_length=255, verbose_name='创建人id')),
                ('title', models.CharField(max_length=255)),
                ('content', models.CharField(max_length=255)),
                ('timestamp', models.DateTimeField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MarkedPhrase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='添加时间', verbose_name='添加时间')),
                ('create_user_id', models.CharField(help_text='创建人id', max_length=255, verbose_name='创建人id')),
                ('title', models.CharField(max_length=255)),
                ('mark', models.CharField(max_length=255)),
                ('start', models.FloatField()),
                ('length', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='添加时间', verbose_name='添加时间')),
                ('create_user_id', models.CharField(help_text='创建人id', max_length=255, verbose_name='创建人id')),
                ('title', models.CharField(max_length=255)),
                ('pos', models.IntegerField()),
                ('length', models.IntegerField()),
                ('pitch', models.FloatField()),
                ('note', models.CharField(max_length=16)),
                ('tone', models.CharField(max_length=16)),
                ('anote', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Wave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='添加时间', verbose_name='添加时间')),
                ('create_user_id', models.CharField(help_text='创建人id', max_length=255, verbose_name='创建人id')),
                ('title', models.CharField(max_length=255)),
                ('waveFile', models.CharField(max_length=255)),
                ('frameNum', models.IntegerField(default=0)),
                ('duration', models.FloatField()),
                ('chin', models.BinaryField(null=True)),
                ('ee', models.BinaryField(null=True)),
                ('rmse', models.BinaryField(null=True)),
                ('fs', models.IntegerField()),
                ('nfft', models.IntegerField(default=4410)),
                ('completion', models.FloatField()),
            ],
            options={
                'unique_together': {('title', 'create_user_id', 'nfft')},
            },
        ),
        migrations.CreateModel(
            name='Tune',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='添加时间', verbose_name='添加时间')),
                ('create_user_id', models.CharField(help_text='创建人id', max_length=255, verbose_name='创建人id')),
                ('tune_name', models.CharField(max_length=255)),
                ('a4_hz', models.FloatField(default=440.0)),
                ('do', models.CharField(max_length=16)),
                ('note1', models.CharField(max_length=16)),
                ('note2', models.CharField(max_length=16)),
                ('note3', models.CharField(max_length=16)),
                ('note4', models.CharField(max_length=16)),
                ('note5', models.CharField(max_length=16)),
                ('note6', models.CharField(max_length=16)),
                ('note7', models.CharField(max_length=16)),
            ],
            options={
                'unique_together': {('tune_name', 'create_user_id')},
            },
        ),
        migrations.CreateModel(
            name='Clip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='添加时间', verbose_name='添加时间')),
                ('create_user_id', models.CharField(help_text='创建人id', max_length=255, verbose_name='创建人id')),
                ('title', models.CharField(max_length=255)),
                ('startingPos', models.IntegerField()),
                ('length', models.IntegerField()),
                ('src', models.BinaryField(null=True)),
                ('tar', models.BinaryField(null=True)),
                ('anote', models.CharField(max_length=255)),
                ('nfft', models.IntegerField()),
            ],
            options={
                'unique_together': {('title', 'startingPos', 'length', 'create_user_id', 'nfft')},
            },
        ),
        migrations.CreateModel(
            name='Stft',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='添加时间', verbose_name='添加时间')),
                ('create_user_id', models.CharField(help_text='创建人id', max_length=255, verbose_name='创建人id')),
                ('startingPos', models.IntegerField()),
                ('length', models.IntegerField()),
                ('src', models.BinaryField(null=True)),
                ('labeling', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='target.Labeling')),
            ],
            options={
                'unique_together': {('labeling', 'startingPos', 'length')},
            },
        ),
        migrations.CreateModel(
            name='LabelingAlgorithmsConf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='添加时间', verbose_name='添加时间')),
                ('create_user_id', models.CharField(help_text='创建人id', max_length=255, verbose_name='创建人id')),
                ('algorithms', models.CharField(max_length=255)),
                ('is_filter', models.BooleanField(default=True)),
                ('anote', models.CharField(max_length=255, null=True)),
                ('labeling', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='target.Labeling')),
            ],
            options={
                'unique_together': {('labeling', 'algorithms')},
            },
        ),
        migrations.CreateModel(
            name='AlgorithmsMediums',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='添加时间', verbose_name='添加时间')),
                ('create_user_id', models.CharField(help_text='创建人id', max_length=255, verbose_name='创建人id')),
                ('algorithms', models.CharField(max_length=255)),
                ('startingPos', models.IntegerField()),
                ('length', models.IntegerField()),
                ('medium', models.BinaryField(null=True)),
                ('anote', models.CharField(max_length=255)),
                ('labeling', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='target.Labeling')),
            ],
            options={
                'unique_together': {('labeling', 'algorithms', 'startingPos', 'length')},
            },
        ),
        migrations.CreateModel(
            name='AlgorithmsClips',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='添加时间', verbose_name='添加时间')),
                ('create_user_id', models.CharField(help_text='创建人id', max_length=255, verbose_name='创建人id')),
                ('algorithms', models.CharField(max_length=255)),
                ('startingPos', models.IntegerField()),
                ('length', models.IntegerField()),
                ('tar', models.BinaryField(null=True)),
                ('anote', models.CharField(max_length=255)),
                ('labeling', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='target.Labeling')),
            ],
            options={
                'unique_together': {('labeling', 'algorithms', 'startingPos', 'length')},
            },
        ),
    ]
