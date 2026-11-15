from time import sleep
from os import system

def print_smooth(text):
    for char in text:
        print(char, end="", flush=True)
        sleep(0.05)
def clear():
    system("clear")

clear()

with open("speed_of_text.txt", mode="r", encoding="utf-8") as f_speed, open(
    "text.txt", mode="r", encoding="utf-8"
) as f_text:
    for speed_line, text_line in zip(f_speed, f_text):
        delay = float(speed_line.strip())
        print_smooth(text_line)
        sleep(delay)

print()
