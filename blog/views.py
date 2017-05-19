from django.shortcuts import redirect
from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .models import Place
from .models import Recommended, Dictionary, Author
from django.shortcuts import render, get_object_or_404
from .forms import PostForm, CommentForm, PlaceForm, RecommendedForm, DictionaryForm, AuthorForm

def category_list(request):
    return render(request, 'blog/category_list.html')

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post= get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk).delete()
    return render(request, 'blog/post_delete.html', {'post': post})

def place_list(request):
    places = Place.objects.all()
    template = 'blog/place_list.html'
    context = {'places': places}
    return render(request, template, context)

def place_detail(request, pk):
    place= get_object_or_404(Place, pk=pk)
    return render(request, 'blog/place_detail.html', {'place': place})

def hostel_list(request):
    hostels = Recommended.objects.all()
    template = 'blog/hostel_list.html'
    context = {'hostels': hostels}
    return render(request, template, context)

def museum_list(request):
    museums = Recommended.objects.all()
    template = 'blog/museum_list.html'
    context = {'museums': museums}
    return render(request, template, context)

def museum_detail(request, pk):
    museum=get_object_or_404(Recommended, pk=pk)
    return render(request, 'blog/museum_detail.html', {'museum': museum})

def add_recommended(request, pk):
    city = get_object_or_404(Place, pk=pk)
    if request.method == 'POST':
        form = RecommendedForm(request.POST)
        if form.is_valid():
            recommended= form.save(commit=False)
            recommended.city = city 
            recommended.save()
            return redirect('place_detail', pk=pk)
    else:
        form = RecommendedForm()
        template = 'blog/add_recommended.html'
        context = {'form': form}
        return render(request, template, context)

def recommended_delete(request, pk):
    recommended = get_object_or_404(Recommended, pk=pk).delete()
    return render(request, 'blog/recommended_delete.html', {'recommended': recommended})

def restaurante_list(request):
    restaurantes = Recommended.objects.all()
    template = 'blog/restaurante_list.html'
    context = {'restaurantes': restaurantes}
    return render(request, template, context)

def restaurante_detail(request, pk):
    restaurante=get_object_or_404(Recommended, pk=pk)
    return render(request, 'blog/restaurante_detail.html', {'restaurante': restaurante})

def hostel_detail(request, pk):
    hostel=get_object_or_404(Recommended, pk=pk)
    return render(request, 'blog/hostel_detail.html', {'hostel': hostel})


def place_new(request):
    if request.method == "POST":
        form = PlaceForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            place=form.save()
            return redirect('place_detail', pk=place.pk)
    else:
        form = PlaceForm()
    return render(request, 'blog/place_edit.html', {'form': form}) 

def place_delete(request, pk):
    place = get_object_or_404(Place, pk=pk).delete()
    return render(request, 'blog/place_delete.html', {'place': place})


def place_edit(request, pk):
    place = get_object_or_404(Place, pk=pk)
    if request.method == "POST":
        form = PlaceForm(request.POST, request.FILES or None, instance=place)
        if form.is_valid():
            place = form.save(commit=False)
            place.save()
            return redirect('place_detail', pk=place.pk)
    else:
        form = PlaceForm(instance=place)
    return render(request, 'blog/place_edit.html', {'form': form})


def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment= form.save(commit=False)
            comment.post = post 
            comment.save()
            return redirect('post_detail', pk=pk)
    else:
        form = CommentForm()
        template = 'blog/add_comment.html'
        context = {'form': form}
        return render(request, template, context)

def words_list(request):
    words = Dictionary.objects.all()
    query= request.GET.get('q')
    if query:
        words = words.filter(portuguese_word=query)
    return render(request, 'blog/dictionary_portuguese.html', {'words': words})

def words_list2(request):
    words = Dictionary.objects.all()
    query= request.GET.get('q')
    if query:
        words = words.filter(polish_word=query)
    return render(request, 'blog/dictionary_polish.html', {'words': words})

def word_new(request):
    if request.method == "POST":
        form = DictionaryForm(request.POST)
        if form.is_valid():
            dictionary = form.save()
            return redirect('word_translation', pk=dictionary.pk)
    else:
        form = DictionaryForm()
        return render(request, 'blog/word_edit.html', {'form': form})

def word_edit(request, pk):
    word = get_object_or_404(Dictionary, pk=pk)
    if request.method == "POST":
        form = DictionaryForm(request.POST, request.FILES or None)
        if form.is_valid():
            word = form.save(commit=False)
            word.save()
            return redirect('word_translation', pk=word.pk)
    else:
        form = DictionaryForm()
    return render(request, 'blog/word_edit.html', {'form': form})

def word_delete(request, pk):
    word= get_object_or_404(Dictionary, pk=pk).delete()
    return render(request, 'blog/word_delete.html', {'word': word})


def word_translation(request,pk):
    word = get_object_or_404(Dictionary, pk=pk)
    return render(request, 'blog/word_translation.html', {'word': word})


def author(request):
    author= Author.objects.all()
    return render(request, 'blog/author.html', {'author': author})

def add_author(request):
    if request.method =="POST":
        form = AuthorForm(request.POST or None)
        if form.is_valid():
            author = form.save()
            return redirect('author_detail', pk=author.pk)
    else:
        form = AuthorForm()
    return render(request, 'blog/add_author.html', {'form': form})

