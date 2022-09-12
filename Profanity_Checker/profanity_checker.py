import requests

def read_text():
  quotes = open(r"C:\Udacity projects\Profanity_Checker\movie_quotes.txt")
  content = quotes.read()
  quotes.close()
  check_profanity(content)

def check_profanity(text_to_check):
  connection = requests.get("https://www.purgomalum.com/service/containsprofanity?text="+text_to_check)

  if connection.text:
    print('Text contains profanity!')
  else:
    print('Text does not contain profanity!')

read_text()