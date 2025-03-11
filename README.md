# Project Title : ATM Machine Simulation

# Program Execution:

The script includes a conditional check to ensure that the ATM simulation runs only when the script is executed directly, not when imported as a module.

# Methods within :
check_balance: Displays the current account balance to the user.

deposit: Accepts a deposit amount, validates that it's positive, adds it to the balance, and confirms the transaction.

withdraw: Handles withdrawal requests by ensuring the requested amount is positive and does not exceed the available balance. It then deducts the amount and confirms the transaction.

run: Acts as the main interface, presenting users with options to check their balance, deposit funds, withdraw funds, or exit. It continuously prompts for user input until the user chooses to exit.
