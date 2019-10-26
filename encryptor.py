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
}

#all Special ciphers(conting special charecters)
sp_cipher_sym = {
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


sp_cipher = inv_map = {v: k for k, v in sp_cipher_sym.items()} #revers the special chipher

def open_file(path):
    f_read = open(path, 'r')
    org_data = f_read.read()
    return org_data

def encrypt(data):
    encrypt_data = ""
    for x in data:
        if x in sp_cipher_sym:
            encrypt_data = encrypt_data + sp_cipher_sym[x]
        elif x in sp_cipher:
            encrypt_data = encrypt_data + sp_cipher[x]
        elif x not in sp_cipher and x not in sp_cipher_sym:
            encrypt_data += x
        else:
            encrypt_data = encrypt_data + cipher[x]
    return encrypt_data

def write_into(path, data):
    f_write = open(path, 'w')
    f_write.write(data)
    f_write.close()

def cr_pass():
    f = open("password.txt", "w")
    f.write("")
    passwd = input("Set a password: ")
    passwd = encrypt(passwd)
    f.write(passwd)
    f.close()
    return True

def main():
    path = input("Enter path of your file: ")
    data = open_file(path)
    cr_pass()
    enc_data = encrypt(data)
    print(enc_data)
    write_into(path, enc_data)

if __name__ == "__main__":
    main()

