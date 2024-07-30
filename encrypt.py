from cryptography.fernet import Fernet
import base64

def encrypt_text_file(file_path, key):
    with open(file_path, 'rb') as file:
        data = file.read()

    cipher_suite = Fernet(key)
    encrypted_data = cipher_suite.encrypt(data)

    with open(file_path + '.encrypted', 'wb') as file:
        file.write(encrypted_data)


name = "Rishabh Rai"  #information asked my the professor
username = "rr19pa"
student_number = "6847156"

#Produce the encryption key using the given formula.
key = base64.urlsafe_b64encode((100 + int(student_number[-2:])).to_bytes(32, byteorder='big'))

#Here we are storing the text information in a file
with open('info.txt', 'w') as file:
    file.write(f"Name: {name}\nUsername: {username}\nStudent Number: {student_number}")

# Encrypt the content within the file
encrypt_text_file('info.txt', key)

print("Encryption completed.")
