from cryptography.fernet import Fernet

key = "UJ5_V_b-TWKKyzlErA96f-9aEnQEfdjFbRKt8ULjdV0="
cred = "gAAAAABfMbX0bqWJTTdHKUYYG9U5Y6JGCpgEiLqmYIVlWB7t8gvsuayfhLOO_cHnJQF1_ibv14si1MbL7Dgt9Odk8mKHAXLhyHZplax0v02MMzh_z_eI7ys="

f = Fernet(key)

#convert strings to bytes
cred_byte = str.encode(cred)

decrypted = f.decrypt(cred_byte)

#convert back to string from bytes
decrypted_final = decrypted.decode()

print(decrypted_final)
