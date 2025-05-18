from django.db import models
from django.utils import timezone
import uuid

class Example(models.Model):
    # Campos básicos de texto
    nombre = models.CharField(max_length=255, verbose_name="Nombre del Item")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción Detallada")

    # Campos numéricos
    entero = models.IntegerField(default=0, verbose_name="Número Entero")
    entero_positivo = models.PositiveIntegerField(verbose_name="Entero Positivo")
    entero_pequeno = models.SmallIntegerField(verbose_name="Entero Pequeño")
    entero_pequeno_positivo = models.PositiveSmallIntegerField(verbose_name="Entero Pequeño Positivo")
    flotante = models.FloatField(verbose_name="Número de Punto Flotante")
    decimal = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Número Decimal")

    # Campos booleanos
    activo = models.BooleanField(default=True, verbose_name="Está Activo")
    nulo_booleano = models.NullBooleanField(verbose_name="Booleano Nulo") # Obsoleto en versiones recientes, usar BooleanField(null=True)

    # Campos de fecha y hora
    fecha = models.DateField(verbose_name="Fecha")
    fecha_hora = models.DateTimeField(default=timezone.now, verbose_name="Fecha y Hora")
    duracion = models.DurationField(verbose_name="Duración")

    # Campos de relación (claves foráneas y muchos a muchos)
    # Para estos, necesitarías otros modelos definidos. Aquí solo se muestran los tipos.
    # clave_foranea = models.ForeignKey('OtroModelo', on_delete=models.CASCADE)
    # muchos_a_muchos = models.ManyToManyField('OtroModelo')

    # Campos de archivo e imagen
    archivo = models.FileField(upload_to='archivos/', blank=True, null=True, verbose_name="Archivo")
    imagen = models.ImageField(upload_to='imagenes/', blank=True, null=True, verbose_name="Imagen")

    # Campos de correo electrónico y URL
    email = models.EmailField(blank=True, null=True, verbose_name="Correo Electrónico")
    url = models.URLField(blank=True, null=True, verbose_name="Dirección URL")
    slug = models.SlugField(unique=True, verbose_name="Slug (URL amigable)")

    # Campos para selecciones fijas
    OPCIONES = [
        ('opcion1', 'Opción Uno'),
        ('opcion2', 'Opción Dos'),
        ('opcion3', 'Opción Tres'),
    ]
    seleccion = models.CharField(max_length=10, choices=OPCIONES, default='opcion1', verbose_name="Selección")

    # Campo para números grandes
    big_entero = models.BigIntegerField(verbose_name="Número Entero Grande")

    # Campo para direcciones IP
    ip_address = models.GenericIPAddressField(blank=True, null=True, verbose_name="Dirección IP")

    # Campo para UUIDs (identificadores únicos universales)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="UUID") # Necesitas importar uuid

    def __str__(self):
        return self.nombre