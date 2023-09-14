# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AAssembly(models.Model):
    size = models.CharField(primary_key=True, max_length=16)  # The composite primary key (size, assembly_price) found, that is not supported. The first column is selected.
    assembly_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'a_assembly'
        unique_together = (('size', 'assembly_price'),)


class ABellmouth(models.Model):
    size = models.CharField(primary_key=True, max_length=50)  # The composite primary key (size, motortype) found, that is not supported. The first column is selected.
    motortype = models.CharField(max_length=16)
    bellmouth_size = models.CharField(max_length=16)
    bellmouth_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'a_bellmouth'
        unique_together = (('size', 'motortype'),)


class AController(models.Model):
    size = models.CharField(primary_key=True, max_length=16)  # The composite primary key (size, motortype, ph) found, that is not supported. The first column is selected.
    motortype = models.CharField(max_length=16)
    ph = models.CharField(max_length=32)
    controller_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'a_controller'
        unique_together = (('size', 'motortype', 'ph'),)


class AFan(models.Model):
    size = models.CharField(primary_key=True, max_length=50)  # The composite primary key (size, motortype) found, that is not supported. The first column is selected.
    motortype = models.CharField(max_length=50)
    fan_size = models.CharField(max_length=16)
    fan_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'a_fan'
        unique_together = (('size', 'motortype'),)


class AFilter(models.Model):
    size = models.CharField(primary_key=True, max_length=16)  # The composite primary key (size, filterstyle) found, that is not supported. The first column is selected.
    filterstyle = models.CharField(max_length=16)
    filterpressure = models.CharField(max_length=16)
    filter_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'a_filter'
        unique_together = (('size', 'filterstyle'),)


class AJab(models.Model):
    size = models.CharField(primary_key=True, max_length=16)
    jab_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'a_jab'


class AMotor(models.Model):
    size = models.CharField(primary_key=True, max_length=16)  # The composite primary key (size, motortype, ph) found, that is not supported. The first column is selected.
    motortype = models.CharField(max_length=16)
    ph = models.CharField(max_length=32)
    motor_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'a_motor'
        unique_together = (('size', 'motortype', 'ph'),)


class ANct(models.Model):
    size = models.CharField(primary_key=True, max_length=16)
    nct_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'a_nct'


class APack(models.Model):
    size = models.CharField(primary_key=True, max_length=16)  # The composite primary key (size, pack_price) found, that is not supported. The first column is selected.
    pack_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'a_pack'
        unique_together = (('size', 'pack_price'),)


class AVolt(models.Model):
    size = models.CharField(primary_key=True, max_length=50)  # The composite primary key (size, volt_name) found, that is not supported. The first column is selected.
    volt_name = models.CharField(max_length=50)
    volt_price = models.FloatField()
    volt_count = models.FloatField()

    class Meta:
        managed = False
        db_table = 'a_volt'
        unique_together = (('size', 'volt_name'),)


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


class BAssembly(models.Model):
    size = models.CharField(primary_key=True, max_length=16)  # The composite primary key (size, assembly_price) found, that is not supported. The first column is selected.
    assembly_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'b_assembly'
        unique_together = (('size', 'assembly_price'),)


class BBellmouth(models.Model):
    size = models.CharField(primary_key=True, max_length=50)  # The composite primary key (size, motortype) found, that is not supported. The first column is selected.
    motortype = models.CharField(max_length=16)
    bellmouth_size = models.CharField(max_length=16)
    bellmouth_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'b_bellmouth'
        unique_together = (('size', 'motortype'),)


class BController(models.Model):
    size = models.CharField(primary_key=True, max_length=16)  # The composite primary key (size, motortype, ph) found, that is not supported. The first column is selected.
    motortype = models.CharField(max_length=16)
    ph = models.CharField(max_length=32)
    controller_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'b_controller'
        unique_together = (('size', 'motortype', 'ph'),)


class BFan(models.Model):
    size = models.CharField(primary_key=True, max_length=50)  # The composite primary key (size, motortype) found, that is not supported. The first column is selected.
    motortype = models.CharField(max_length=50)
    fan_size = models.CharField(max_length=16)
    fan_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'b_fan'
        unique_together = (('size', 'motortype'),)


class BFilter(models.Model):
    size = models.CharField(primary_key=True, max_length=16)  # The composite primary key (size, filterstyle) found, that is not supported. The first column is selected.
    filterstyle = models.CharField(max_length=16)
    filterpressure = models.CharField(max_length=16)
    filter_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'b_filter'
        unique_together = (('size', 'filterstyle'),)


class BJab(models.Model):
    size = models.CharField(primary_key=True, max_length=16)
    jab_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'b_jab'


class BMotor(models.Model):
    size = models.CharField(primary_key=True, max_length=16)  # The composite primary key (size, motortype, ph) found, that is not supported. The first column is selected.
    motortype = models.CharField(max_length=16)
    ph = models.CharField(max_length=32)
    motor_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'b_motor'
        unique_together = (('size', 'motortype', 'ph'),)


class BNct(models.Model):
    size = models.CharField(primary_key=True, max_length=16)
    nct_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'b_nct'


class BPack(models.Model):
    size = models.CharField(primary_key=True, max_length=16)  # The composite primary key (size, pack_price) found, that is not supported. The first column is selected.
    pack_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'b_pack'
        unique_together = (('size', 'pack_price'),)


class BVolt(models.Model):
    size = models.CharField(primary_key=True, max_length=50)  # The composite primary key (size, volt_name) found, that is not supported. The first column is selected.
    volt_name = models.CharField(max_length=50)
    volt_price = models.FloatField()
    volt_count = models.FloatField()

    class Meta:
        managed = False
        db_table = 'b_volt'
        unique_together = (('size', 'volt_name'),)


class CAssembly(models.Model):
    size = models.CharField(primary_key=True, max_length=16)  # The composite primary key (size, assembly_price) found, that is not supported. The first column is selected.
    assembly_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'c_assembly'
        unique_together = (('size', 'assembly_price'),)


class CBellmouth(models.Model):
    size = models.CharField(primary_key=True, max_length=50)  # The composite primary key (size, motortype) found, that is not supported. The first column is selected.
    motortype = models.CharField(max_length=16)
    bellmouth_size = models.CharField(max_length=16)
    bellmouth_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'c_bellmouth'
        unique_together = (('size', 'motortype'),)


class CController(models.Model):
    size = models.CharField(primary_key=True, max_length=16)  # The composite primary key (size, motortype, ph) found, that is not supported. The first column is selected.
    motortype = models.CharField(max_length=16)
    ph = models.CharField(max_length=32)
    controller_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'c_controller'
        unique_together = (('size', 'motortype', 'ph'),)


class CFan(models.Model):
    size = models.CharField(primary_key=True, max_length=50)  # The composite primary key (size, motortype) found, that is not supported. The first column is selected.
    motortype = models.CharField(max_length=50)
    fan_size = models.CharField(max_length=16)
    fan_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'c_fan'
        unique_together = (('size', 'motortype'),)


class CFilter(models.Model):
    size = models.CharField(primary_key=True, max_length=16)  # The composite primary key (size, filterstyle) found, that is not supported. The first column is selected.
    filterstyle = models.CharField(max_length=16)
    filterpressure = models.CharField(max_length=16)
    filter_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'c_filter'
        unique_together = (('size', 'filterstyle'),)


class CJab(models.Model):
    size = models.CharField(primary_key=True, max_length=16)
    jab_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'c_jab'


class CMotor(models.Model):
    size = models.CharField(primary_key=True, max_length=16)  # The composite primary key (size, motortype, ph) found, that is not supported. The first column is selected.
    motortype = models.CharField(max_length=16)
    ph = models.CharField(max_length=32)
    motor_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'c_motor'
        unique_together = (('size', 'motortype', 'ph'),)


class CNct(models.Model):
    size = models.CharField(primary_key=True, max_length=16)
    nct_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'c_nct'


class CPack(models.Model):
    size = models.CharField(primary_key=True, max_length=16)  # The composite primary key (size, pack_price) found, that is not supported. The first column is selected.
    pack_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'c_pack'
        unique_together = (('size', 'pack_price'),)


class CVolt(models.Model):
    size = models.CharField(primary_key=True, max_length=50)  # The composite primary key (size, volt_name) found, that is not supported. The first column is selected.
    volt_name = models.CharField(max_length=50)
    volt_price = models.FloatField()
    volt_count = models.FloatField()

    class Meta:
        managed = False
        db_table = 'c_volt'
        unique_together = (('size', 'volt_name'),)


class DAssembly(models.Model):
    size = models.CharField(primary_key=True, max_length=16)  # The composite primary key (size, assembly_price) found, that is not supported. The first column is selected.
    assembly_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'd_assembly'
        unique_together = (('size', 'assembly_price'),)


class DBellmouth(models.Model):
    size = models.CharField(primary_key=True, max_length=50)  # The composite primary key (size, motortype) found, that is not supported. The first column is selected.
    motortype = models.CharField(max_length=16)
    bellmouth_size = models.CharField(max_length=16)
    bellmouth_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'd_bellmouth'
        unique_together = (('size', 'motortype'),)


class DController(models.Model):
    size = models.CharField(primary_key=True, max_length=16)  # The composite primary key (size, motortype, ph) found, that is not supported. The first column is selected.
    motortype = models.CharField(max_length=16)
    ph = models.CharField(max_length=32)
    controller_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'd_controller'
        unique_together = (('size', 'motortype', 'ph'),)


class DFan(models.Model):
    size = models.CharField(primary_key=True, max_length=50)  # The composite primary key (size, motortype) found, that is not supported. The first column is selected.
    motortype = models.CharField(max_length=50)
    fan_size = models.CharField(max_length=16)
    fan_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'd_fan'
        unique_together = (('size', 'motortype'),)


class DFilter(models.Model):
    size = models.CharField(primary_key=True, max_length=16)  # The composite primary key (size, filterstyle) found, that is not supported. The first column is selected.
    filterstyle = models.CharField(max_length=16)
    filterpressure = models.CharField(max_length=16)
    filter_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'd_filter'
        unique_together = (('size', 'filterstyle'),)


class DJab(models.Model):
    size = models.CharField(primary_key=True, max_length=16)
    jab_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'd_jab'


class DMotor(models.Model):
    size = models.CharField(primary_key=True, max_length=16)  # The composite primary key (size, motortype, ph) found, that is not supported. The first column is selected.
    motortype = models.CharField(max_length=16)
    ph = models.CharField(max_length=32)
    motor_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'd_motor'
        unique_together = (('size', 'motortype', 'ph'),)


class DNct(models.Model):
    size = models.CharField(primary_key=True, max_length=16)
    nct_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'd_nct'


class DPack(models.Model):
    size = models.CharField(primary_key=True, max_length=16)  # The composite primary key (size, pack_price) found, that is not supported. The first column is selected.
    pack_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'd_pack'
        unique_together = (('size', 'pack_price'),)


class DVolt(models.Model):
    size = models.CharField(primary_key=True, max_length=50)  # The composite primary key (size, volt_name) found, that is not supported. The first column is selected.
    volt_name = models.CharField(max_length=50)
    volt_price = models.FloatField()
    volt_count = models.FloatField()

    class Meta:
        managed = False
        db_table = 'd_volt'
        unique_together = (('size', 'volt_name'),)


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


class EAssembly(models.Model):
    size = models.CharField(primary_key=True, max_length=16)  # The composite primary key (size, assembly_price) found, that is not supported. The first column is selected.
    assembly_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'e_assembly'
        unique_together = (('size', 'assembly_price'),)


class EBellmouth(models.Model):
    size = models.CharField(primary_key=True, max_length=50)  # The composite primary key (size, motortype) found, that is not supported. The first column is selected.
    motortype = models.CharField(max_length=16)
    bellmouth_size = models.CharField(max_length=16)
    bellmouth_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'e_bellmouth'
        unique_together = (('size', 'motortype'),)


class EController(models.Model):
    size = models.CharField(primary_key=True, max_length=16)  # The composite primary key (size, motortype, ph) found, that is not supported. The first column is selected.
    motortype = models.CharField(max_length=16)
    ph = models.CharField(max_length=32)
    controller_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'e_controller'
        unique_together = (('size', 'motortype', 'ph'),)


class EFan(models.Model):
    size = models.CharField(primary_key=True, max_length=50)  # The composite primary key (size, motortype) found, that is not supported. The first column is selected.
    motortype = models.CharField(max_length=50)
    fan_size = models.CharField(max_length=16)
    fan_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'e_fan'
        unique_together = (('size', 'motortype'),)


class EFilter(models.Model):
    size = models.CharField(primary_key=True, max_length=16)  # The composite primary key (size, filterstyle) found, that is not supported. The first column is selected.
    filterstyle = models.CharField(max_length=16)
    filterpressure = models.CharField(max_length=16)
    filter_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'e_filter'
        unique_together = (('size', 'filterstyle'),)


class EJab(models.Model):
    size = models.CharField(primary_key=True, max_length=16)
    jab_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'e_jab'


class EMotor(models.Model):
    size = models.CharField(primary_key=True, max_length=16)  # The composite primary key (size, motortype, ph) found, that is not supported. The first column is selected.
    motortype = models.CharField(max_length=16)
    ph = models.CharField(max_length=32)
    motor_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'e_motor'
        unique_together = (('size', 'motortype', 'ph'),)


class ENct(models.Model):
    size = models.CharField(primary_key=True, max_length=16)
    nct_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'e_nct'


class EPack(models.Model):
    size = models.CharField(primary_key=True, max_length=16)  # The composite primary key (size, pack_price) found, that is not supported. The first column is selected.
    pack_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'e_pack'
        unique_together = (('size', 'pack_price'),)


class EVolt(models.Model):
    size = models.CharField(primary_key=True, max_length=50)  # The composite primary key (size, volt_name) found, that is not supported. The first column is selected.
    volt_name = models.CharField(max_length=50)
    volt_price = models.FloatField()
    volt_count = models.FloatField()

    class Meta:
        managed = False
        db_table = 'e_volt'
        unique_together = (('size', 'volt_name'),)


class Ffilter(models.Model):
    size = models.CharField(primary_key=True, max_length=16)  # The composite primary key (size, filterstyle, filterpressure, windspeed) found, that is not supported. The first column is selected.
    filterstyle = models.CharField(max_length=16)
    filterpressure = models.CharField(max_length=16)
    windspeed = models.CharField(max_length=16)
    filter_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ffilter'
        unique_together = (('size', 'filterstyle', 'filterpressure', 'windspeed'),)


class GenAssembly(models.Model):
    size = models.CharField(primary_key=True, max_length=16)  # The composite primary key (size, assembly_price) found, that is not supported. The first column is selected.
    assembly_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gen_assembly'
        unique_together = (('size', 'assembly_price'),)


class GenBellmouth(models.Model):
    size = models.CharField(primary_key=True, max_length=50)  # The composite primary key (size, motortype) found, that is not supported. The first column is selected.
    motortype = models.CharField(max_length=16)
    bellmouth_size = models.CharField(max_length=16)
    bellmouth_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gen_bellmouth'
        unique_together = (('size', 'motortype'),)


class GenController(models.Model):
    size = models.CharField(primary_key=True, max_length=16)  # The composite primary key (size, motortype, ph) found, that is not supported. The first column is selected.
    motortype = models.CharField(max_length=16)
    ph = models.CharField(max_length=32)
    controller_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gen_controller'
        unique_together = (('size', 'motortype', 'ph'),)


class GenFan(models.Model):
    size = models.CharField(primary_key=True, max_length=50)  # The composite primary key (size, motortype) found, that is not supported. The first column is selected.
    motortype = models.CharField(max_length=50)
    fan_size = models.CharField(max_length=16)
    fan_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gen_fan'
        unique_together = (('size', 'motortype'),)


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
    size = models.CharField(primary_key=True, max_length=16)  # The composite primary key (size, motortype, ph, location) found, that is not supported. The first column is selected.
    motortype = models.CharField(max_length=16)
    ph = models.CharField(max_length=32)
    motor_price = models.IntegerField()
    location = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'gen_motor'
        unique_together = (('size', 'motortype', 'ph', 'location'),)


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
    volt_price = models.FloatField()
    volt_count = models.FloatField()

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


class HighBellmouth(models.Model):
    size = models.CharField(primary_key=True, max_length=50)  # The composite primary key (size, motortype) found, that is not supported. The first column is selected.
    motortype = models.CharField(max_length=16)
    bellmouth_size = models.CharField(max_length=16)
    bellmouth_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'high_bellmouth'
        unique_together = (('size', 'motortype'),)


class HighController(models.Model):
    size = models.CharField(primary_key=True, max_length=16)  # The composite primary key (size, motortype, ph) found, that is not supported. The first column is selected.
    motortype = models.CharField(max_length=16)
    ph = models.CharField(max_length=32)
    controller_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'high_controller'
        unique_together = (('size', 'motortype', 'ph'),)


class HighFan(models.Model):
    size = models.CharField(primary_key=True, max_length=50)  # The composite primary key (size, motortype) found, that is not supported. The first column is selected.
    motortype = models.CharField(max_length=50)
    fan_size = models.CharField(max_length=16)
    fan_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'high_fan'
        unique_together = (('size', 'motortype'),)


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
    size = models.CharField(primary_key=True, max_length=16)  # The composite primary key (size, motortype, ph) found, that is not supported. The first column is selected.
    motortype = models.CharField(max_length=16)
    ph = models.CharField(max_length=32)
    motor_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'high_motor'
        unique_together = (('size', 'motortype', 'ph'),)


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
    volt_price = models.FloatField()
    volt_count = models.FloatField()

    class Meta:
        managed = False
        db_table = 'high_volt'
        unique_together = (('size', 'volt_name'),)


class LoadQuantity(models.Model):
    size = models.CharField(primary_key=True, max_length=50)  # The composite primary key (size, ea) found, that is not supported. The first column is selected.
    ea = models.IntegerField()
    carsize = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'load_quantity'
        unique_together = (('size', 'ea'),)


class LocationMovecost(models.Model):
    location = models.CharField(primary_key=True, max_length=50)  # The composite primary key (location, carsize) found, that is not supported. The first column is selected.
    carsize = models.CharField(max_length=50)
    move_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'location_movecost'
        unique_together = (('location', 'carsize'),)
