text = "four score and seven years ago.98787^&&*&^^*87687"
rev_text = text[::-1]

while not rev_text[0].isalpha():
    rev_text = rev_text[1:]

print(rev_text[0])
