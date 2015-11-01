def prompt()
	message = input("What is your message? ")
	key = input("What is your key? ")
  encrypted = encrypt(message, key)
	print("Encrypted message")
	print(encrypted)

def encrypt(message, key):
  klen = len(key)
  return "".join([message[i] + key[i%klen] for i in range(len(message))])

if __name__ == "__main__":
  prompt()