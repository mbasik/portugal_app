from django.db import models
from django.utils import timezone

class Category(models.Model):
		name = models.CharField(max_length=100)

		def __str__(self):
			return self.name

class Post(models.Model):
		author = models.ForeignKey('auth.User')
		title = models.CharField(max_length=200)
		text = models.TextField()
		created_date = models.DateTimeField(
			default=timezone.now)
		published_date = models.DateTimeField(
			blank=True, null=True)

		def publish(self):
			self.published_date = timezone.now()
			self.save()

		def __str__(self):
			return self.title

class Comment(models.Model):
		post = models.ForeignKey(Post, related_name='comments')
		user = models.CharField(max_length=250)
		email = models.EmailField()
		body = models.TextField()
		created = models.DateTimeField(auto_now_add=True)
		approved = models.BooleanField(default=False)

		def approved(self):
			self.approved=True
			self.save()

		def __str__(self):
			return self.user

class Place(models.Model):
		name = models.CharField(max_length=200)
		parametr = models.CharField(max_length=30)
		text = models.TextField()
		image = models.FileField(null=True, blank=True)

		def __str__(self):
			return self.name

class Recommended(models.Model):
		city = models.ForeignKey(Place, related_name='recommendeds')
		category = models.CharField(max_length=250)
		name = models.CharField(max_length=200)
		address = models.CharField(max_length=200)
		body = models.TextField()

		def __str__(self):
			return self.name

class Dictionary(models.Model):
		portuguese_word = models.CharField(max_length=50)
		polish_word = models.CharField(max_length=50)
		note = models.TextField(null=True, blank=True)

		def __str__(self):
			return self.portuguese_word

class Author(models.Model):
		name= models.CharField(max_length=50)
		email= models.EmailField()
		about = models.TextField()

		def __str__(self):
			return self.name


# Create your models here.
