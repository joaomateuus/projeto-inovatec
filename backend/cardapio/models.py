from django.db import models

def upload_image_book(instance, filename):
    return f"{instance.id_book}-{filename}"

class Prato(models.Model):
    nome = models.CharField(max_length=40)
    valor = models.FloatField()
    detalhes = models.TextField()
    foto = models.ImageField(upload_to=upload_image_book, blank=True, null=True)

    def __str__(self):
        return self.nome

