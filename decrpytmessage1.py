def decrypt_message(encrypted_text, key):
    decrypted_text = bytearray()
    for byte in encrypted_text:
        decrypted_text.append(byte ^ key)
    return decrypted_text

#This statement is used  Read the encrypted text file
with open('secretmessageA.txt.enc', 'rb') as file:
    encrypted_data = bytearray(file.read())

# This method is used to iterate through possible keys (0 to 255)
for key in range(256):
    decrypted_data = decrypt_message(encrypted_data, key)
    #Verfiying whether the result looks like ASCII text
    if all(32 <= byte < 127 or byte == 10 or byte == 13 for byte in decrypted_data):
        #This is the Print statement for the decrypted text and the key
        print(f"Key: {key}\nDecrypted Text is as follows:\n{decrypted_data.decode('utf-8')}")