# Generated by Django 2.2.7 on 2020-02-10 20:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import portola.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agreement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('website', models.CharField(blank=True, default='', max_length=255)),
                ('country', models.CharField(blank=True, default='', max_length=100)),
                ('bio', models.TextField(blank=True, max_length=500)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('name', models.SlugField(max_length=80)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(blank=True, default='', max_length=100)),
                ('type', models.CharField(choices=[['REPORT', 'Report'], ['RAW', 'Raw'], ['PAN', 'PAN File'], ['MIAM', 'Module IAM Report'], ['PANRPT', 'PAN Report'], ['FER', 'field exposure rpt'], ['FINREL', 'final reliability'], ['interim1 reliability', 'interim1 reliability'], ['interim2', 'interim2'], ['LID', 'LID'], ['INTAKE', 'Intake'], ['FWR', 'Factory Witness Report'], ['financials(VDP)', 'financials(VDP)'], ['IFT', 'Inverter Field Testing - Other'], ['IPQPF', 'Inverter PQP Final'], ['IPQPILT', 'Inverter PQP Interim Lab Test'], ['MFT', 'Module Field Testing - Other'], ['MINTAKE', 'Module Intake'], ['MLID', 'Module LID'], ['MDML', 'Module Mechanical Load (Static, Dynamic, Other)'], ['MNOCT', 'Module NOCT'], ['MPANF', 'Module PAN File'], ['MPANR', 'Module PAN Report'], ['MPID', 'Module PID Testing'], ['MPQPF', 'Module PQP Final'], ['MPQPFE', 'Module PQP Field Exposure'], ['MPQPI1', 'Module PQP Interim 1'], ['MPQPI2', 'Module PQP Interim 2'], ['MPQPI3', 'Module PQP Interim 3'], ['MISC', 'Miscellaneous'], ['MCEY', 'Module Comparative Energy Yield'], ['RIE', 'Racking Installation Efficiency']], default='REPORT', max_length=32)),
                ('issued_date', models.DateField(default=django.utils.timezone.now)),
                ('product_type', models.CharField(choices=[['modules', 'modules'], ['racking', 'racking'], ['inverter', 'inverter'], ['optimizer', 'optimizer']], default='MODULES', max_length=32)),
                ('box_id', models.CharField(blank=True, default='', max_length=30)),
                ('disclosure', models.CharField(choices=[['GENERAL', 'General'], ['BY REQUEST', 'By Request'], ['UNAVAILABLE', 'Undisclosed'], ['PENDING', 'Pending Authorization'], ['VDP', 'VDP']], default='GENERAL', max_length=100)),
                ('disclosure_date', models.DateField(blank=True, null=True)),
                ('factory_witness_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_name', models.CharField(max_length=100)),
                ('legal_name', models.CharField(max_length=100, unique=True)),
                ('type', models.CharField(choices=[['PARTNER', 'Downstream Partner'], ['CLIENT', 'Downstream Client'], ['MANUFACTURER', 'Manufacturer'], ['PVEL', 'PVEL']], default='DOWNSTREAM', max_length=100)),
                ('website', models.CharField(blank=True, default='', max_length=255)),
                ('country', models.CharField(blank=True, default='', max_length=100)),
                ('company_type', models.CharField(choices=[['DEV', 'Developer (Developer, EPC, Installer, O+M Provider)'], ['INV', 'Investor (Investor, Finance Institution)'], ['MFG', 'Manufacturer'], ['OWN', 'Owner (IPP, Public Utility Company)'], ['EPC', 'Engineering, Procurement and Construction (EPC) Company'], ['IE', "Independent Engineer (Owner's Engineer, Technical Advisor)"], ['IPP', 'Independent Power Producer'], ['SUP', 'Supplier']], default='MFG', max_length=100)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='portola.Company')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('followers', models.ManyToManyField(related_name='entities_following', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('legal_name',),
            },
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField()),
            ],
            options={
                'ordering': ('create_date',),
            },
        ),
        migrations.CreateModel(
            name='TechnologyTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('type', models.CharField(choices=[['Tracker Type', 'Tracker Type'], ['Racking Type', 'Racking Type'], ['Power Bin', 'Power Bin'], ['Mounting Type', 'Mounting Type'], ['Misc', 'Misc'], ['Max Voltage', 'Max Voltage'], ['Inverter Type', 'Inverter Type'], ['Cell Type', 'Cell Type'], ['Cell Count', 'Cell Count'], ['Cell Chemistry', 'Cell Chemistry'], ['Battery Type', 'Battery Type'], ['Battery Testing', 'Battery Testing']], default='Power Bin', max_length=32)),
            ],
            options={
                'ordering': ('type', 'title'),
            },
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('resolved', models.DateField(blank=True, null=True)),
                ('expires', models.DateField(blank=True, default=portola.models._request_expiration, null=True)),
                ('last_updated', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[['ACTIVE', 'ACTIVE'], ['APPROVED', 'APPROVED'], ['REFUSED', 'REFUSED'], ['EXPIRED', 'EXPIRED']], default='ACTIVE', max_length=100)),
                ('requestor_comment', models.TextField(blank=True, null=True)),
                ('approver_comment', models.TextField(blank=True, null=True)),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='portola.Document')),
                ('requestor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='PVModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.DecimalField(decimal_places=2, max_digits=5)),
                ('longitude', models.DecimalField(decimal_places=2, max_digits=5)),
                ('surface_tilt', models.DecimalField(decimal_places=2, max_digits=5)),
                ('surface_azimuth', models.DecimalField(decimal_places=2, max_digits=5)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(blank=True, max_length=16)),
                ('name', models.CharField(blank=True, max_length=32, null=True)),
                ('status', models.CharField(choices=[['ACTIVE', 'ACTIVE'], ['INACTIVE', 'INACTIVE']], default='ACTIVE', max_length=100)),
                ('salesforce_id', models.CharField(blank=True, max_length=10, null=True)),
                ('type', models.CharField(choices=[['MPQP', 'Module PQP'], ['IPQP', 'Inverter PQP'], ['SPQP', 'Storage PQP']], default='MPQP', max_length=100)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portola.Entity')),
                ('document_approver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='document_approver', to=settings.AUTH_USER_MODEL)),
                ('followers', models.ManyToManyField(related_name='projects_following', to=settings.AUTH_USER_MODEL)),
                ('primary_contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('pvel_manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pvel_manager', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('number',),
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('location', models.CharField(blank=True, max_length=30)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('box_user', models.CharField(blank=True, max_length=30)),
                ('entity', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='portola.Entity')),
                ('user', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('user',),
            },
        ),
        migrations.CreateModel(
            name='NotificationQueue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transport', models.CharField(choices=[['EMAIL', 'EMAIL']], default='EMAIL', max_length=8)),
                ('subject', models.CharField(blank=True, db_index=True, default='', max_length=255)),
                ('text_body', models.TextField(blank=True, default='')),
                ('html_body', models.TextField(blank=True, default='')),
                ('queued_date', models.DateTimeField(auto_now_add=True)),
                ('sent', models.BooleanField(default=False)),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('queued_date',),
            },
        ),
        migrations.CreateModel(
            name='NewsFeed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_updated', models.DateTimeField(auto_now_add=True)),
                ('subject', models.CharField(blank=True, default='', max_length=100)),
                ('body', models.TextField()),
                ('type', models.CharField(choices=[['PARTNER', 'Downstream Partner'], ['CLIENT', 'Downstream Client'], ['MANUFACTURER', 'Manufacturer'], ['PVEL', 'PVEL']], default='PVEL', max_length=100)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='newsfeed_created_by', to=settings.AUTH_USER_MODEL)),
                ('last_updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='newsfeed_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('subject',),
            },
        ),
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_updated', models.DateTimeField(auto_now_add=True)),
                ('subject', models.CharField(blank=True, default='', max_length=100)),
                ('body', models.TextField()),
                ('section', models.CharField(blank=True, default='', max_length=100)),
                ('type', models.CharField(choices=[['PARTNER', 'Downstream Partner'], ['CLIENT', 'Downstream Client'], ['MANUFACTURER', 'Manufacturer'], ['PVEL', 'PVEL']], default='PVEL', max_length=100)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='faq_created_by', to=settings.AUTH_USER_MODEL)),
                ('last_updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='faq_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('subject',),
            },
        ),
        migrations.AddField(
            model_name='document',
            name='entity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='document_entity', to='portola.Entity'),
        ),
        migrations.AddField(
            model_name='document',
            name='permitted_entities',
            field=models.ManyToManyField(blank=True, related_name='permitted_entities', to='portola.Entity'),
        ),
        migrations.AddField(
            model_name='document',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='document_project', to='portola.Project'),
        ),
        migrations.AddField(
            model_name='document',
            name='technology_tags',
            field=models.ManyToManyField(related_name='documents', to='portola.TechnologyTag'),
        ),
    ]