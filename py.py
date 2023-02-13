# For when school, or admin blocks websites such as ChatGPT
import openai
import subprocess
from colorama import Fore, Style
import pwinput
import json
import os
import base64


def askquestion(question, engine):
  completion = openai.Completion.create(
    engine=engine,
    prompt=question,
    max_tokens=2048,
    n=1,
    stop=None,
    temperature=0.5,
  )

  response = completion.choices[0].text
  return response


if __name__ == "__main__":
  print(Fore.RED + 'Test /n' + Style.RESET_ALL)
  key1 = base64.b64decode(
    "c2std2NERzNhYTRqOUlVbWc3VnVWYjlUM0JsYmtGSkhTdGlrd3ZDYUZhQjJIZTFLRHNQ").decode("utf-8")
  key2 = base64.b64decode(
    "c2stOFRBWXZjMnd1THhORk5qWVR5VDBUM0JsYmtGSmVlTmtScjBjNTROS1d3U3RCTWZB").decode("utf-8")
  openai.api_key = key1 or key2
  model_engine = 'text-davinci-003'

  print(
    Fore.GREEN +
    "Chat commands: \n\tExit - Straight forward. \n\tNano - [NOT WORKING!!]\n"
    + Style.RESET_ALL)
  print(Fore.MAGENTA +
        "Hi, I'm a ChatGPT based AI. How can I help you today? \n")

  while True:
    question = input(Fore.BLUE + "You: \n")

    if question.lower() == "exit":
      print("Bye! Have a great day.")
      break
    response = askquestion(question, model_engine)
    print(Fore.MAGENTA + "\nChatGPT: " + response + "\n" + Style.RESET_ALL)
