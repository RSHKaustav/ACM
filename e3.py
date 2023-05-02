from Crypto.Cipher import AES
from hashlib import md5

print('Choose operation to be done:\n\t1- Encryption\n\t2- Decryption')
operation = input('Your Choice: ')

file_path = input('File Path: ')
#Key that will be used for the encryption process
key = input('Key: ')
key_hash = md5(key.encode('ascii')).digest()

#Initial Vector optimally should be random but for simplicity we are going for a constant one
iv = "kaasfasf"
iv_hash = md5(key.encode('ascii')).digest()



with open(file_path, 'rb') as input_file:
    #Saving the input image files as a byte string
    file_bytes = input_file.read()

    if operation == '1':
        #Generating the cipher for the encrption process
        cipher = AES.new(key_hash, AES.MODE_EAX, iv_hash)
        #Encrypting the image
        new_file_bytes = cipher.encrypt(file_bytes)
    else:
        cipher = AES.new(key_hash, AES.MODE_EAX, iv_hash)
        #Decrypting the image
        new_file_bytes = cipher.decrypt(file_bytes)

    
    
with open(file_path, 'wb') as output_file:
    #Writing the new byte string into the original file
    output_file.write(new_file_bytes)
    print('Operation Done!')

print(key_hash)
print(iv_hash)

       
