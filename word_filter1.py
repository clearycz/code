import re

def word_filter_counter(text, filter_words):
    # Convert filter words to lowercase for case-insensitive comparison
    filter_words = set(word.lower() for word in filter_words)

    # Remove punctuation and split text into words
    words = re.findall(r'\b\w+\b', text.lower())

    # Count occurrences of filtered words
    word_count = {}
    for word in words:
        if word in filter_words:
            word_count[word] = word_count.get(word, 0) + 1

    return word_count

# Test cases
test1 = word_filter_counter("Hello world, hello!", ["hello"])  # Expected: {'hello': 2}
test2 = word_filter_counter("The quick brown fox.", ["the"])   # Expected: {'the': 1}
test3 = word_filter_counter("Is this real life? Is this just fantasy?", ["is", "this", "just"])  # Expected: {'is': 2, 'this': 2, 'just': 1}
test4 = word_filter_counter("Do we see the big picture or just small details?", ["we", "the", "or"])  # Expected: {'we': 1, 'the': 1, 'or': 1}

test1, test2, test3, test4

