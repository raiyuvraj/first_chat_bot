# import random

# # Dictionary of responses: Fisrst Project

# responses = {
#     "hi": ["Hello !!", "Hey !!", "Hi, how can I help you ?"],
#     "how are you ?": ["I am doing well, thank you !!", "I'm good, thank for asking. "],
#     "bye" : ["Good bye !!", "Bye !!", "See you later.", "Have a great day !!"],
#     "default" : ["Sorry, I didn't understand that.", "I'm not sure what do you mean."]
# }

# # for generating responses:

# def get_responses(message):
#     message= message.lower()
#     if message in responses:
#         return random.choice(responses[message])
#     else:
#         return random.choice(responses["default"])

# # for getting user input:

# def main():
#     print("Chatbot: Hello, How can i help you ?") 
#     while True:
#         user_input = input("You: ")
#         if user_input.lower()== "exit":
#             print("Chatbot: Good Bye !!")
#             break
#         response = get_responses(user_input)
#         print("Chat Bot: ", response)
# # calling the method
# main()
  