words =input("What would you like to tell me?\n").lower()
# Respond to speech
if"hello"in words: 
    print("Hello to you too!")
elif"how are you"in words:
    print("I am doing great, thanks for asking! How are you?")
elif"goodbye"in words:
    print("Goodbye to you too!")
else:
    print("Huh?")

