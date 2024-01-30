def morse_translator(text):
    # Morse code mapping
    morse_code_dict = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
    }

    translated_text = []
    for word in text.upper().split():
        translated_word = ' '.join([morse_code_dict.get(char, '') for char in word])
        translated_text.append(translated_word)

    return ' / '.join(translated_text)

# Test cases
test1 = morse_translator("HELLO WORLD")  # Expected: ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
test2 = morse_translator("Python")       # Expected: ".--. -.-- - .... --- -."
test3 = morse_translator("Morse Code")   # Expected: "-- --- .-. ... . / -.-. --- -.. ."

test1, test2, test3

print(morse_translator(""))





