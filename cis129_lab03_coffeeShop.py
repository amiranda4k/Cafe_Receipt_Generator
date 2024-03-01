# Define the prices of items and the tax rate
PRICE_OF_COFFEE = 5  # $5 per coffee
PRICE_OF_MUFFIN = 4  # $4 per muffin
TAX_RATE = 0.06      # 6% sales tax

# Function to calculate total cost
def calculate_total_cost(num_coffees, num_muffins):
    total_coffee_cost = num_coffees * PRICE_OF_COFFEE
    total_muffin_cost = num_muffins * PRICE_OF_MUFFIN
    subtotal = total_coffee_cost + total_muffin_cost
    tax = subtotal * TAX_RATE
    total_cost = subtotal + tax
    return total_coffee_cost, total_muffin_cost, tax, total_cost

# Function to display receipt
def display_receipt(num_coffees, num_muffins, coffee_cost, muffin_cost, tax, total):
    print("\n***************************************")
    print("My Coffee and Muffin Shop Receipt")
    print(f"{num_coffees} Coffee at ${PRICE_OF_COFFEE} each: ${coffee_cost:.2f}")
    print(f"{num_muffins} Muffins at ${PRICE_OF_MUFFIN} each: ${muffin_cost:.2f}")
    print(f"6% tax: ${tax:.2f}")
    print("---------")
    print(f"Total: ${total:.2f}")
    print("Thank you for visiting! We hope to see you again soon.")
    print("***************************************")

# Main function to run the program
def main():
    # Ask the user for the number of coffees and muffins
    num_coffees = int(input("Number of coffees bought? "))
    num_muffins = int(input("Number of muffins bought? "))

    # Calculate costs and total
    coffee_cost, muffin_cost, tax, total = calculate_total_cost(num_coffees, num_muffins)

    # Display the receipt
    display_receipt(num_coffees, num_muffins, coffee_cost, muffin_cost, tax, total)

# Call the main function to run the program
if __name__ == "__main__":
    main()
