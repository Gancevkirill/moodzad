# 1
# def read_end(lines, file):
#     if not isinstance(lines, int) or lines <= 0:
#         print("Пожалуйста, укажите положительное целое число для параметра lines.")
#         return
#     try:
#         with open(file, 'r', encoding='utf-8') as f:
#             all_lines = f.readlines()
#             last_lines = all_lines[-lines:]
#             for line in last_lines:
#                 print(line, end='')
#     except FileNotFoundError:
#         print(f"Файл {file} не найден.")
#     except Exception as e:
#         print(f"Произошла ошибка при чтении файла: {e}")
# read_end(3, 'article.txt')
# 2
# def print_reps(directory):
#     try:
#         print(f"Содержимое директории {directory}:")
#         for item in os.listdir(directory):
#             item_path = os.path.join(directory, item)
#             if os.path.isfile(item_path):
#                 print(f"Файл: {item}")
#             elif os.path.isdir(item_path):
#                 print(f"Папка: {item}")
#                 print_reps(item_path)
#     except FileNotFoundError:
#         print(f"Директория {directory} не найдена")
#     except PermissionError:
#         print(f"Нет доступа к директории {directory}.")
#     except Exception as e:
#         print(f"Произошла ошибка: {e}")
# print_reps('путь_к_вашей_папке/venv')
# 3
# def longest_words(file):
#     try:
#         with open(file, 'r', encoding='utf-8') as f:
#             text = f.read()
#             words = text.split()
#             max_length = max(len(word) for word in words)
#             longest_words_list = [word for word in words if len(word) == max_length]
#             if len(longest_words_list) == 1:
#                 print(f"Самое длинное слово: {longest_words_list[0]}")
#             elif len(longest_words_list) > 1:
#                 print("Самые длинные слова:")
#                 for word in longest_words_list:
#                     print(word)
#             else:
#                 print("Файл не содержит слов")
#     except FileNotFoundError:
#         print(f"Файл {file} не найден")
#     except Exception as e:
#         print(f"Произошла ошибка при чтении файла: {e}")
# longest_words('путь_к_вашему_файлу/poem.txt')
# 4
# def text_statistics(file_name):
#     try:
#         with open(file_name, 'r', encoding='utf-8') as file:
#             content = file.read()
#
#             letter_count = sum(1 for char in content if char.isalpha() and char.isascii())
#
#             word_count = len(content.split())
#
#             line_count = content.count('\n') + 1
#
#             print(f"Input file contains:")
#             print(f"{letter_count} letters")
#             print(f"{word_count} words")
#             print(f"{line_count} lines")
#
#     except FileNotFoundError:
#         print(f"File {file_name} not found.")
#     except Exception as e:
#         print(f"An error occurred: {e}")
#
# text_statistics('file.txt')