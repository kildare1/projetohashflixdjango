from django.db import models
from django.utils import timezone   # utilizado para extrair data e hora da criacao do filme
from django.contrib.auth.models import AbstractUser


# Create your models here.

LISTA_CATEGORIAS = (
    ("ANALISE", "Análise"),
    ("PROGRAMACAO", "Programacao"),
    ("APRESENTACAO", "Apresentação"),
    ("OUTROS", "Outros"),
)

# Criar o filme
class Filme(models.Model):

    titulos = models.CharField(max_length=100)  # CharField -> campo de texto
    thumb = models.ImageField(upload_to='thumb_filmes')
    descricao = models.TextField(max_length=1000)   # TextField mais de uma linha de texto
    categoria = models.CharField(max_length=15, choices=LISTA_CATEGORIAS)  # choices -> opçoes da lista_caategorias que é uma tupla com varias tuplas
    visualizacoes = models.IntegerField(default=0)   # IntegerField -> Numeros inteiros
    data_criacao = models.DateTimeField(default=timezone.now)     # DateTimeField  -> data e hora. precisa importar o timezone

    # mostra o formato de string do objeto da classe, como voce quer que ele seja exibido qdo der um print
    def __str__(self):
        return self.titulos

#criar os episodios
class Episodio(models.Model):
    filme = models.ForeignKey("Filme", related_name="episodios", on_delete=models.CASCADE)  # chave primaria de varios episodio para um unico filme
    titulos = models.CharField(max_length=100)
    video = models.URLField()

    def __str__(self):
        return self.filme.titulos + " - " + self.titulos


# criar o usuario
class Usuario(AbstractUser):
    filmes_vistos = models.ManyToManyField("Filme")


