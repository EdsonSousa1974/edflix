from django.shortcuts import redirect, reverse
from .models import Filme
from .forms import CriarContaForm
from django.views.generic import TemplateView, ListView, DetailView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

# url view html

#Function based views
# def homepage(request):
#     return render(request, "homepage.html")

#Function based views
# def homefilmes(request):
#     context = {}
#     lista_filmes = Filme.objects.all()
#     context['lista_filmes'] = lista_filmes
#     return render(request, "homefilmes.html", context)

#Class based views
class Homepage(TemplateView):
    template_name = "homepage.html"

    def get(self, request, *args, **kwargs) :
        if request.user.is_authenticated: 
            # Redificiona para homefilmes
            return redirect('filme:homefilmes')
        else: 
            # Redificiona para homepage
            return super().get(request, *args, **kwargs) 


class Homefilmes(LoginRequiredMixin, ListView):
    template_name = "homefilmes.html"
    model = Filme #object_list


class Detalhesfilme(LoginRequiredMixin, DetailView):
    template_name = "detalhesfilme.html"
    model = Filme #object

    def get(self, request, *args, **kwargs) :
        #decobrindo qual filme está sendo acessado
        filme = self.get_object()
        filme.visualizacoes += 1
        filme.save()
        usuario = request.user
        usuario.filmes_vistos.add(filme)
        return super().get(request, *args, **kwargs) # Redificiona o usuário para a URL final

    def get_context_data(self, **kwargs):
        context = super(Detalhesfilme, self).get_context_data(**kwargs)
        
        # filtrar a minha tabela de filmes pegando os filmes cuja categoria é igual a categoria do filme da página (object)
        # self.get_object()
        filmes_relacionados = Filme.objects.filter(categoria=self.get_object().categoria)[0:8]
        context['filmes_relacionados'] = filmes_relacionados
        return context


class Pesquisafilmes(LoginRequiredMixin, ListView):
    template_name = "pesquisafilmes.html"
    model = Filme #object_list
    
    def get_queryset(self):
        termo_pesquisa = self.request.GET.get('query')
        if termo_pesquisa:
            #object_list = Filme.objects.filter(titulo__icontains=termo_pesquisa)
            object_list = self.model.objects.filter(titulo__icontains=termo_pesquisa)
            return object_list        
        else: 
            return None
    
class Paginaperfil(LoginRequiredMixin, TemplateView):
    template_name = "editarperfil.html"

class Criarconta(FormView):
    template_name = "criarconta.html"
    form_class = CriarContaForm
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('filme:login')
