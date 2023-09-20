from django.urls import path

from catalog import views

urlpatterns = [
    path('', views.index, name='index'),

    path('books/', views.BookListView.as_view(), name='books'),
    path('book-detail/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author-detail/<int:pk>/', views.AuthorDetailView.as_view(), name='author_detail'),

    path('all-borrowed-books/', views.LoanedBooksByAllListView.as_view(), name='all_borrowed'),
    path('my-borrowed-books/', views.LoanedBooksByUserListView.as_view(), name='my_borrowed'),

    path('book/<uuid:pk>/renew/', views.renew_book, name='renew_book'),

    path('book/create/', views.BookCreate.as_view(), name='create_book'),
    path('book/<int:pk>/update/', views.BookUpdate.as_view(), name='update_book'),
    path('book/<int:pk>/delete/', views.BookDelete.as_view(), name='delete_book'),

    path('author/create/', views.AuthorCreate.as_view(), name='create_author'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='update_author'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='delete_author'),
]
