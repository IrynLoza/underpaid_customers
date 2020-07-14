def count__customers_payments(name, melons, paid, melon_cost=1.00):
    # defining function and put parameters with customers data inside
    """Counting customers payment for melons and catch unexpected sum"""
    # add Docstring to explain the function

    expected = melons * melon_cost
    # count the expected payment

    # catch if payment unexpected and print output
    if expected != paid:
        print(f'{name} paid ${paid:.2f},', f'expected ${expected:.2f}')
        # {paid:.2f} cut the payment under 2 integers after .


count__customers_payments('Joe', 5, 5.00)  # call the function
count__customers_payments('Frank', 6, 6.00)
count__customers_payments('Sally', 3, 3.00)
count__customers_payments('Sean', 9, 9.50)
count__customers_payments('David', 4, 4.00)
count__customers_payments('Ashley', 3, 2.00)
