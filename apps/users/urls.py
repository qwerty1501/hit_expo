from django.urls import path

from .views import UserMVS, UserSMIViewSet, CustomTokenRefreshView, UserLoginView, CurrentUserView , BookListCreateView, BookRetrieveUpdateDeleteView, BookSearchView

userPlural = {
    'get': 'list',
    'post': 'create'
}

useSingle = {
    'get': 'retrieve',
    'patch': 'update'
}

useSingle2 = {
    'get': 'retrieve',
    'post': 'create',
}

useSingle3 = {
    'get': 'retrieve',
    'patch': 'update',
    'post': 'create',
    'delete': 'destroy'
}

urlpatterns = [
    path('user/', UserMVS.as_view(userPlural)),
    path('user/<uuid:uniqueId>/', UserMVS.as_view(useSingle)),

    path('user-smi/', UserSMIViewSet.as_view(userPlural)),
    path('user-smi/<uuid:uniqueId>/', UserSMIViewSet.as_view(useSingle)),

    path('profile/', CurrentUserView.as_view()),

    path('check/', CustomTokenRefreshView.as_view()),

    path('login/', UserLoginView.as_view()),
    
    
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDeleteView.as_view(), name='book-retrieve-update-delete'),
    path('books/search/', BookSearchView.as_view(), name='book-search'),
]
