text = input("Add text: The most widely performed love story ")
uniq_symbols = set(text)
if len(uniq_symbols) > 10:
    print('True')
else:
    print('False')