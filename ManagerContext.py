"""Program describes own manager context"""

import time
import random

# Class describes own manager context, which define a duration of code executing
class CodeTimer:
  def __init__(self, note):
    self.note = note
    self.begin_time = time.time()

  def __enter__(self):
    return self

  def __exit__(self, exc_type, exc_val, exc_tb):
    self.end_time = time.time()
    print(f"{self.note} is {self.end_time - self.begin_time}.")


def create_random_file(filename, count_values=1000):
  """

  (string, int) -> None

  Function generates file <count_values> random integer values

  """

  counter = 0
  try:
    with open(filename, 'w', encoding="utf8") as file:
      while counter < count_values:
        file.write(str(random.randint(0, 99999)) + "\n")
        counter += 1
    return 0
  except PermissionError:
    print("Не хватает прав для создания файла.")
    return -1

def write_list_to_file(filename, values):
  """

  (string, list) -> int

  Function writes values of list to text file

  """
  try:
    with open(filename, 'w', encoding="utf8") as file:
      for i in values:
        file.write(str(i) + "\n")
    return 0
  except PermissionError:
    print("Не хватает прав для создания файла.")
    return -1

def read_file_to_list(filename):
  """

  (string) -> list or None

  Function read file to list

  """

  try:
    with open(filename, 'r', encoding="utf8") as file:
      values = [int(i.strip()) for i in file]
    return values
  except FileNotFoundError:
    print(f"Файл \"{filename}\" не найден.")

def sorting_list_method1(values):
  """

  (list) -> None

  Function sorting list used method #1

  """

  while True:
    found = False
    for i in range(0, len(values) - 1):
      if values[i] > values[i + 1]:
        values[i], values[i + 1] = values[i + 1], values[i]
        found = True

    if not found:
      break

def sorting_list_method2(values):
  """

  (list) -> list

  Function sorting list used method #2

  """

  values_result = []
  while True:
    if len(values) <= 0:
      break
    a = min(values)
    values_result.append(a)
    values.remove(a)

  return values_result

def print_captionlist(caption, values):
  """

  (list) -> list

  Function prints list with caption

  """

  print(caption)
  print(values, end="\n\n")

def main():
  """

  (None) -> None

  Main function describe main functionality

  """

  filename = "data.txt"
  count_values = 7000

  if create_random_file(filename, count_values) != 0:
    return

  with CodeTimer("Time reading list from file") as context:
    values = read_file_to_list(filename)
  if values == None:
    return
  print_captionlist("Source list: ", values)

  values_copy = values.copy()
  with CodeTimer("Time of inner sorting list") as context:
    values_copy.sort()
  print_captionlist("Sorted list: ", values_copy)

  values_copy = values.copy()
  with CodeTimer("Time of my sorting method №1 list") as context:
    sorting_list_method1(values_copy)
  print_captionlist("Sorted list: ", values_copy)

  values_copy = values.copy()
  with CodeTimer("Time of my sorting method №2 list") as context:
    values_result = sorting_list_method2(values_copy)
  print_captionlist("Sorted list: ", values_result)

  with CodeTimer("Time writing list to file") as context:
    write_list_to_file(filename, values_result)

# Point of enter to program
main()
