# Importing required modules.
import random
import string

import kivy
from kivy.app import App
from kivy.core.clipboard import Clipboard
from kivy.uix.boxlayout import BoxLayout

# Minimum requirements.
kivy.require("1.9.0")

# The Characters for generating passwords.
UPPERCASE = string.ascii_uppercase
LOWERCASE = string.ascii_lowercase
DIGITS = string.digits
PUNCTUATION = string.punctuation.replace("-", "")

CHARS = UPPERCASE + LOWERCASE + DIGITS + PUNCTUATION
LENGTH = 13


class MyRoot(BoxLayout):

    def __init__(self):
        super(MyRoot, self).__init__()

    @staticmethod
    def get_random_password():
        # Generating random password.
        password = ""
        for i in range(LENGTH):
            if i % 4 == 0 and i != 0 and i + 1 != LENGTH:
                password += "-"
            else:
                password += random.choice(CHARS)

        return password

    def generate_password(self):
        # Checking if copy btn is disabled.
        if self.copy_btn.disabled:
            self.copy_btn.disabled = False

        # Changing the text of the label.
        self.password_label.text = self.get_random_password()

    def copy_password(self):
        # Copying password to clipboard.
        Clipboard.copy(self.password_label.text)


class PWGenerator(App):

    def build(self):
        return MyRoot()


pwgenerator = PWGenerator()
pwgenerator.run()
