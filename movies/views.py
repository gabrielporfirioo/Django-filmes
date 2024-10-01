from multiprocessing import AuthenticationError
from django.shortcuts import render, redirect
import requests
from .models import Movie
from .forms import MovieForm, SignUpForm
from django.contrib.auth import login
from .forms import SignUpForm, MovieForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .utils import get_movie_from_omdb
from django.shortcuts import render, redirect, get_object_or_404





@login_required 
def movie_list(request):
    movies = Movie.objects.filter(user=request.user)
    return render(request, 'movies/movie_list.html', {'movies': movies})

@login_required 
def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.user = request.user  # Associa o filme ao usuário logado
            
            movie_title = form.cleaned_data['title']
            custom_description = form.cleaned_data['custom_description']
            
            # Fazer consulta à API OMDb
            movie_data = get_movie_from_omdb(movie_title)
            
            if movie_data:
                # Criar e salvar o objeto Movie no banco de dados com a descrição personalizada
                movie = Movie(
                    title=movie_data['title'],
                    year=movie_data['year'],
                    description=movie_data['plot'],
                    custom_description=custom_description,
                    poster_url=movie_data['poster'],
                    user = request.user,
                )
                movie.save()
                return redirect('movie_list')
            else:
                form.add_error(None, "Filme não encontrado ou erro na API.")
    else:
        form = MovieForm()

    return render(request, 'movies/add_movie.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = AuthenticationError(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('http://127.0.0.1:8000/movies/accounts/profile/')  
            else:
                form.add_error(None, 'Invalid username or password.')
    else:
        form = MovieForm()
    
    return render(request, 'login.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Faz o login automático após o cadastro
            return redirect('movie_list')  # Redireciona para a página inicial ou outra de sua escolha
    else:
        form = SignUpForm()
    
    return render(request, 'registration/signup.html', {'form': form})

@login_required 
def logout(request):
    if request.method == 'POST':
        return render(request, 'login.html')
    

def home_redirect(request):
    return redirect('login')

@login_required 
def delete_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id, user=request.user)
    
    if request.method == 'POST':
        movie.delete()
        return redirect('movie_list')
    
    


    
