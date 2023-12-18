from main import BooksCollector
import pytest

class TestBooksCollector:
    @pytest.mark.parametrize('book', ['О дивный новый мир', 'Убийство в «Восточном экспрессе»', 'Горе от ума'])
    def test_add_new_book_add_book(self, book):
        collector = BooksCollector()

        collector.add_new_book(book)
        assert collector.get_book_genre(book) == ''

    def test_set_book_genre_for_three_books(self):
        collector = BooksCollector()

        collector.add_new_book('О дивный новый мир')
        collector.add_new_book('Убийство в «Восточном экспрессе»')
        collector.add_new_book('Горе от ума')
        collector.set_book_genre('О дивный новый мир','Фантастика')
        collector.set_book_genre('Убийство в «Восточном экспрессе»','Детективы')
        collector.set_book_genre('Горе от ума','Комедии')

        assert collector.get_book_genre('О дивный новый мир') == 'Фантастика' and collector.get_book_genre('Убийство в «Восточном экспрессе»') == 'Детективы' and collector.get_book_genre('Горе от ума') == 'Комедии'


    def test_get_books_with_specific_genre_for_three_books(self):
        collector = BooksCollector()

        collector.add_new_book('О дивный новый мир')
        collector.add_new_book('Алиса в стране чудес')
        collector.add_new_book('Горе от ума')
        collector.set_book_genre('О дивный новый мир', 'Фантастика')
        collector.set_book_genre('Алиса в стране чудес', 'Фантастика')
        collector.set_book_genre('Горе от ума', 'Комедии')

        assert collector.get_books_with_specific_genre('Фантастика') == ['О дивный новый мир', 'Алиса в стране чудес']


    def test_get_books_with_specific_genre_for_three_books_empty_list(self):
        collector = BooksCollector()

        collector.add_new_book('О дивный новый мир')
        collector.add_new_book('Алиса в стране чудес')
        collector.add_new_book('Горе от ума')
        collector.set_book_genre('О дивный новый мир', 'Фантастика')
        collector.set_book_genre('Алиса в стране чудес', 'Фантастика')
        collector.set_book_genre('Горе от ума', 'Комедии')

        assert collector.get_books_with_specific_genre('Мультфильмы') == []


    def test_get_books_genre_for_book(self):
        collector = BooksCollector()

        collector.add_new_book('О дивный новый мир')
        collector.set_book_genre('О дивный новый мир', 'Фантастика')

        assert collector.get_books_genre() == {'О дивный новый мир': 'Фантастика'}


    def test_get_books_for_children_for_three_books(self):
        collector = BooksCollector()

        collector.add_new_book('О дивный новый мир')
        collector.add_new_book('Убийство в «Восточном экспрессе»')
        collector.add_new_book('Горе от ума')
        collector.set_book_genre('О дивный новый мир', 'Фантастика')
        collector.set_book_genre('Убийство в «Восточном экспрессе»', 'Детективы')
        collector.set_book_genre('Горе от ума', 'Комедии')

        assert collector.get_books_for_children() == ['О дивный новый мир', 'Горе от ума']


    def test_add_book_in_favorites_for_book(self):
        collector = BooksCollector()

        collector.add_new_book('Убийство в «Восточном экспрессе»')
        collector.add_book_in_favorites('Убийство в «Восточном экспрессе»')

        assert collector.get_list_of_favorites_books() == ['Убийство в «Восточном экспрессе»']


    def test_add_book_in_favorites_for_book_already_exist(self):
        collector = BooksCollector()

        collector.add_new_book('Убийство в «Восточном экспрессе»')

        collector.add_book_in_favorites('Убийство в «Восточном экспрессе»')

        collector.add_book_in_favorites('Убийство в «Восточном экспрессе»')

        assert collector.get_list_of_favorites_books() == ['Убийство в «Восточном экспрессе»']


    def test_delete_book_from_favorites_for_book(self):
        collector = BooksCollector()

        collector.add_new_book('Убийство в «Восточном экспрессе»')
        collector.add_book_in_favorites('Убийство в «Восточном экспрессе»')
        collector.delete_book_from_favorites('Убийство в «Восточном экспрессе»')

        assert collector.get_list_of_favorites_books() == []








