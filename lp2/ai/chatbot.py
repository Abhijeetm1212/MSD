def chatbot():
    print(" Hello! Welcome to ShopBot - your shopping assistant.")
    print("How can I help you today?")
    print("Type 'exit' to end the conversation.\n")

    while True:
        user_input = input("You: ").lower()

        if 'exit' in user_input:
            print("ShopBot: Thank you for visiting! Have a great day! 👋")
            break
        elif 'order' in user_input:
            print("ShopBot: You can place an order by visiting our website and adding items to your cart.")
        elif 'status' in user_input or 'track' in user_input:
            print("ShopBot: To check your order status, please enter your order ID on our tracking page.")
        elif 'refund' in user_input or 'return' in user_input:
            print("ShopBot: Refunds are processed within 5-7 business days after the returned item is received.")
        elif 'product' in user_input or 'available' in user_input:
            print("ShopBot: You can browse our product catalog online to check availability.")
        elif 'hello' in user_input or 'hi' in user_input:
            print("ShopBot: Hello there! How can I assist you today?")
        else:
            print("ShopBot: I'm sorry, I didn't understand that. Could you please rephrase?")

# Run the chatbot
chatbot()
