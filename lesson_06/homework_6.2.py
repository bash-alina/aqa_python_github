while True:
    text = input("Add text with 'h' or 'H'")
    if 'h' in text.lower():
        print("With 'h' or 'H'")
        break
    else:
        print("'h' or 'H' not found!")
