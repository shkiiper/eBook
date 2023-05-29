from rest_framework import permissions

from book.models import Book


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Пользователь может редактировать или удалять объекты только, если он является автором.
    Для остальных пользователей доступ только на чтение.
    """

    def has_object_permission(self, request, view, obj):
        # Разрешить все методы HTTP только для чтения (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True

        # Разрешить редактирование или удаление только авторам
        return obj.author == request.user


class IsAuthorOrReadOnlyForBookPages(permissions.BasePermission):
    """
    Пользователь может создавать страницы только для своих книг,
    но может просматривать страницы всех книг.
    """

    def has_permission(self, request, view):
        # Разрешить только чтение для всех пользователей
        if request.method in permissions.SAFE_METHODS:
            return True

        # Разрешить создание страницы только авторам
        book_id = request.data.get('book', None)
        if book_id:
            book = Book.objects.get(pk=book_id)
            return book.author == request.user

        return False
