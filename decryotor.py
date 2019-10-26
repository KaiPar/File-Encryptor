from encryptor import encrypt

cipher = {
    'A' : "1",
    'B' : "3",
    'C' : "2",
    'D' : "4",
    'E' : "6",
    'F' : "5",
    'G' : "7",
    'H' : "9",
    'I' : "0",
    'J' : "A",
    'L' : "B",
    "M" : "C",
    "N" : "D",
    "O" : "E",
    "P" : "F",
    "Q" : "G",
    "R" : "S",
    "T" : "H",
    "U" : "I",
    "V" : "W",
    "X" : "J",
    "Y" : "K",
    "Z" : "Q",
    "1" : "b",
    "2" : "c",
    "3" : "g",
    "4" : "i",
    "5" : "h",
    "6" : "l",
    "7" : "n",
    "8" : "m",
    "9" : "x",
    "0" : "z",
    " " : " ",
    "\n" : "\n", 
    'K' : "*",
    'a' : "!",
    'b' : "#",
    'c' : "@",
    'd' : "%",
    'e' : "$",
    'f' : "&",
    'g' : "^",
    'h' : "(",
    'i' : "-",
    'j' : ")",
    'k' : "+",
    'l' : "[",
    'm' : "}",
    'n' : "]",
    'o' : "{",
    'p' : "p",
    'q' : "|",
    'r' : ":",
    's' : ";",
    't' : "'",
    'u' : '"',
    'v' : "/",
    'w' : "?",
    'x' : "<",
    'y' : ".",
    'z' : ">",
    ',' : ','
}

rev_cipher = inv_map2 = {v: k for k, v in cipher.items()}


def chk_pass(passWd):
    f = open("password.txt", "r")
    if encrypt(passWd) == f.read():
        fr = open("password.txt", "w")
        fr.write("")
        f.close()
        fr.close()
        return True
    else:
        return False


def open_file(path):
    f_read = open(path, 'r')
    org_data = f_read.read()
    return org_data

def decrypt(data):
    decrypt_data = ""
    for x in data:
        if x in rev_cipher:
            decrypt_data += rev_cipher[x]
    return decrypt_data

def write_into(path, data):
    f_write = open(path, 'w')
    f_write.write(data)

def main():
    path = input("Enter path of your file: ")
    passwd = input("Enter password: ")
    if chk_pass(passwd):
        data = open_file(path)
        decrypt_data = decrypt(data)
        print(decrypt_data)
        write_into(path, decrypt_data)
    else:
        print("Invalid Password...")

if __name__ == "__main__":
    main()
    
