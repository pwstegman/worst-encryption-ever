message = input("What is your encrypted message? ")
print("Decrypted message")
print("".join([message[i] for i in range(0, len(message), 2)]))
