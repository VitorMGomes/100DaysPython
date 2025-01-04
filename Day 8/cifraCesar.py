alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        temp = alphabet.index(letter) + shift_amount
        cipher_text += alphabet[temp % len(alphabet)]
    
    print(f"Here is the encoded result: {cipher_text}")
    

def decrypt(encrypted_text, shift_amount):
    decrypted_text = ""
    for letter in encrypted_text:
        temp = alphabet.index(letter) - shift_amount
        decrypted_text += alphabet[temp % len(alphabet)]
    
    print(f"Here is the encoded result: {decrypted_text}")
    
def ceasar(text, shift, direction):
    if(direction == "decrypt"):
        decrypt(text, shift)
    else:
        encrypt(text, shift)
        
command = input("Do u wanna encrypt or decrypt?\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

ceasar(text, shift, command)