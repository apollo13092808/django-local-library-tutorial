import uuid
from datetime import date

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse  # To generate URLS by reversing URL patterns
from django.utils import timezone


# Create your models here.
class Genre(models.Model):
    """Model representing a book genre."""
    name = models.CharField(max_length=100, help_text='Enter a book genre (e.g. Science Fiction)')

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return f"{self.name}"


class Language(models.Model):
    """Model representing a Language (e.g. English, French, Japanese, etc.)"""
    name = models.CharField(max_length=100,
                            help_text="Enter the book's natural language (e.g. English, French, Japanese etc.)")

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return f"{self.name}"


class Author(models.Model):
    """Model representing an author."""
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=20)
    pen_name = models.CharField(max_length=100, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True, verbose_name='Born')
    date_of_death = models.DateField(null=True, blank=True, verbose_name='Died')

    class Meta:
        ordering = ['first_name', 'last_name']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse(viewname='author_detail', args=[str(self.pk)])

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return f"{self.pen_name}"


class Book(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    # book can only have one author, but authors can have multiple books
    author = models.ForeignKey(to=Author, on_delete=models.SET_NULL, null=True)

    # a genre can contain many books and a book can cover many genres
    genre = models.ManyToManyField(to=Genre, help_text="Select a genre for this book")

    language = models.ForeignKey(to=Language, on_delete=models.SET_NULL, null=True)

    help_text_isbn_link = '<a href="https://www.isbn-international.org/content/isbn-standard">ISBN number</a>'
    isbn = models.CharField(max_length=15, unique=True, verbose_name='ISBN',
                            help_text=f'13 Character {help_text_isbn_link}')

    title = models.CharField(max_length=200)
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')

    class Meta:
        ordering = ['title', 'author']

    def display_genre(self):
        """Creates a string for the Genre. This is to display genre in Admin."""
        return ', '.join([genre.name for genre in self.genre.all()[:3]])

    display_genre.short_description = 'Genre'

    def get_absolute_url(self):
        """Returns the url to access a particular book instance."""
        return reverse(viewname='book_detail', args=[str(self.pk)])

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return f"{self.title}"


class BookInstance(models.Model):
    """Model representing a specific copy of a book (i.e. that can be borrowed from the library)."""
    id = models.UUIDField(verbose_name='ID', default=uuid.uuid4, primary_key=True,
                          help_text='Unique ID for this particular book across whole library')
    book = models.ForeignKey(to=Book, on_delete=models.RESTRICT, null=True)
    borrower = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, blank=True)
    publisher = models.CharField(max_length=200)
    date_published = models.DateField(null=True, blank=True)
    due_back = models.DateField(default=date.today(), null=True, blank=True)

    STATUS_CHOICES = (
        ('maintenance', 'Maintenance'),
        ('loan', 'On loan'),
        ('available', 'Available'),
        ('reserved', 'Reserved'),
    )
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default="available", help_text='Book availability')

    class Meta:
        verbose_name_plural = 'Book Instances'
        ordering = ['due_back']
        permissions = (('can_mark_returned', 'Set book as returned'),)

    @property
    def is_overdue(self):
        """Determines if the book is overdue based on due date and current date."""
        return bool(self.due_back and date.today() > self.due_back)

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return f"{self.id} {self.book.title}"
