def open_book(path):
  file_contents = get_text(path)
  words = file_contents.split()
  word_count = len(words)
  character_dict = count_characters(words)
  character_list = convert_to_list(character_dict)
  generate_report(path, word_count, character_list)


def sort_on(dict):
  return dict["num"]

def convert_to_list(dict):
  output_list = []
  for item in dict:
    output_list.append({"name": item, "num": dict[item]})

  return output_list

def count_characters(words):
  count_dict = {}
  for word in words:
    word = word.lower()
    for character in word:
      if character.isalpha():
        if character in count_dict:
          count_dict[character] += 1
        else:
          count_dict[character] = 1
  return count_dict

def generate_report(path, word_count, character_list):
  print(f"--- Begin report of {path} ---")
  print(f'{word_count} words found in the doucment\n')
  print(character_list)

  character_list.sort(reverse=True, key=sort_on)
  for character in character_list:
    print(f"The '{character['name']} was found {character['num']} times")
  print("--- End report ---")  


def get_text(path):
  with open(path) as f:
    return f.read()

if __name__ == "__main__":
  path = "books/frankenstein.txt"
  open_book(path)


