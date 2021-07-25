from rest_framework import generics as apigeneric
from .forms import RegisterFormUser
from django.contrib.auth.views import LoginView, LogoutView
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import PokemonModel
import requests
import json
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse_lazy
from .serializers import PokeModelSerializer


class UserLogin(LoginView):
    template_name = 'login.html'


class UserLogout(LogoutView):
    template_name = 'login.html'


class UserRegister(generic.CreateView):
    template_name = 'register.html'
    form_class = RegisterFormUser
    success_url = '/'


class Choice(LoginRequiredMixin, generic.ListView):
    """pokemon status logic implementation and pagination
    as well as displaying a table of selected pokemon
    """

    login_url = '/'
    model = PokemonModel
    template_name = 'choice.html'

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        offset = request.GET.get('offset')
        r = requests.get(f'https://pokeapi.co/api/v2/pokemon?offset={offset}&limit=10')
        pokemons = json.loads(r.content.decode('utf-8'))['results']
        for item in pokemons:
            if PokemonModel.objects.filter(pokemon=item['name']).count() >= 1:
                item['state'] = 'BUZY'
            else:
                item['state'] = 'FREE'
        next = json.loads(r.content.decode('utf-8'))['next'].split('?')[-1]
        prew = None
        if json.loads(r.content.decode('utf-8'))['previous']:
            prew = json.loads(r.content.decode('utf-8'))['previous'].split('?')[-1]
        return self.render_to_response({'pokes': pokemons,
                                        'my_pokes': PokemonModel.objects.filter(custumer=request.user),
                                        'next': next,
                                        'previous': prew})



class Chosen(LoginRequiredMixin, generic.View):
    """The same Pokemon cannot be selected by
    different players or multiple times
    I Use try: and except: constructions"""

    login_url = 'poke:login'

    def get(self, request, *args, **kwargs):
        try:
            PokemonModel.objects.get_or_create(custumer=self.request.user,
                                            pokemon=self.kwargs['name'],
                                           pokemon_url=self.kwargs['name'])
        except:
            pass
        return HttpResponseRedirect(reverse_lazy('poke:choice'))


class UsersAllApi(apigeneric.ListAPIView):
    """ API output of all players and their Pokémons"""
    queryset = PokemonModel.objects.all()
    serializer_class = PokeModelSerializer
