from django.db import models

# Create your models here.

class Artista(models.Model):
    id_artista  = models.AutoField(db_column='idArtista', primary_key=True)
    artista     = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return str(self.artista)


class Producto(models.Model):
    id_producto     = models.CharField(primary_key=True, max_length=10)
    id_artista      = models.ForeignKey('Artista', on_delete=models.CASCADE, db_column='idArtista')
    nombre          = models.CharField(max_length=30)
    concepto        = models.CharField(max_length=50)
    tecnica         = models.CharField(max_length=50)
    precio          = models.IntegerField()
    descripcion     = models.CharField(max_length=500)
    imagen          = models.ImageField(upload_to="ground_zero", null=True)

    def __str__(self):
        return str(self.nombre)+" "+str(self.precio)
    

class Motivo(models.Model):
    id_motivo   = models.AutoField(db_column='idMotivo', primary_key=True)
    motivo      = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return str(self.motivo)
    

class ContactoGeneral(models.Model):
    id_motivo           = models.ForeignKey('Motivo', on_delete=models.CASCADE, db_column='idMotivo')
    id_contactoGeneral  = models.AutoField(db_column='idContactoGeneral', primary_key=True)
    nombre              = models.CharField(max_length=100)
    apellidos           = models.CharField(max_length=100)
    username            = models.CharField(max_length=80)
    email               = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    mensaje             = models.CharField(max_length=500)
    imagen              = models.ImageField(upload_to="ground_zero", null=True)

    def __str__(self):
        return str(self.id_motivo)+" - "+str(self.id_contactoGeneral)
    
class Usuario(models.Model):
    id_usuario      = models.AutoField(db_column='idUsuario', primary_key=True)
    nombre          = models.CharField(max_length=50)
    email           = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    contraseña      = models.CharField(max_length=30)

    def __str__(self):
        return str(self.nombre)+" - "+str(self.email)