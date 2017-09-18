class Grammar():
    def a(word):
        if word in "aeiou":
            return "an " + word
        else:
            return "a " + word

    def are(amount, item):
        if amount == 1:
            return "is " + str(amount) + " " + item
        else:
            return "are " + str(amount) + " " + item + "s"
