# -------------------------------------------------------
# Function to check if input contains only digits
# Returns True if valid positive number
# -------------------------------------------------------
def is_number(value):
    if value == "":
        return False
    
    for ch in value:
        if ch < '0' or ch > '9':
            return False
    
    return True


# -------------------------------------------------------
# E-Commerce Cart System
# - Removes duplicate product prices
# - Applies 10% discount if total > 5000
# - Adds 18% GST
# - Displays final payable amount
# -------------------------------------------------------
def ecommerce_cart():

    # Take product prices input
    data = input("Enter product prices separated by space: ").split()

    prices = []

    # Validate and convert to integers
    for item in data:
        if is_number(item):
            price = int(item)

            # Remove duplicates manually
            if price not in prices:
                prices.append(price)

    # If no valid prices entered
    if len(prices) == 0:
        print("No valid product prices entered.")
        return

    # Calculate total amount
    total = 0
    for price in prices:
        total += price

    print("\nTotal before discount and GST:", total)

    # Apply 10% discount if total > 5000
    if total > 5000:
        discount = (total * 10) // 100
        total = total - discount
        print("Discount Applied (10%):", discount)
    else:
        print("No discount applied.")

    # Add 18% GST
    gst = (total * 18) // 100
    total = total + gst

    print("GST Added (18%):", gst)

    # Final payable amount
    print("Final Payable Amount:", total)









    '''output:
    Enter product prices separated by space: 1000 2000 3000 1000 2000
    Total before discount and GST: 6000
    Discount Applied (10%): 600
    GST Added (18%): 972
    Final Payable Amount: 6572
    ''' 
