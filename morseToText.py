morse = {'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', '0':'-----'}
val_list = list(morse.values())
key_list = list(morse.keys())
code = input("Enter a morse code: ")
code += " "
start = 0
for i in range(0, len(code)):
    if code[i - 1:i + 1] == "/ ":
        start = i + 1
        continue
    if  code[i] == "/":
        print(" ", end = "")
        continue
    if code[i] == " ":
        print(key_list[val_list.index(code[start:i])], end = "")
        start = i + 1