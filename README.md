# qa_python
1. test_add_new_book_add_two_books - проверяет добавление двух книг в коллекцию
2. test_add_new_book_valid_name_added - проверяет добавление книги с допустимым названием
3. test_add_new_book_name_too_long_not_added - проверяет, что книга с названием длиннее 40 символов не добавляется
4. test_add_new_book_empty_name_not_added - проверяет, что книга с пустым названием не добавляется
5. test_add_new_book_duplicate_not_added - проверяет, что нельзя добавить одну книгу дважды
6. test_set_book_genre_valid_genre_set - проверяет установку корректного жанра для книги
7. test_set_book_genre_invalid_genre_not_set - проверяет, что нельзя установить несуществующий жанр
8. test_get_books_with_specific_genre_returns_correct_books - проверяет получение книг по конкретному жанру
9. test_get_books_for_children_excludes_age_rated_books - проверяет, что книги с возрастным рейтингом не попадают в детский список
10. test_add_and_remove_from_favorites - проверяет добавление и удаление книг из избранного
11. test_add_to_favorites_only_books_from_collection - проверяет, что в избранное можно добавлять только книги из коллекции