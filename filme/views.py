from django.shortcuts import render, redirect, reverse
from .models import Filme, Usuario
from .forms import CriarContaForm, FormHomepage
from django.views.generic import TemplateView, ListView, DetailView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin


class Homepage(FormView):
    template_name = "homepage.html"
    form_class = FormHomepage

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('filme:homefilmes')  # redirecionando para outra pagina, nesse caso a homefilmes - o filme e homefilme, foram dados no arquivo URLs do app(filme)
        else:
            return super().get(request, *args, **kwargs)  # redireciona para a homepage

    def get_success_url(self):
        email = self.request.POST.get("email")
        usuarios = Usuario.objects.filter(email=email)
        if usuarios:
            return reverse('filme:login')
        else:
            return reverse('filme:criarconta')

# tentando mostrar o que o quest_sucess_url(self) vai buscar. não deu certo, rever
        # email = self.request.POST.get("email"):
        # print(self.request.POST)
        # return


class Homefilmes(LoginRequiredMixin, ListView):
    template_name = "homefilmes.html"
    model = Filme
    # object_lis -> Lista de itens do modelo

class Detalhesfilme(LoginRequiredMixin, DetailView):
    template_name = "detalhesfilme.html"
    model = Filme
    # object -> 1 item do modelo

    def get(self, request, *args, **kwargs):
        # descobrir qual o filme ele está acessando
        filme = self.get_object()
        # somar 1 nas visualizacoes daquele filme
        filme.visualizacoes += 1
        #salvando o acrescimo nas visualizações
        filme.save()
        usuario = request.user
        usuario.filmes_vistos.add(filme)
        return super().get(request, *args, **kwargs)   # redireciona o susario para a url final

    def get_context_data(self, **kwargs):
        context = super(Detalhesfilme, self).get_context_data(**kwargs)
        filmes_relacionados = self.model.objects.filter(categoria=self.get_object().categoria)[0:3]
        context["filmes_relacionados"] = filmes_relacionados
        return context

class Pesquisafilme(LoginRequiredMixin, ListView):
    template_name = "pesquisa.html"
    model = Filme

    # Editando o nosso obect_list
    def get_queryset(self):
        termo_pesquisa = self.request.GET.get('query')
        if termo_pesquisa:
            object_list = self.model.objects.filter(titulos__icontains=termo_pesquisa)
            return object_list
        else:
            return None

class Paginaperfil(LoginRequiredMixin, UpdateView):
    template_name = "editarperfil.html"
    model = Usuario
    fields = ['first_name', 'last_name', 'email']

    def get_success_url(self):
        return reverse('filme:homefilmes')

class Criarconta(FormView):
    template_name = 'criarconta.html'
    form_class = CriarContaForm

    def form_valid(self, form):   # Função que verifica se o formulario é valido
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('filme:login')  # sempre utiliza-se reverse quando a função pede um link(URL) como resposta







# url - view - html
# # Create your views here.
# def homepage(request):
#     return render(request, "homepage.html")
# transformando de função ou medoto para classe precisa mudar na filmes\urls "urlpattners"

# def homefilmes(request):
#     context = {}
#     lista_filmes = Filme.objects.all()
#     context['lista_filmes'] = lista_filmes
#     return render(request, "homefilmes.html", context)

# transformando de função ou medoto para classe precisa mudar na filmes\urls "urlpattners"

