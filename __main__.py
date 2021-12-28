from core import block
from core.block import Block
from core.blockchain import Blockchain
from uuid import uuid4
import time

# TODO: Move Commands
transaction_command = "t"
mine_command = "m"
print_command = "p"
quit_command = "q"

# TODO: Move these Messages
input_block = """
Input one of the following commands:
- t/T (add new transaction)
- m/M (mine transactions)
- p/P (print current blockchain state)
- q/Q (to quit)

Command to Run: 
"""
input_difficulty = "Input the difficulty(integer MAX 65) for the blockchain: "
invalid_command_msg = "Invalid command attempted please try again"
transaction_message = "Adding a new Transaction {} to the Blockchain"
mine_message = "Mining a new Block for the Chain"
mined_message = "Completed minging Block {}"
print_message = "Below is the current state of the block chain!"

# Define Main Function
"""
Quick main function to test the block chain and see how we're doing
"""
def main():
    difficulty = int(input(input_difficulty))

    if difficulty <= 0 or difficulty > 65: return

    blockchain = Blockchain(difficulty)

    while True:
        possible_commands = ["t", "m", "p", "q"]
        command = input(input_block).lower()

        if command not in possible_commands:
            print(invalid_command_msg)
            continue

        if command == transaction_command:
            transaction = str(uuid4())
            print(transaction_message.format(transaction))
            blockchain.add_new_transaction(transaction)

        if command == mine_command:
            print(mine_message)
            new_block_id = blockchain.mine()
            print(mined_message.format(new_block_id))

        if command == print_command:
            print(print_message)
            print(blockchain)
        
        if command == quit_command:
            print("Done!")
            break

if __name__ == "__main__":
    main()