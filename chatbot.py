print("Hello I'm Chatbot. How Can I Help You?")
while True:
    user = input("You: ") 
    if user.lower() in ["bye","exit","quit"]:
        print("Bot : Goodbye! ")
        break
    elif user.lower() in ["hi","good morning","hello",]:
        print(user,"!!")
        user = input("Do you want me to Help you? : ")
        if user.lower() in ["yes"]:
            print("Okay Tell me!")
    elif user.lower() in ["tell me about the topic"]:
        print("Give the prompt!")
    elif user.lower() in [""]:
        print("It Seem's Empty, Type something")
    else:
        print("No data found")