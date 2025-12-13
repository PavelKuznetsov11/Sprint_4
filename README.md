# qa_python

test_add_new_book_add_two_books_is_added - добавляет две книги
test_two_books_is_not_added - 1 тест(длина имени больше 41 символа не добавляет книги), 2 тест(длина имени 0 символов не добавляет книги)
test_add_book_existing_book_is_not_added - не добавляет книгу с уже существующей, заданный жанр не сменился на 0 символов

test_set_book_genre_existing_book_genre_is_set - у существующей книги установлен нужный жанр
test_set_book_genre_absent_name_book_genre_is_not_set - у несуществующей книги жанр не установлен
test_set_book_genre_absent_genre_is_not_set - у книги не установлен недопустимый жанр

test_get_book_genre_one_book_genre_get - получен жанр одной книги

test_get_books_with_specific_genre_get_list_with_two_books - получен список из двух книг с указанным жанром 
test_get_books_with_specific_genre_not_found_books - список книг с указанным жанром не найден
test_get_books_with_specific_genre_get_empty_list_book - 1 тест(книга не была добавлена и книга не найдена), 2 тест(указан недопустимый жанр и книга не найдена)

test_get_books_genre_get_list_two_books - получен словарь с названием и жанром книг

test_get_books_for_children_get_one_book - получено названии книги для детей
test_get_books_for_children_not_found_book - 1 тест(указан жанр не для детей, книга для детей не найдена), 2 тест(указан недопустимый жанр, книга для детей не найдена)

test_add_book_in_favorites_add_one_book_is_added - добавлена книга в список favorites
test_add_book_in_favorites_existing_book_favorites_is_not_added - книга уже существует в списке favorites, поэтому не добавляется
test_add_book_in_favorites_absent_book_is_not_added_favorites - книга не была добавлена, не добавляется в список favorites

test_delete_book_from_favorites_delete_one_book - удаляет книгу из списка favorites
test_delete_book_from_favorites_delete_absent_book_favorites - попытка удаления книги из списка favorites, которая не была добавлена ранее

test_get_list_of_favorites_books_get__books - получает список из двух книг добавленных в список favorites
