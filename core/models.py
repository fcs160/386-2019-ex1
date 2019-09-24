from django.db import models

# Create your models here.
class Contato(models.Model):
    nome= models.CharField(max_length=50)
    endereco= models.CharField(max_length=200)
    email= models.EmailField(max_length=100)
    data_nascimento= models.DateField()
    telefone = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nome
class Livro(models.Model):
    Titulo= models.CharField(max_length=150)
    Nome_autor= models.CharField(max_length=200)
    Assunto= models.CharField(max_length=200)
    Editora= models.CharField(max_length=200)
    ISBN = models.CharField(max_length=20)
    Ano_publicacao = models.DateField()

    def __str__(self):
        return self.Titulo

class Compra(models.Model):
    nomec = models.CharField(max_length=80)
    descricaoProduto = models.CharField(max_length=100)
    qtdPrevistoMes = models.FloatField()
    preco = models.FloatField()
    precoMax = models.FloatField()

    def __str__(self):
        return self.nomec

class Despesa(models.Model):
    datacriacao = models.CharField(max_length=35)
    tipodespesa = models.CharField(max_length=50)
    descricao = models.CharField(max_length=60)
    formapagamento = models.CharField(max_length=40)
    vencimento = models.DateField()
    quitado = models.BooleanField()


    def __str__(self):
        return self.datacriacao
