import datetime

def show_datetime():
    now = datetime.datetime.now()
    print(f"\nBuddy: Today's date and time is {now.strftime('%Y-%m-%d %H:%M:%S')}")

def ask_feedback():
    print("\nBuddy: Could you share your feedback about our service today?")
    feedback = input("You: ").lower()

    if any(word in feedback for word in ["good", "great", "awesome", "nice", "helpful", "excellent", "thank"]):
        print("Buddy: Thank you so much for your encouragement! We’re happy to help! 😊")
    elif any(word in feedback for word in ["bad", "poor", "worst", "delay", "disappointed", "problem"]):
        print("Buddy: Oh no! I’m sorry to hear that. 😔 Can you tell me which part of the service was not good?")
        issue = input("You: ")
        print(f"Buddy: Thank you for letting us know about '{issue}'. We’ll definitely work on improving that! 💪")
    else:
        print("Buddy: Thank you for your feedback!")

    print("Buddy: On a scale of 1 to 5, how would you rate your experience today?")
    try:
        rating = int(input("You (1-5): "))
        if 1 <= rating <= 5:
            print(f"Buddy: Noted! You rated us {rating}/5. Thank you again! 🌟")
        else:
            print("Buddy: Rating should be between 1 and 5.")
    except ValueError:
        print("Buddy: That doesn't look like a number. We’ll skip the rating.")

def get_address():
    print("Buddy: Please provide the following address details.")
    place = input("Place: ")
    taluk = input("Taluk: ")
    district = input("District: ")
    street = input("Street: ")
    pincode = input("Pincode: ")
    phone = input("Phone number: ")

    
    if not place or not taluk or not district or not street or not pincode or not phone:
        print("Buddy: It looks like some address details are missing. Please provide complete address information.")
        return get_address()  # Recursively ask until the address is complete
    
    print(f"Buddy: Thank you for the address! Place: {place}, Taluk: {taluk}, District: {district}, Street: {street}, Pincode: {pincode}, Phone: {phone}")
    return place, taluk, district, street, pincode, phone

def ask_email():
    print("Buddy: Please provide your email ID to send confirmation.")
    email = input("You: ")
    print(f"Buddy: Thanks! We'll send the confirmation to {email}.")
    return email

def suggest_brand(product):
    if product.lower() == "laptop":
        return "Dell"  
    elif product.lower() == "phone":
        return "Samsung"  
    elif product.lower() == "tv":
        return "Sony"  
    else:
        return "No suggestion available"

def handle_purchase():
    print("Buddy: What product do you want to purchase?")
    product = input("You: ")

    print("Buddy: What is your expected price range?")
    price_range = input("You: ")

    suggested_brand = suggest_brand(product)
    print(f"Buddy: Based on your choice, I suggest considering {suggested_brand} for {product}. Would you like to proceed with this brand? (yes/no)")
    brand_confirmation = input("You: ").lower()

    if brand_confirmation != "yes":
        print("Buddy: No worries! Please specify your preferred brand.")
        brands = input("You: ")
    else:
        brands = suggested_brand

    print(f"Buddy: What features are you looking for in this {product}?")
    features = input("You: ")

    print(f"Buddy: Do you want to place the order for the {brands} {product} with features: {features}? (yes/no)")
    confirm = input("You: ").lower()

    if confirm == "yes":
        name = input("Buddy: Please enter your full name: ")
        address_details = get_address()
        email = ask_email()

        print(f"Buddy: Thank you {name}! Your order for {brands} {product} has been placed successfully.")
        print("Buddy: You will receive the product within 3 to 5 working days. 🚚")
        print(f"Buddy: Confirmation will be sent to {email}.")
        ask_feedback()
    else:
        print("Buddy: No problem! Let me know if you need anything else.")

def handle_delivery():
    print("Buddy: Please enter the product name you are expecting to be delivered:")
    product = input("You: ")

    print("Buddy: Please enter your order ID or reference:")
    order_id = input("You: ")

    print(f"Buddy: Your product '{product}' with order ID '{order_id}' is on the way!")
    print("Buddy: Expected delivery within 2 to 4 working days. 📦")
    email = ask_email()
    print(f"Buddy: Confirmation will be sent to {email}.")
    ask_feedback()

def handle_return():
    print("Buddy: What product would you like to return?")
    product = input("You: ")

    print("Buddy: What is the type/model?")
    model = input("You: ")

    print("Buddy: What was the price of the product?")
    cost = input("You: ")

    print("Buddy: Why do you want to return the product?")
    reason = input("You: ")

    print("Buddy: When did you purchase this product? (YYYY-MM-DD)")
    purchase_date = input("You: ")

    print(f"Buddy: Return accepted for {product} ({model}) purchased on {purchase_date}.")
    print("Buddy: Pickup will be arranged within 2 days. ♻️")
    email = ask_email()
    print(f"Buddy: Confirmation will be sent to {email}.")
    ask_feedback()

def main():
    print("Buddy: Welcome to Smart Customer Support!")
    show_datetime()
    while True:
        print("\nBuddy: Are you here for a purchase, delivery, or return? Type 'exit' to leave.")
        query = input("You: ").lower()

        if query == "purchase":
            handle_purchase()
        elif query == "delivery":
            handle_delivery()
        elif query == "return":
            handle_return()
        elif query == "exit":
            print("Buddy: Thank you for using our service. Goodbye! 👋")
            break
        else:
            print("Buddy: Sorry, I didn't understand that. Please choose: purchase, delivery, or return.")


main()