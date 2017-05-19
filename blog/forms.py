from django import forms
from .models import Post
from .models import Comment 
from .models import Place
from .models import Recommended
from .models import Dictionary
from .models import Author

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('user', 'email', 'body')

class PlaceForm(forms.ModelForm):
	class Meta:
		model = Place
		fields = ('name', 'parametr', 'text', 'image')

class RecommendedForm(forms.ModelForm):
	class Meta:
		model = Recommended
		fields = ('category', 'name', 'address', 'body')

class DictionaryForm(forms.ModelForm):
	
	class Meta:
		model = Dictionary
		fields = ('portuguese_word', 'polish_word', 'note')

class AuthorForm(forms.ModelForm):
	
	class Meta:
		model = Author
		fields = ('name', 'email', 'about')

