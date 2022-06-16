from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet
import os


def HybridCryptKeys(): #encrypt key
    key = Fernet.generate_key() #uses a function from the 'cryptography' package to generate a fresh fernet key. generate_key() is called from IVsKeys file.
    print("key is"+str(key))
    f=open('SecureKey.txt', 'wb') #open the SecureKey.txt file
    f.write(key)# write the generated key to the SecureKey.txt file to safely store the key
    f.close()#close the opened file

    listDir=os.listdir(os.getcwd()+"\Infos") #listdir() lists the files present in the 'Infos' folder.
    #here listDir gets ['IV.txt', 'KEY1.txt', 'KEY2.txt', 'LengthFile.txt']


    fer = Fernet(key) #store the key into the 'fer' variable
    for i in listDir:
        KI=open(os.getcwd()+'\Infos\\'+i,'rb') #open each file
        content=KI.read() #read content of the file
        KI.close() #close the file
        content=fer.encrypt(content) #Encrypts data passed (content). The result of this encryption is known as a “Fernet token”.
        #Fernet tokens  are message packed tokens that contain authentication and authorization data.

        open(os.path.join(os.getcwd()+"\Infos",i),'wb').close()
        #os.path.join() method in Python join one or more path components intelligently.
        f=open(os.path.join(os.getcwd()+"\Infos",i),"wb")
        f.write(content)# write the “Fernet token” to the files in the 'infos' folder
        f.close()


def AES(key,iv): #Encrypting with AES
    f=open(os.path.join(os.getcwd()+"\Segments","0.txt"),"r") #open segment 0.txt file
    content=f.read() #store contents to variable "content"
    f.close() #close file
    content=content.encode() #encode the content
    b=len(content) #get length of content.

    #AES is a block cipher. “a block cipher is a deterministic algorithm operating on fixed-length groups of bits”.
    # AES can only work with blocks of 128 bits (that is, 16 chars).
    if(b%16!=0): #if file is not empty do:
        while(b%16!=0): # while file is not empty do:
            content+=" ".encode() #encode
            b=len(content)
    backend = default_backend()
    #A backend that provides methods for using ciphers for encryption and decryption. here: OpenSSL backend.
    print("backend"+str(backend))

    # Encrypt and get the associated ciphertext.
    # CBC (Cipher Blocker Chaining) is an advanced form of block cipher encryption.
    # With CBC mode encryption, each ciphertext block is dependent on all plaintext blocks processed up to that point.
    #In Cipher Block Chaining (CBC) mode, an initialization vector (IV) is added to the first block of plaintext before
    # encryption and the resultant ciphertext is added to the next block of plaintext before encryption, and so on.
    # Decryption is the reverse process.
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend) #get ciphertext by passing key from .hazmat.primitives.ciphers

    encryptor = cipher.encryptor()
    # When calling encryptor() or decryptor() on a Cipher object the result will conform to the CipherContext interface.
    # You can then call update(content) with data until you have fed everything into the context.
    # Once that is done call finalize() to finish the operation and obtain the remainder of the data.
    cont = encryptor.update(content) + encryptor.finalize()
    open(os.path.join(os.getcwd()+"\Segments","0.txt"),"wb").close()
    f=open(os.path.join(os.getcwd()+"\Segments","0.txt"),"wb")
    f.write(cont) #write encrypted content to the file
    f.close();

def BlowFish(key,iv): #encrypt using blowfish algorithm
    f=open(os.path.join(os.getcwd()+"\Segments","1.txt"),"r") #open 1.txt
    content=f.read()
    f.close()
    content=content.encode()
    b=len(content)
    #Blowfish is a block cipher that operates on 64 bit (8 byte) blocks of data.
    if(b%8!=0):
        while(b%8!=0):
            content+=" ".encode()
            b=len(content)
    backend = default_backend()
    cipher = Cipher(algorithms.Blowfish(key), modes.CBC(iv), backend=backend)
    encryptor = cipher.encryptor()
    cont = encryptor.update(content) + encryptor.finalize()
    open(os.path.join(os.getcwd()+"\Segments","1.txt"),"w").close()
    f=open(os.path.join(os.getcwd()+"\Segments","1.txt"),"wb")
    f.write(cont);
    f.close();


def TrippleDES(key,iv): #encrypting using 3DES algorithm
    f=open(os.path.join(os.getcwd()+"\Segments","2.txt"),"r");
    content=f.read();
    f.close();
    content=content.encode()
    b=len(content);
    if(b%8!=0):
        while(b%8!=0):
            content+=" ".encode()
            b=len(content);
    backend = default_backend();
    cipher = Cipher(algorithms.TripleDES(key), modes.CBC(iv), backend=backend);
    encryptor = cipher.encryptor();
    cont = encryptor.update(content) + encryptor.finalize();
    open(os.path.join(os.getcwd()+"\Segments","2.txt"),"w").close();
    f=open(os.path.join(os.getcwd()+"\Segments","2.txt"),"wb");
    f.write(cont);
    f.close();

def AES2(key,iv):
    f=open(os.path.join(os.getcwd()+"\Segments","3.txt"),"r")
    content=f.read()
    f.close()
    content=content.encode()
    b=len(content)
    if(b%16!=0):
        while(b%16!=0):
            content+=" ".encode()
            b=len(content)
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    encryptor = cipher.encryptor()
    cont = encryptor.update(content) + encryptor.finalize()
    open(os.path.join(os.getcwd()+"\Segments","3.txt"),"wb").close()
    f=open(os.path.join(os.getcwd()+"\Segments","3.txt"),"wb")
    f.write(cont)
    f.close();



def TrippleDES2(key, iv):
    f=open(os.path.join(os.getcwd()+"\Segments","4.txt"),"r");
    content=f.read();
    f.close();
    content=content.encode()
    b=len(content);
    if(b%8!=0):
        while(b%8!=0):
            content+=" ".encode()
            b=len(content);
    backend = default_backend();
    cipher = Cipher(algorithms.TripleDES(key), modes.CBC(iv), backend=backend);
    encryptor = cipher.encryptor();
    cont = encryptor.update(content) + encryptor.finalize();
    open(os.path.join(os.getcwd()+"\Segments","4.txt"),"w").close();
    f=open(os.path.join(os.getcwd()+"\Segments","4.txt"),"wb");
    f.write(cont);
    f.close();


