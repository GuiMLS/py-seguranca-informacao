import hashlib

string = input("Digite o texto que você quer criptografar: ")

resultado_md5 = hashlib.md5(string.encode('utf-8'))
resultado_sha1 = hashlib.sha1(string.encode('utf-8'))
resultado_sha256 = hashlib.sha256(string.encode('utf-8'))
resultado_sha512 = hashlib.sha512(string.encode('utf-8'))

print(f"O hash da string md5 é: {resultado_md5.hexdigest()}")
print(f"O hash da string SHA1 é: {resultado_sha1.hexdigest()}")
print(f"O hash da string SHA256 é: {resultado_sha256.hexdigest()}")
print(f"O hash da string SHA512 é: {resultado_sha512.hexdigest()}")
