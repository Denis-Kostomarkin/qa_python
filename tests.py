from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    def test_add_new_book_valid_name_added(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        assert 'Война и мир' in collector.get_books_genre()
        assert collector.get_book_genre('Война и мир') == ''

    def test_add_new_book_name_too_long_not_added(self):
        collector = BooksCollector()
        long_name = 'О' * 41
        collector.add_new_book(long_name)
        assert long_name not in collector.get_books_genre()

    def test_add_new_book_empty_name_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('')
        assert '' not in collector.get_books_genre()

    def test_add_new_book_duplicate_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('Преступление и наказание')
        collector.add_new_book('Преступление и наказание')
        books = collector.get_books_genre()
        assert list(books.keys()).count('Преступление и наказание') == 1

    def test_set_book_genre_valid_genre_set(self):
        collector = BooksCollector()
        collector.add_new_book('Мастер и Маргарита')
        collector.set_book_genre('Мастер и Маргарита', 'Фантастика')
        assert collector.get_book_genre('Мастер и Маргарита') == 'Фантастика'

    def test_set_book_genre_invalid_genre_not_set(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Несуществующий жанр')
        assert collector.get_book_genre('1984') == ''

    def test_get_books_with_specific_genre_returns_correct_books(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')
        collector.set_book_genre('Книга 1', 'Фантастика')
        collector.set_book_genre('Книга 2', 'Комедии')
        
        fantasy_books = collector.get_books_with_specific_genre('Фантастика')
        assert 'Книга 1' in fantasy_books
        assert 'Книга 2' not in fantasy_books

    def test_get_books_for_children_excludes_age_rated_books(self):
        collector = BooksCollector()
        collector.add_new_book('Детская книга')
        collector.add_new_book('Страшная книга')
        collector.set_book_genre('Детская книга', 'Мультфильмы')
        collector.set_book_genre('Страшная книга', 'Ужасы')
        
        children_books = collector.get_books_for_children()
        assert 'Детская книга' in children_books
        assert 'Страшная книга' not in children_books

    def test_add_and_remove_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Избранная книга')
        collector.add_book_in_favorites('Избранная книга')
        assert 'Избранная книга' in collector.get_list_of_favorites_books()
        
        collector.delete_book_from_favorites('Избранная книга')
        assert 'Избранная книга' not in collector.get_list_of_favorites_books()

    def test_add_to_favorites_only_books_from_collection(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Несуществующая книга')
        assert 'Несуществующая книга' not in collector.get_list_of_favorites_books()