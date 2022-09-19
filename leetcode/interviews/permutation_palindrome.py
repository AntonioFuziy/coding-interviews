import string

def is_permutation_of_palindrome(phrase: str):
  lower_phrase = phrase.lower().replace(" ", "").translate(str.maketrans('', '', string.punctuation))
  char_count = {}
  for char in lower_phrase:
    if char in char_count:
      char_count[char] += 1
    else:
      char_count[char] = 1
  odd_count = 0
  for count in char_count.values():
    if count % 2 == 1:
      odd_count += 1
    if odd_count > 1:
      return False
  return True