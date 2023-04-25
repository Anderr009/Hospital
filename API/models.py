from django.db import models


class Cargo(models.Model):
    id_cargo = models.AutoField(db_column='ID_CARGO', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=20, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CARGO'


class Cliente(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    cedula = models.CharField(db_column='CEDULA', unique=True, max_length=11, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pasaporte = models.CharField(db_column='PASAPORTE', unique=True, max_length=10, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    nombre1 = models.CharField(db_column='NOMBRE1', max_length=25, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    nombre2 = models.CharField(db_column='NOMBRE2', max_length=25, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    apellido1 = models.CharField(db_column='APELLIDO1', max_length=25, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    apellido2 = models.CharField(db_column='APELLIDO2', max_length=25, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fecha_nacimiento = models.DateField(db_column='FECHA_NACIMIENTO', blank=True, null=True)  # Field name made lowercase.
    nacionalidad = models.CharField(db_column='NACIONALIDAD', max_length=50, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tipo_sangre = models.CharField(db_column='TIPO_SANGRE', max_length=3, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLIENTE'


class Empleado(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    cedula = models.CharField(db_column='CEDULA', unique=True, max_length=11, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    nombre1 = models.CharField(db_column='NOMBRE1', max_length=25, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    nombre2 = models.CharField(db_column='NOMBRE2', max_length=25, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    apellido1 = models.CharField(db_column='APELLIDO1', max_length=25, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    apellido2 = models.CharField(db_column='APELLIDO2', max_length=25, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='USERNAME', max_length=20, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    passw = models.CharField(db_column='PASSW', max_length=18, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fk_hospital = models.ForeignKey('Hospital', models.DO_NOTHING, db_column='FK_HOSPITAL', blank=True, null=True)  # Field name made lowercase.
    fk_cargo = models.ForeignKey(Cargo, models.DO_NOTHING, db_column='FK_CARGO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EMPLEADO'


class ExamenFisico(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    aspecto_general = models.TextField(db_column='ASPECTO_GENERAL', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cabeza = models.TextField(db_column='CABEZA', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cuello = models.TextField(db_column='CUELLO', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    corazon = models.TextField(db_column='CORAZON', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    torax = models.TextField(db_column='TORAX', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    abdomen = models.TextField(db_column='ABDOMEN', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    genitales = models.TextField(db_column='GENITALES', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pulmones = models.TextField(db_column='PULMONES', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    extremidades = models.TextField(db_column='EXTREMIDADES', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    exam_neurol = models.TextField(db_column='EXAM_NEUROL', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    tacto_rectal = models.TextField(db_column='TACTO_RECTAL', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    tacto_vaginal = models.TextField(db_column='TACTO_VAGINAL', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fk_registro = models.ForeignKey('Registro', models.DO_NOTHING, db_column='FK_REGISTRO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EXAMEN_FISICO'


class Hospital(models.Model):
    cod_hospital = models.AutoField(db_column='COD_HOSPITAL', primary_key=True)  # Field name made lowercase.
    nombre_hosp = models.CharField(db_column='NOMBRE_HOSP', max_length=25, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    nombre_ceo = models.CharField(db_column='NOMBRE_CEO', max_length=40, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    numero_fax = models.IntegerField(db_column='NUMERO_FAX', blank=True, null=True)  # Field name made lowercase.
    telefono = models.IntegerField(db_column='TELEFONO', blank=True, null=True)  # Field name made lowercase.
    tipo_hospital = models.CharField(db_column='TIPO_HOSPITAL', max_length=20, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    api_key = models.CharField(db_column='API_KEY', unique=True, max_length=30, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HOSPITAL'


class Imagenes(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    electrocardiograma = models.TextField(db_column='ELECTROCARDIOGRAMA', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    rayosx = models.TextField(db_column='RAYOSX', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sonografia = models.TextField(db_column='SONOGRAFIA', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    tomografia_axial = models.TextField(db_column='TOMOGRAFIA_AXIAL', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    diagnostico = models.TextField(db_column='DIAGNOSTICO', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fecha = models.DateField(db_column='FECHA', blank=True, null=True)  # Field name made lowercase.
    fk_registro2 = models.ForeignKey('Registro', models.DO_NOTHING, db_column='FK_REGISTRO2', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IMAGENES'


class Placas(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    foto = models.TextField(db_column='FOTO', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fk_imag = models.ForeignKey(Imagenes, models.DO_NOTHING, db_column='FK_IMAG', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PLACAS'


class Registro(models.Model):
    cod_registro = models.AutoField(db_column='COD_REGISTRO', primary_key=True)  # Field name made lowercase.
    motivo = models.TextField(db_column='MOTIVO', db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fecha_llegada = models.DateTimeField(db_column='FECHA_LLEGADA', blank=True, null=True)  # Field name made lowercase.
    fechahora_clasificacion = models.DateTimeField(db_column='FECHAHORA_CLASIFICACION', blank=True, null=True)  # Field name made lowercase.
    fechahora_final = models.DateTimeField(db_column='FECHAHORA_FINAL', blank=True, null=True)  # Field name made lowercase.
    enfermedad = models.CharField(db_column='ENFERMEDAD', max_length=60, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fk_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='FK_CLIENTE', blank=True, null=True)  # Field name made lowercase.
    fk_empleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='FK_EMPLEADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'REGISTRO'


class Telefono(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    numero = models.IntegerField(db_column='NUMERO', blank=True, null=True)  # Field name made lowercase.
    tipo = models.ForeignKey('TipoTelefono', models.DO_NOTHING, db_column='TIPO', blank=True, null=True)  # Field name made lowercase.
    empleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='EMPLEADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TELEFONO'


class TipoTelefono(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='TIPO', max_length=30, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TIPO_TELEFONO'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, db_collation='Modern_Spanish_CI_AS')

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
    name = models.CharField(max_length=255, db_collation='Modern_Spanish_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, db_collation='Modern_Spanish_CI_AS')

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, db_collation='Modern_Spanish_CI_AS')
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, db_collation='Modern_Spanish_CI_AS')
    first_name = models.CharField(max_length=150, db_collation='Modern_Spanish_CI_AS')
    last_name = models.CharField(max_length=150, db_collation='Modern_Spanish_CI_AS')
    email = models.CharField(max_length=254, db_collation='Modern_Spanish_CI_AS')
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
    object_id = models.TextField(db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    object_repr = models.CharField(max_length=200, db_collation='Modern_Spanish_CI_AS')
    action_flag = models.SmallIntegerField()
    change_message = models.TextField(db_collation='Modern_Spanish_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, db_collation='Modern_Spanish_CI_AS')
    model = models.CharField(max_length=100, db_collation='Modern_Spanish_CI_AS')

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, db_collation='Modern_Spanish_CI_AS')
    name = models.CharField(max_length=255, db_collation='Modern_Spanish_CI_AS')
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40, db_collation='Modern_Spanish_CI_AS')
    session_data = models.TextField(db_collation='Modern_Spanish_CI_AS')
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
