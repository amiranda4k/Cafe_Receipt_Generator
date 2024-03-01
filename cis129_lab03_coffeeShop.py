# Define the prices of items and the tax rate
PRICE_OF_COFFEE = 5  # $5 per coffee
PRICE_OF_MUFFIN = 4  # $4 per muffin
PRICE_OF_TEA = 3     # $3 per tea
PRICE_OF_CROISSANT = 5  # $5 per croissant
TAX_RATE = 0.06      # 6% sales tax

# Function to calculate total cost
def calculate_total_cost(num_coffees, num_muffins, num_teas, num_croissants):
    total_coffee_cost = num_coffees * PRICE_OF_COFFEE
    total_muffin_cost = num_muffins * PRICE_OF_MUFFIN
    total_tea_cost = num_teas * PRICE_OF_TEA
    total_croissant_cost = num_croissants * PRICE_OF_CROISSANT
    subtotal = total_coffee_cost + total_muffin_cost + total_tea_cost + total_croissant_cost
    tax = subtotal * TAX_RATE
    total_cost = subtotal + tax
    return total_coffee_cost, total_muffin_cost, total_tea_cost, total_croissant_cost, tax, total_cost

# Function to display receipt
def display_receipt(num_coffees, num_muffins, num_teas, num_croissants, coffee_cost, muffin_cost, tea_cost, croissant_cost, tax, total):
    print("\n***************************************")
    print("My Expanded Coffee Shop Receipt")
    print(f"{num_coffees} Coffee at ${PRICE_OF_COFFEE} each: ${coffee_cost:.2f}")
    print(f"{num_muffins} Muffins at ${PRICE_OF_MUFFIN} each: ${muffin_cost:.2f}")
    print(f"{num_teas} Tea at ${PRICE_OF_TEA} each: ${tea_cost:.2f}")
    print(f"{num_croissants} Croissant at ${PRICE_OF_CROISSANT} each: ${croissant_cost:.2f}")
    print(f"6% tax: ${tax:.2f}")
    print("---------")
    print(f"Total: ${total:.2f}")
    print("Thank you for visiting! We hope to see you again soon.")
    print("***************************************")

# Main function to run the program
def main():
    # Ask the user for the number of each item
    num_coffees = int(input("Number of coffees bought? "))
    num_muffins = int(input("Number of muffins bought? "))
    num_teas = int(input("Number of teas bought? "))
    num_croissants = int(input("Number of croissants bought? "))

    # Calculate costs and total
    coffee_cost, muffin_cost, tea_cost, croissant_cost, tax, total = calculate_total_cost(num_coffees, num_muffins, num_teas, num_croissants)

    # Display the receipt
    display_receipt(num_coffees, num_muffins, num_teas, num_croissants, coffee_cost, muffin_cost, tea_cost, croissant_cost, tax, total)

# Call the main function to run the program
if __name__ == "__main__":
    main()
