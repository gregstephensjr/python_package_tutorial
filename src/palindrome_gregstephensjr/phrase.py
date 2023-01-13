import re
class Phrase:
    """A class to represent phrases."""

    def __init__(self, content):
        self.content = str(content)

    def processed_content(self):
        """Processes the content for palindrome testing."""
        return self.letters_and_digits().lower()

    def ispalindrome(self):
        """Return True for a palindrome, False otherwise."""
        return self.processed_content() == reverse(self.processed_content())

    def letters_and_digits(self):
        """Return the letters in the content."""
        # imperative solution
        # the_letters = []
        # for char in self.content:
        #     if re.search(r"[a-zA-Z]", char):
        #         the_letters.append(char)
        # return "".join(the_letters)

        # functional solution with re.search
        # return "".join(c for c in self.content if re.search(r"[a-zA-Z]", c))
        
        # functional version with re.findall
        return "".join(re.findall(r"[a-zA-Z\d]", self.content))

    # def functional_singles(states):
    #     return [state for state in states if len(state.split()) == 1]

def reverse(string):
    """Reverse a string."""
    return "".join(reversed(string))