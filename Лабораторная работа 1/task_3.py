diskette_capacity_bytes = 1.44 * 1024 * 1024

pages_per_book = 100
lines_per_page = 50
characters_per_line = 25
bytes_per_character = 4

bytes_per_page = lines_per_page * characters_per_line * bytes_per_character

bytes_per_book = pages_per_book * bytes_per_page

num_books_on_diskette = int(diskette_capacity_bytes // bytes_per_book)

print("Количество книг, помещающихся на дискету:", num_books_on_diskette)
