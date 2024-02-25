TICKET_PRICE = 10
SURCHARGE = 2

tickets_remaining = 100  

# Create the calculate the calculte_price function with surcharge of $2

def calculate_price(number_of_tickets):
    return (number_of_tickets * TICKET_PRICE) + SURCHARGE

# Run this code until all tickets are sold
while tickets_remaining >= 1:

    #Output how many tickets are remaining using the tickets_remaining variable. 
    print("There are {} tickets remaining".format(tickets_remaining))
    
    # Gather user's name and assign it to a new variable
    user_name = input("What is your name? ")
    
    # Prompt user by name and ask how many tickets they would like and handle any possible ValueError's
    try:
        number_of_tickets = int(input("How many tickets do you wish to purchase? "))
        if number_of_tickets > tickets_remaining:
            raise ValueError("There are only {} tickets remaining".format(tickets_remaining))
        # Raise ValueError if there is a request for more tickets than are available
    except ValueError as err:
        # Include the error text in the output
        print("Oops, that is an invalid value. {}. Please try again.".format(err))
    else:
        # Calculate the total price for tickets and assign it to a variable
        total_price = calculate_price(number_of_tickets)
                
        # Output the price to the screen
        print("Your total price is: ${}".format(total_price))
        
        # Prompt user if they want to proceed. Y/N
        confirm = input("Do you wish to purchase tickets for the price of ${}. Yes or No? ".format(total_price))
        
        # If they wish to proceed, 
        if confirm.lower() == "yes":
            # print out to screen "Sold"
            print("Sold!")
            # and then reduce tickets remaining by number of tickets purchased
            tickets_remaining -= number_of_tickets
            
            # otherwise thank them by name
        else:
            print("Thank you for visiting {}. Have a great day :)".format(user_name))
        
    # Notify user if tickets are sold out
else:
    print("Sorry, tickets are all sold out :(")