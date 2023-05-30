from .models import Filme
# Gerenciador de context ( contexto )

#   a function filme_destaque poderia incluir na funcion lista_filmes_recentes, conforme abaixo e assim foi feito conforme abaixo

# def lista_filmes_recentes(request):    # Geranda uma função com o parametro request
#     lista_filmes = Filme.objects.all().order_by('-data_criacao')[0:8] # criando uma variavel e definindo o que vou buscar no banco de dados
#     return {"lista_filmes_recentes": lista_filmes} # Criando um dicionario onde a lis_fil_rec é a chave primaria e que receberá o valor da variavel lista_filmes.
# essa linha teria que incluida em context processors
#'filme.novos_context.filme_destaque',

def lista_filmes_recentes(request):
    lista_filmes = Filme.objects.all().order_by('-data_criacao')[0:8]
    if lista_filmes:
        filme_destaque = lista_filmes[0]
    else:
        filme_destaque = None
    return {"lista_filmes_recentes": lista_filmes, "filme_destaque": filme_destaque}


def lista_filmes_emalta(request):
    lista_filmes = Filme.objects.all().order_by('-visualizacoes')[0:8]
    return {"lista_filmes_emalta": lista_filmes}


def filme_destaque(request):
    filme = Filme.objects.order_by('-data-criacao')[0]
    return {"filme_destaque": filme}




