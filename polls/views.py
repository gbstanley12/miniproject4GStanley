from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Movie
from .models import Review
from .forms import ReviewForm
from .forms import RegisterForm
from .forms import MovieForm
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('polls:movie_list')  # Redirect to a desired page after registration
    else:
        form = RegisterForm()
    return render(request, 'polls/register.html', {'form': form})

class MovieListView(generic.ListView):
    template_name = "polls/movie_list.html"
    context_object_name = "movie_list"

    def get_queryset(self):
        """Return all movies."""
        return Movie.objects.all()

class MovieDetailView(generic.DetailView):
    model = Movie
    template_name = "polls/movie_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['review_form'] = ReviewForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        review_form = ReviewForm(request.POST)

        if review_form.is_valid():
            new_review = review_form.save(commit=False)
            new_review.movie = self.object
            new_review.user = request.user
            new_review.save()
            return redirect(reverse('polls:movie_detail', args=(self.object.id,)))
        else:
            context['review_form'] = review_form
            return self.render_to_response(context)
def home_view(request):
    reviews = Review.objects.order_by('-created_at')[:10]  # Fetch the 10 most recent reviews
    return render(request, 'home.html', {'reviews': reviews})

@login_required
def submit_review(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.movie = movie
            new_review.user = request.user
            new_review.save()
            return redirect(reverse('polls:movie_detail', args=(movie.id,)))
    else:
        form = ReviewForm()
    return render(request, 'polls/movie_detail.html', {'form': form, 'movie': movie})

    return render(request, 'home.html', {'anticipated_movies': anticipated_movies})

def movie_list_view(request):
    movies = Movie.objects.all()  # Query all movies
    return render(request, 'movie_list.html', {'movies': movies})

def add_movie_view(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('polls:movie_list')
    else:
        form = MovieForm()
    return render(request, 'polls/add_movie.html', {'form': form})

def upcoming_movies_view(request):
    anticipated_movies = [
        {
    'title': 'The Marvels',
    'release_date': 'November 10, 2023',
    'director': 'Nia DaCosta',
    'summary': 'Captain Marvel returns alongside Ms. Marvel and Monica Rambeau to face a new villain.',
    'image': 'polls/images/marvels.jpg',  # Replace with the actual path
    },
    {
        'title': 'The Hunger Games: The Ballad of Songbirds and Snakes',
        'release_date': 'November 17, 2023',
        'director': 'Francis Lawrence',  # Replace with the actual director's name
        'summary': 'A Hunger Games prequel about Coriolanus Snow and his mentee tribute.',
        'image': 'polls/images/hungergames.jpg',  # Replace with the actual path
    },
    {
        'title': 'Napoleon',
        'release_date': 'November 22, 2023',
        'director': 'Ridley Scott',
        'summary': 'A historical epic about Napoleon Bonaparte’s rise to power and his relationship with Empress Joséphine.',
        'image': 'polls/images/napolean.jpg',  # Replace with the actual path
    },
    {
        'title': 'Wonka',
        'release_date': 'December 15, 2023',
        'director': 'Paul King',
        'summary': 'An origin story of the all-singing, all-dancing chocolatier Willy Wonka.',
        'image': 'polls/images/wonka.jpg',  # Replace with the actual path
    },
    {
        'title': 'Aquaman and the Lost Kingdom',
        'release_date': 'December 20, 2023',
        'director': 'James Wan',
        'summary': 'Aquaman returns in a darker sequel, exploring new depths of the ocean and its creatures.',
        'image': 'polls/images/aquaman.jpg',  # Replace with the actual path
    },
    {
        'title': 'Rebel Moon',
        'release_date': 'December 22, 2023',
        'director': 'Zack Snyder',
        'summary': 'A peaceful colony seeks help against a brutal dictator’s army in this sci-fi epic.',
        'image': 'polls/images/rebel.jpg',  # Replace with the actual path
    },
    {
        'title': 'Ferrari',
        'release_date': 'December 25, 2023',
        'director': 'Michael Mann',
        'summary': 'The story of Enzo Ferrari, a racing legend facing personal and professional crises.',
        'image': 'polls/images/ferrari.jpg',  # Replace with the actual path
    },
    {
        'title': 'Dune: Part Two',
        'release_date': 'March 15, 2024',
        'director': 'Denis Villeneuve',
        'summary': 'The saga on Arrakis continues as Paul Atreides joins forces with the Fremen.',
        'image': 'polls/images/dune.jpg',  # Replace with the actual path
    },
    {
        'title': 'A Quiet Place: Day One',
        'release_date': 'June 8, 2024',
        'director': 'Michael Sarnoski',
        'summary': 'A spin-off from the A Quiet Place series, the plot is still under wraps but promises the same tension and drama.',
        'image': 'polls/images/place.jpg',
    }
]
    return render(request, 'polls/upcoming_movies.html', {'anticipated_movies': anticipated_movies})
