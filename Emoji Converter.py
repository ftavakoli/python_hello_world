# the program identifies the smiley faces within the user's message and
# converts to the corresponding emojis
emoji_mapping =  {
    ":)": "😀",
    ":(": "😞",
    ";)": "😉",
    ":@": "🤬"
}

user_message = input("> ")
words_list = user_message.split(" ")  # generates a list
message = ""
for word in words_list:
    message += emoji_mapping.get(word, word) + " "
print(message)
