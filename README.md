# qa_python — тесты для BooksCollector

Юнит-тесты на pytest для класса `BooksCollector` (`main.py`). Тесты находятся в `tests.py`.

Запуск:

```
pytest -v tests.py
```

## Реализованные тесты

Для создания нового экземпляра `BooksCollector` перед каждым тестом используется фикстура `collector`.

### add_new_book
- `test_add_new_book_add_two_books` — две разные книги добавляются в словарь.
- `test_add_new_book_valid_name_length_added` *(параметризован)* — названия длиной 1, 5, 39 и 40 символов добавляются.
- `test_add_new_book_invalid_name_length_not_added` *(параметризован)* — пустое название и названия длиннее 40 символов не добавляются.
- `test_add_new_book_same_book_twice_added_once` — одну и ту же книгу нельзя добавить дважды.
- `test_add_new_book_new_book_has_no_genre` — у новой книги нет жанра.

### set_book_genre
- `test_set_book_genre_valid_genre_set` *(параметризован)* — устанавливается любой жанр из списка `genre`.
- `test_set_book_genre_genre_not_in_list_not_set` — жанр не из списка не устанавливается.
- `test_set_book_genre_book_not_added_not_set` — жанр нельзя установить книге, которой нет в словаре.

### get_book_genre
- `test_get_book_genre_unknown_book_returns_none` — для неизвестной книги возвращается `None`.

### get_books_with_specific_genre
- `test_get_books_with_specific_genre_returns_only_matching_books` — возвращаются только книги указанного жанра.
- `test_get_books_with_specific_genre_unknown_genre_returns_empty_list` — для жанра не из списка возвращается пустой список.

### get_books_genre
- `test_get_books_genre_returns_dict_with_books_and_genres` — возвращается словарь «книга: жанр».

### get_books_for_children
- `test_get_books_for_children_genre_without_age_rating_included` *(параметризован)* — книги жанров без возрастного рейтинга попадают в список.
- `test_get_books_for_children_genre_with_age_rating_excluded` *(параметризован)* — книги жанров «Ужасы» и «Детективы» в список не попадают.
- `test_get_books_for_children_book_without_genre_excluded` — книга без жанра в список не попадает.

### add_book_in_favorites
- `test_add_book_in_favorites_book_in_dict_added` — книга из словаря добавляется в избранное.
- `test_add_book_in_favorites_book_not_in_dict_not_added` — книгу, которой нет в словаре, нельзя добавить в избранное.
- `test_add_book_in_favorites_same_book_twice_added_once` — одну и ту же книгу нельзя добавить в избранное дважды.

### delete_book_from_favorites
- `test_delete_book_from_favorites_book_in_favorites_deleted` — книга удаляется из избранного.
- `test_delete_book_from_favorites_book_not_in_favorites_list_unchanged` — если книги нет в избранном, список не меняется.

### get_list_of_favorites_books
- `test_get_list_of_favorites_books_new_collector_returns_empty_list` — у нового коллекционера список избранного пуст.
- `test_get_list_of_favorites_books_returns_all_favorites` — возвращаются все книги из избранного.
