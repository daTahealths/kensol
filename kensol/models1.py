# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class GenAssembly(models.Model):
    size = models.CharField(primary_key=True, max_length=16)  # The composite primary key (size, assembly_price) found, that is not supported. The first column is selected.
    assembly_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gen_assembly'
        unique_together = (('size', 'assembly_price'),)


class GenController(models.Model):
    size = models.CharField(primary_key=True, max_length=16)  # The composite primary key (size, motor_company) found, that is not supported. The first column is selected.
    motor_company = models.CharField(max_length=32)
    watt = models.CharField(max_length=32)
    motor_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gen_controller'
        unique_together = (('size', 'motor_company'),)


class GenJab(models.Model):
    size = models.CharField(primary_key=True, max_length=16)
    jab_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gen_jab'


class GenMaterialcost(models.Model):
    item = models.CharField(primary_key=True, max_length=32)  # The composite primary key (item, size) found, that is not supported. The first column is selected.
    size = models.CharField(max_length=16)
    matherialsize_width = models.FloatField()
    matherialsize_length = models.FloatField()
    rawmaterial_thickness = models.FloatField()
    rawmaterial_density = models.FloatField()
    manufacture_quantity = models.IntegerField()
    necessary_quantity = models.IntegerField()
    won_per_kg = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gen_materialcost'
        unique_together = (('item', 'size'),)


class GenMotor(models.Model):
    size = models.CharField(primary_key=True, max_length=16)  # The composite primary key (size, motor_company) found, that is not supported. The first column is selected.
    motor_company = models.CharField(max_length=32)
    watt = models.CharField(max_length=32)
    motor_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gen_motor'
        unique_together = (('size', 'motor_company'),)


class GenNct(models.Model):
    size = models.CharField(primary_key=True, max_length=16)
    nct_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gen_nct'


class GenPack(models.Model):
    size = models.CharField(primary_key=True, max_length=16)  # The composite primary key (size, pack_price) found, that is not supported. The first column is selected.
    pack_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gen_pack'
        unique_together = (('size', 'pack_price'),)


class GenPaint(models.Model):
    item = models.CharField(primary_key=True, max_length=32)  # The composite primary key (item, size) found, that is not supported. The first column is selected.
    size = models.CharField(max_length=16)
    figure_width = models.FloatField()
    figure_length = models.FloatField()
    won_per_meter = models.IntegerField()
    necessary_quantity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gen_paint'
        unique_together = (('item', 'size'),)


class GenVolt(models.Model):
    size = models.CharField(primary_key=True, max_length=50)  # The composite primary key (size, volt_name) found, that is not supported. The first column is selected.
    volt_name = models.CharField(max_length=50)
    volt_price = models.IntegerField()
    volt_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gen_volt'
        unique_together = (('size', 'volt_name'),)


class HighAssembly(models.Model):
    size = models.CharField(primary_key=True, max_length=16)  # The composite primary key (size, assembly_price) found, that is not supported. The first column is selected.
    assembly_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'high_assembly'
        unique_together = (('size', 'assembly_price'),)


class HighController(models.Model):
    size = models.CharField(primary_key=True, max_length=16)  # The composite primary key (size, motor_company) found, that is not supported. The first column is selected.
    motor_company = models.CharField(max_length=32)
    watt = models.CharField(max_length=32)
    motor_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'high_controller'
        unique_together = (('size', 'motor_company'),)


class HighJab(models.Model):
    size = models.CharField(primary_key=True, max_length=16)
    jab_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'high_jab'


class HighMaterialcost(models.Model):
    item = models.CharField(primary_key=True, max_length=32)  # The composite primary key (item, size) found, that is not supported. The first column is selected.
    size = models.CharField(max_length=16)
    matherialsize_width = models.FloatField()
    matherialsize_length = models.FloatField()
    rawmaterial_thickness = models.FloatField()
    rawmaterial_density = models.FloatField()
    manufacture_quantity = models.IntegerField()
    necessary_quantity = models.IntegerField()
    won_per_kg = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'high_materialcost'
        unique_together = (('item', 'size'),)


class HighMotor(models.Model):
    size = models.CharField(primary_key=True, max_length=16)  # The composite primary key (size, motor_company, watt) found, that is not supported. The first column is selected.
    motor_company = models.CharField(max_length=32)
    watt = models.CharField(max_length=32)
    motor_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'high_motor'
        unique_together = (('size', 'motor_company', 'watt'),)


class HighNct(models.Model):
    size = models.CharField(primary_key=True, max_length=16)
    nct_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'high_nct'


class HighPack(models.Model):
    size = models.CharField(primary_key=True, max_length=16)  # The composite primary key (size, pack_price) found, that is not supported. The first column is selected.
    pack_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'high_pack'
        unique_together = (('size', 'pack_price'),)


class HighPaint(models.Model):
    item = models.CharField(primary_key=True, max_length=32)  # The composite primary key (item, size) found, that is not supported. The first column is selected.
    size = models.CharField(max_length=16)
    figure_width = models.FloatField()
    figure_length = models.FloatField()
    won_per_meter = models.IntegerField()
    necessary_quantity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'high_paint'
        unique_together = (('item', 'size'),)


class HighVolt(models.Model):
    size = models.CharField(primary_key=True, max_length=50)  # The composite primary key (size, volt_name) found, that is not supported. The first column is selected.
    volt_name = models.CharField(max_length=50)
    volt_price = models.IntegerField()
    volt_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'high_volt'
        unique_together = (('size', 'volt_name'),)
