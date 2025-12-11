import pytest
from main import BooksCollector


class TestBooksCollector:


    def test_add_new_book_add_two_books_is_added(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.books_genre) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    add_books_negative_tests = [
        ['Как завоевывать друзей и оказывать влияние на людей',
          'Путеводитель для путешествующих автостопом по Галактике'],
        ['', '']
    ]
    @pytest.mark.parametrize("book_name1, book_name2", add_books_negative_tests)
    def test_two_books_is_not_added(self, book_name1, book_name2):
        collector = BooksCollector()

        collector.add_new_book(book_name1)
        collector.add_new_book(book_name2)

        assert len(collector.books_genre) == 0

    def test_add_book_existing_book_is_not_added(self):
        collector = BooksCollector()

        name_book = 'Противостояние'
        genre = 'Фантастика'
        collector.add_new_book(name_book)
        collector.set_book_genre(name_book, genre)
        collector.add_new_book(name_book)

        assert collector.books_genre.get(name_book) == genre



    def test_set_book_genre_existing_book_genre_is_set(self):
        collector = BooksCollector()
        name_book = 'Тёмные начала'
        genre = 'Фантастика'
        collector.add_new_book(name_book)
        collector.set_book_genre(name_book, genre)

        assert collector.books_genre.get(name_book) == genre


    def test_set_book_genre_absent_name_book_genre_is_not_set(self):
        collector = BooksCollector()

        name_book = 'Убийство на улице Морг'
        genre = 'Детективы'

        collector.set_book_genre(name_book, genre)

        assert collector.books_genre.get(name_book) == None

    def test_set_book_genre_absent_genre_is_not_set(self):
        collector = BooksCollector()

        name_book = 'Унесённые ветром' 
        genre = 'Роман-эпопея'
        collector.add_new_book(name_book)
        collector.set_book_genre(name_book, genre)

        assert collector.books_genre.get(name_book) == ''


    
    def test_get_book_genre_one_book_genre_get(self):
        collector = BooksCollector()

        name_book = 'Таинственный сад'
        genre = 'Мультфильмы'
        collector.add_new_book(name_book)
        collector.set_book_genre(name_book, genre)

        assert collector.get_book_genre(name_book) == genre


    
    def test_get_books_with_specific_genre_get_list_with_two_books(self):
        collector = BooksCollector()

        name_book = ['Золотая тетрадь', 'Повелитель мух', 'Поющие в терновнике']
        genre = ['Мультфильмы', 'Ужасы', 'Мультфильмы']

        for i in range(len(name_book)):
            collector.add_new_book(name_book[i])
            collector.set_book_genre(name_book[i], genre[i])

        assert len(collector.get_books_with_specific_genre(genre[0])) == 2

    def test_get_books_with_specific_genre_not_found_books(self):
        collector = BooksCollector()

        name_book = 'Песнь Соломона'
        genre = 'Комедии'
        collector.add_new_book(name_book)
        collector.set_book_genre(name_book, genre)

        assert len(collector.get_books_with_specific_genre('Ужасы')) == 0

    books_with_specific_genre_negative = [
        ['', 'Ужасы'],
        ['Широкое Саргассово море', 'Роман']
    ]
    @pytest.mark.parametrize('name_book, genre', books_with_specific_genre_negative)
    def test_get_books_with_specific_genre_get_empty_list_book(self, name_book, genre):
        collector = BooksCollector()

        collector.add_new_book(name_book)
        collector.set_book_genre(name_book, genre)

        assert collector.get_books_with_specific_genre(genre) == []


    
    def test_get_books_genre_get_dict_two_books(self):
        collector = BooksCollector()

        name_book = {'Аня из Зелёных Мезонинов': '', 'Чарли и шоколадная фабрика': ''}
                     
        for i in name_book.keys():
            collector.add_new_book(i)

        assert collector.get_books_genre() == name_book

    

    def test_get_books_for_children_get_one_book(self):
        collector = BooksCollector()

        name_book = 'Хоббит, или Туда и обратно'
        genre = 'Мультфильмы'

        collector.add_new_book(name_book)
        collector.set_book_genre(name_book, genre)

        assert collector.get_books_for_children() == [name_book]


    books_for_children_negative = [
        ['Алиса в Стране чудес', 'Детективы'],
        ['Остров сокровищ', 'Приключенческий роман']
    ]
    @pytest.mark.parametrize('name_book, genre', books_for_children_negative)
    def test_get_books_for_children_not_found_book(self, name_book, genre):
        collector = BooksCollector()

        collector.add_new_book(name_book)
        collector.set_book_genre(name_book, genre)

        assert collector.get_books_for_children() == []



    def test_add_book_in_favorites_add_one_book_is_added(self):
        collector = BooksCollector()

        name_book = ['Лев, колдунья и платяной шкаф', 'Дюна']

        for i in range(len(name_book)):
            collector.add_new_book(name_book[i])
            
        collector.add_book_in_favorites(name_book[0])

        assert collector.favorites[0] == name_book[0]

    def test_add_book_in_favorites_existing_book_favorites_is_not_added(self):
        collector = BooksCollector()

        name_book = ['Рождественская песнь', 'Рождественская песнь']

        for i in range(len(name_book)):
            collector.add_new_book(name_book[i])
            
        for i in range(len(name_book)):
            collector.add_book_in_favorites(name_book[i])

        assert len(collector.favorites) == 1


    def test_add_book_in_favorites_absent_book_is_not_added_favorites(self):
        collector = BooksCollector()

        name_book = 'Преступление и наказание'

        collector.add_book_in_favorites(name_book)

        assert len(collector.favorites) == 0

    def test_delete_book_from_favorites_delete_one_book(self):
        collector = BooksCollector()    

        name_book = 'Великий Гэтсби'

        collector.add_new_book(name_book)
        collector.add_book_in_favorites(name_book)
        collector.delete_book_from_favorites(name_book)        
            
        assert collector.favorites == []

    def test_delete_book_from_favorites_delete_absent_book_favorites(self):
        collector = BooksCollector()    

        name_book = 'Спокойной ночи, мистер Том'

        collector.add_new_book(name_book)
        collector.add_book_in_favorites(name_book)
        collector.delete_book_from_favorites('Граф Монте-Кристо')        
            
        assert collector.favorites == [name_book]

    def test_get_list_of_favorites_books_get__books(self):
        collector = BooksCollector()

        name_book = ['Вдали от обезумевшей толпы', 'О мышах и людях', 'Возвращение в Брайдсхед']

        for i in range(len(name_book)):
            collector.add_new_book(name_book[i])
            
        for i in range(len(name_book) - 1):
            collector.add_book_in_favorites(name_book[i])

        assert len(collector.get_list_of_favorites_books()) == 2
