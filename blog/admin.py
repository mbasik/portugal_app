from django.contrib import admin
from .models import Post, Comment, Place, Recommended, Dictionary

admin.site.register(Post)

class CommentAdmin(admin.ModelAdmin):
	list_display = ('user', 'email', 'approved')

admin.site.register(Comment, CommentAdmin)

class PlaceAdmin(admin.ModelAdmin):
	list1_display = ('name', 'parametr', 'text')

admin.site.register(Place, PlaceAdmin)

class RecommendedAdmin(admin.ModelAdmin):
	list2_display = ('category', 'name', 'address', 'body')

admin.site.register(Recommended, RecommendedAdmin)

class DictionaryAdmin(admin.ModelAdmin):
	list3_display = ('portuguese_word', 'polish_word', 'note')

admin.site.register(Dictionary, DictionaryAdmin)

# Register your models here.
