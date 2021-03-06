# -*- coding: utf-8 -*-
# Generated by Django 1.10.dev20160107235441 on 2016-10-25 03:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('configuration_name', models.CharField(max_length=200, unique=True)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('display_order', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('signal_name', models.CharField(choices=[('None', 'None'), ('lavfi.signalstats.BRNG', 'BRNG'), ('lavfi.cropdetect.y2', 'Crop Bottom'), ('lavfi.cropdetect.y1', 'Crop Top'), ('lavfi.cropdetect.x1', 'Crop Left'), ('lavfi.cropdetect.x2', 'Crop Right'), ('lavfi.cropdetect.h', 'Crop Height'), ('lavfi.cropdetect.w', 'Crop Width'), ('lavfi.cropdetect.x', 'Crop X'), ('lavfi.cropdetect.y', 'Crop Y'), ('lavfi.signalstats.HUEAVG', 'HUE AVG'), ('lavfi.signalstats.HUEMED', 'HUE MED'), ('lavfi.psnr.mse_avg', 'MSEf Avg'), ('lavfi.psnr.mse.u', 'MSEf U'), ('lavfi.psnr.mse.v', 'MSEf V'), ('lavfi.psnr.mse.y', 'MSEf Y'), ('lavfi.psnr.psnr_avg', 'PSNRf Avg'), ('lavfi.psnr.psnr.u', 'PSNRf U'), ('lavfi.psnr.psnr.v', 'PSNRf V'), ('lavfi.psnr.psnr.y', 'PSNRf Y'), ('lavfi.r128.I', 'R128.I'), ('lavfi.r128.LRA', 'R128.LRA'), ('lavfi.r128.LRA.high', 'R28.LRA.high'), ('lavfi.r128.LRA.low', 'R128.LRA.low'), ('lavfi.r128.M', 'R128.M'), ('lavfi.r128.S', 'R128.S'), ('lavfi.signalstats.SATAVG', 'SAT AVG'), ('lavfi.signalstats.SATHIGH', 'SAT HIGH'), ('lavfi.signalstats.SATLOW', 'SAT LOW'), ('lavfi.signalstats.SATMAX', 'SAT MAX'), ('lavfi.signalstats.SATMIN', 'SAT MIN'), ('lavfi.signalstats.TOUT', 'TOUT'), ('lavfi.signalstats.UAVG', 'U AVG'), ('lavfi.signalstats.UDIF', 'U DIF'), ('lavfi.signalstats.UHIGH', 'U HIGH'), ('lavfi.signalstats.ULOW', 'U LOW'), ('lavfi.signalstats.UMAX', 'U MAX'), ('lavfi.signalstats.UMIN', 'U MIN'), ('lavfi.signalstats.VAVG', 'V AVG'), ('lavfi.signalstats.VDIF', 'V DIF'), ('lavfi.signalstats.VHIGH', 'V HIGH'), ('lavfi.signalstats.VLOW', 'V LOW'), ('lavfi.signalstats.VMAX', 'V MAX'), ('lavfi.signalstats.VMIN', 'V MIN'), ('lavfi.signalstats.VREP', 'VREP'), ('lavfi.signalstats.YAVG', 'Y AVG'), ('lavfi.signalstats.YDIF', 'Y DIF'), ('lavfi.signalstats.YHIGH', 'Y HIGH'), ('lavfi.signalstats.YLOW', 'Y LOW'), ('lavfi.signalstats.YMAX', 'Y MAX'), ('lavfi.signalstats.YMIN', 'Y MIN')], max_length=200)),
                ('second_signal_name', models.CharField(choices=[('None', 'None'), ('lavfi.signalstats.BRNG', 'BRNG'), ('lavfi.cropdetect.y2', 'Crop Bottom'), ('lavfi.cropdetect.y1', 'Crop Top'), ('lavfi.cropdetect.x1', 'Crop Left'), ('lavfi.cropdetect.x2', 'Crop Right'), ('lavfi.cropdetect.h', 'Crop Height'), ('lavfi.cropdetect.w', 'Crop Width'), ('lavfi.cropdetect.x', 'Crop X'), ('lavfi.cropdetect.y', 'Crop Y'), ('lavfi.signalstats.HUEAVG', 'HUE AVG'), ('lavfi.signalstats.HUEMED', 'HUE MED'), ('lavfi.psnr.mse_avg', 'MSEf Avg'), ('lavfi.psnr.mse.u', 'MSEf U'), ('lavfi.psnr.mse.v', 'MSEf V'), ('lavfi.psnr.mse.y', 'MSEf Y'), ('lavfi.psnr.psnr_avg', 'PSNRf Avg'), ('lavfi.psnr.psnr.u', 'PSNRf U'), ('lavfi.psnr.psnr.v', 'PSNRf V'), ('lavfi.psnr.psnr.y', 'PSNRf Y'), ('lavfi.r128.I', 'R128.I'), ('lavfi.r128.LRA', 'R128.LRA'), ('lavfi.r128.LRA.high', 'R28.LRA.high'), ('lavfi.r128.LRA.low', 'R128.LRA.low'), ('lavfi.r128.M', 'R128.M'), ('lavfi.r128.S', 'R128.S'), ('lavfi.signalstats.SATAVG', 'SAT AVG'), ('lavfi.signalstats.SATHIGH', 'SAT HIGH'), ('lavfi.signalstats.SATLOW', 'SAT LOW'), ('lavfi.signalstats.SATMAX', 'SAT MAX'), ('lavfi.signalstats.SATMIN', 'SAT MIN'), ('lavfi.signalstats.TOUT', 'TOUT'), ('lavfi.signalstats.UAVG', 'U AVG'), ('lavfi.signalstats.UDIF', 'U DIF'), ('lavfi.signalstats.UHIGH', 'U HIGH'), ('lavfi.signalstats.ULOW', 'U LOW'), ('lavfi.signalstats.UMAX', 'U MAX'), ('lavfi.signalstats.UMIN', 'U MIN'), ('lavfi.signalstats.VAVG', 'V AVG'), ('lavfi.signalstats.VDIF', 'V DIF'), ('lavfi.signalstats.VHIGH', 'V HIGH'), ('lavfi.signalstats.VLOW', 'V LOW'), ('lavfi.signalstats.VMAX', 'V MAX'), ('lavfi.signalstats.VMIN', 'V MIN'), ('lavfi.signalstats.VREP', 'VREP'), ('lavfi.signalstats.YAVG', 'Y AVG'), ('lavfi.signalstats.YDIF', 'Y DIF'), ('lavfi.signalstats.YHIGH', 'Y HIGH'), ('lavfi.signalstats.YLOW', 'Y LOW'), ('lavfi.signalstats.YMAX', 'Y MAX'), ('lavfi.signalstats.YMIN', 'Y MIN')], default=None, max_length=100)),
                ('op_name', models.CharField(choices=[('average', 'average'), ('exceeds', 'exceeds'), ('average_difference', 'average_difference')], max_length=20)),
                ('cut_off_number', models.IntegerField(default=0)),
                ('display_order', models.IntegerField(default=0)),
                ('configuration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='policies.Configuration')),
            ],
        ),
    ]
