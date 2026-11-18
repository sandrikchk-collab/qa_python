import pytest

from main import BooksCollector


@pytest.fixture
def collector():
    return BooksCollector()


class TestBooksCollector:

    # пример теста из заготовки
    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize('name', ['А', 'Книга', 'К' * 39, 'К' * 40])
    def test_add_new_book_valid_name_length_added(self, collector, name):
        collector.add_new_book(name)
        assert name in collector.get_books_genre()

    @pytest.mark.parametrize('name', ['', 'К' * 41, 'К' * 50])
    def test_add_new_book_invalid_name_length_not_added(self, collector, name):
        collector.add_new_book(name)
        assert name not in collector.get_books_genre()

    def test_add_new_book_same_book_twice_added_once(self, collector):
        collector.add_new_book('Дюна')
        collector.add_new_book('Дюна')
        assert len(collector.get_books_genre()) == 1

    def test_add_new_book_new_book_has_no_genre(self, collector):
        collector.add_new_book('Дюна')
        assert collector.get_book_genre('Дюна') == ''

    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_set_book_genre_valid_genre_set(self, collector, genre):
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', genre)
        assert collector.get_book_genre('Дюна') == genre

    def test_set_book_genre_genre_not_in_list_not_set(self, collector):
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Роман')
        assert collector.get_book_genre('Дюна') == ''

    def test_set_book_genre_book_not_added_not_set(self, collector):
        collector.set_book_genre('Дюна', 'Фантастика')
        assert 'Дюна' not in collector.get_books_genre()

    def test_get_book_genre_unknown_book_returns_none(self, collector):
        assert collector.get_book_genre('Неизвестная книга') is None

    def test_get_books_with_specific_genre_returns_only_matching_books(self, collector):
        collector.add_new_book('Дюна')
        collector.add_new_book('Оно')
        collector.add_new_book('Солярис')
        collector.set_book_genre('Дюна', 'Фантастика')
        collector.set_book_genre('Оно', 'Ужасы')
        collector.set_book_genre('Солярис', 'Фантастика')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Дюна', 'Солярис']

    def test_get_books_with_specific_genre_unknown_genre_returns_empty_list(self, collector):
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        assert collector.get_books_with_specific_genre('Роман') == []

    def test_get_books_genre_returns_dict_with_books_and_genres(self, collector):
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        collector.add_new_book('Шерлок Холмс')
        assert collector.get_books_genre() == {'Дюна': 'Фантастика', 'Шерлок Холмс': ''}

    @pytest.mark.parametrize('genre', ['Фантастика', 'Мультфильмы', 'Комедии'])
    def test_get_books_for_children_genre_without_age_rating_included(self, collector, genre):
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', genre)
        assert collector.get_books_for_children() == ['Книга']

    @pytest.mark.parametrize('genre', ['Ужасы', 'Детективы'])
    def test_get_books_for_children_genre_with_age_rating_excluded(self, collector, genre):
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', genre)
        assert collector.get_books_for_children() == []

    def test_get_books_for_children_book_without_genre_excluded(self, collector):
        collector.add_new_book('Книга')
        assert collector.get_books_for_children() == []

    def test_add_book_in_favorites_book_in_dict_added(self, collector):
        collector.add_new_book('Дюна')
        collector.add_book_in_favorites('Дюна')
        assert collector.get_list_of_favorites_books() == ['Дюна']

    def test_add_book_in_favorites_book_not_in_dict_not_added(self, collector):
        collector.add_book_in_favorites('Дюна')
        assert collector.get_list_of_favorites_books() == []

    def test_add_book_in_favorites_same_book_twice_added_once(self, collector):
        collector.add_new_book('Дюна')
        collector.add_book_in_favorites('Дюна')
        collector.add_book_in_favorites('Дюна')
        assert collector.get_list_of_favorites_books() == ['Дюна']

    def test_delete_book_from_favorites_book_in_favorites_deleted(self, collector):
        collector.add_new_book('Дюна')
        collector.add_book_in_favorites('Дюна')
        collector.delete_book_from_favorites('Дюна')
        assert collector.get_list_of_favorites_books() == []

    def test_delete_book_from_favorites_book_not_in_favorites_list_unchanged(self, collector):
        collector.add_new_book('Дюна')
        collector.add_book_in_favorites('Дюна')
        collector.delete_book_from_favorites('Оно')
        assert collector.get_list_of_favorites_books() == ['Дюна']

    def test_get_list_of_favorites_books_new_collector_returns_empty_list(self, collector):
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_returns_all_favorites(self, collector):
        collector.add_new_book('Дюна')
        collector.add_new_book('Оно')
        collector.add_book_in_favorites('Дюна')
        collector.add_book_in_favorites('Оно')
        assert collector.get_list_of_favorites_books() == ['Дюна', 'Оно']
