import re


class Token:
    def __init__(self, text, index):
        self.text = text
        self.index = index
        if text == 'x':
            self.kind = 'variable'
        elif re.match(r"^[0-9]", text):
            self.kind = 'number'
        elif re.match(r"[*+-/^()]", text):
            self.kind = 'operator'
        else:
            self.kind = 'function'

    def __str__(self):
        return self.text


class Tokenizer:
    @staticmethod
    def tokenize(text):
        text_len = len(text)
        token_list = []
        token_pattern = r"[0-9]+(\.[0-9]*)?([eE][\+\-]?[0-9]+)?|x|sin|cos|tg|[*+-\/\(\)]"
        while True:
            match = re.match(token_pattern, text)
            if not match:
                break
            token_list.append(Token(match.group(0), text_len-len(text)))
            text = text[match.start() + len(match.group(0)):]
        return token_list
