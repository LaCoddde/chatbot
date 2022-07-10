# Chat bot tes
import time
from replit import clear

bot_name = "Leo the ChatBot"
# customer_care = ""
# start_over = ""
begin = True

options = {
    1: ["How does Headless UI work?", "https://leo1.com"],
    2: ["How do Form Input Tags work?", "https://leo2.com"],
    3: ["Is there a payment plan to access all javascript functions for CURLCSS?", "https://leo3.com"],
    4: ["How long does my subscription last using the BASIC plan?", "https://leo4.com"],
}

print(f"Hi, my name is {bot_name}.")
client_name = input("What is your name?:\n").title()
print("")
print(f"Hello {client_name}!!!\nWelcome to CURLCSS.")
print("")
time.sleep(1)


def begin():
    print("Below are the things I can assist you with today:")

    for key in options:
        # print(key, options[key][0])
        # print(key)
        print(f"{key}: {options[key][0]}")
        time.sleep(1)

    print("")
    all_good = False

    prompt = int(input("To make a selection, reply with the number next to your option.\n"
                       "Example: Reply 1 for 'How does Headless UI work?': "))
    print("")

    for key in options:
        if key == prompt:
            print(f"{key}: {options[key][0]}")
            print(
                f"Please follow the link: {options[key][1]} to get more information on that.\nThank you {client_name}.")
            print("")
            all_good = True
            start_over = input("Would you like to start all over? Enter 'Y' for yes and 'N' for no: ").lower()
            print("")
            if start_over == "y":
                clear()
                begin()
            else:
                break

    if not all_good:
        print("Oops!")
        customer_care = input("It seems you have entered a different input, would you like me to "
                              "transfer you to customer care?\n""Enter 'Y' for yes and 'N' for no: ").lower()

        if customer_care == "y":
            print("Connecting you to support...")
        else:
            start_over = input("Would you like to start all over? Enter 'Y' for yes and 'N' for no: ").lower()
            if start_over == "y":
                clear()
                begin()

    print("Thank you for your time.\nLeo the ChatBot says goodbye!")


begin()
