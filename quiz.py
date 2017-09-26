def make_quiz_text(text, words):
    """
    Returns a quiz text with blank spaces for each word in words

    :param text: (str) Quiz text.
    :param words: (list) List of words.
    :return: (str) Quiz text filled with blank spaces.
    """
    for index, word in enumerate(words):
        text = text.replace(word, "___{}___".format(index + 1))
    return text


def get_and_check_user_input(words, index):
    """
    Gets the user_input. Checks if the user_input is equal to the asked word in the list.
     Returns True or False.

    :param words: (str) List of words.
    :param index: (int) Index of the words on the list.
    :return: (bool) Returns True if the user_input is correct else False.
    """
    user_input = raw_input("What do you think needs to go on ___{}___ ? ".format(index + 1))
    if user_input.lower() == words[index].lower():
        return True
    else:
        return False


def quiz(text, words):
    """
    This function starts the quiz, with the input of text and a list of words.

    :param text: (str) Quiz text.
    :param words: (list) List of words.
    """
    text = make_quiz_text(text, words)
    print "Hello, welcome to the quiz!\n\n" + text + "\n"

    index = 0
    attempts = 2 * len(words)
    while attempts > 0 and not index == len(words):
        if get_and_check_user_input(words, index):
            text = text.replace("___{}___".format(index + 1), words[index])
            index += 1
            print "That's correct!\n\n" + text + "\n"
        else:
            attempts -= 1
            print "Wrong, you've got {} attempts left.\n\n".format(attempts) + text + "\n"
    if attempts > 0:
        print "You won! Congratulations!"
    else:
        print "You are all out of tries, you lost!"


def get_level(options):
    """
    Asks the user to select a level from a list of options.

    :param options: (list) level options
    :return: selected level
    """
    user_input = raw_input("Make a choice for a level: " + ", ".join(options) + "\n")
    if user_input not in options:
        print "I didn't get that."
        return get_level(options)
    return user_input

if __name__ == "__main__":
    level = get_level(["easy", "medium", "hard"])

    if level == "easy":
        text = "Here's a little song I wrote\n" \
               "You might want to sing it note for note\n" \
               "Don't worry, be happy\n" \
               "In every life we have some trouble\n" \
               "But when you worry you make it double\n" \
               "Don't worry, be happy\n" \
               "Don't worry, be happy now"
        words = ["song", "sing", "happy", "life"]
    elif level == "medium":
        text = "A woman who my mother knows,\n" \
               "Came in and took off all her clothes. \n" \
               "Said I, not being very old, \n" \
               "'By golly gosh, you must be cold!'\n" \
               "'No, no.' She cried. 'Indeed Im not!'\n" \
               "'Im feeling develishly hot!'"
        words = ["woman", "clothes", "cold", "hot"]
    else:
        text = "Cheer up, Brian. You know what they say.\n" \
               "Some things in life are bad, \n" \
               "They can really make you mad.\n" \
               "Other things just make you swear and curse.\n" \
               "When you're chewing on life's gristle,\n" \
               "Don't grumble, give a whistle!\n" \
               "And this'll help things turn out for the best\n " \
               "And \n\n" \
               "Always look on the bright side of life!\n\n" \
               "Always look on the bright side of life\n" \
               "If life seems jolly rotten, \n" \
               "There's something you've forgotten!\n" \
               "And that's to laugh and smile and dance and sing,\n\n" \
               "When you're feeling in the dumps, \n" \
               "Don't be silly chumps,\n" \
               "Just purse your lips and whistle -- that's the thing!\n" \
               "And always look on the bright side of life"
        words = ["life", "mad", "things", "chewing", "whistle", "bright", "rotten"]

    quiz(text, words)
