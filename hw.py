from random import randint,choice


GREEN = "\u001b[42;1m"
RES = "\u001b[0m"
YELLOW = "\u001b[43;1m"
WHITE = "\u001b[47m"


fruits = ["яблоко","банан","лимон","грейпфрут","ананас","мандарин","манго","гранат","авокадо","киви"]
hidden_word = choice(fruits)
print(u"\u001b[47m \u001b[0m " * len(hidden_word))
user_guess_options = input('Введите слово:')
user_guess_options = [* user_guess_options]


for i in range(len(hidden_word)):
    if hidden_word[i] == user_guess_options[i]:
        user_guess_options[i] = GREEN + user_guess_options[i] + RES


for i in range(len(hidden_word)):
    if user_guess_options[i] in hidden_word:
        user_guess_options[i] = YELLOW + user_guess_options[i] + RES


user_guess_options = "".join(user_guess_options)
print(f"{user_guess_options}")





