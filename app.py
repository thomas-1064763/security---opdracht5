from cryptography.fernet import Fernet

def gen_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
        print("🔑 Nieuwe sleutel is succesvol gegeneerd en opgeslagen als 'secret.key'.")
    return key

def load_key():
    try:
        with open("secret.key", "rb") as key_file:
            key = key_file.read()
            print("✅ Sleutel is succesvol geladen uit 'secret.key'")
            return key
    except FileNotFoundError:
        print("⚠️  Er is geen sleutel gevonden. Er wordt een nieuwe sleutel gegenereerd.")
        return gen_key()

def encrypt(message):
    key = load_key()
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode())
    return encrypted_message.decode()

def decrypt(encrypt):
    key = load_key()
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypt.encode()).decode()
    return decrypted_message
