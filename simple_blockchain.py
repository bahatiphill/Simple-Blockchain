#Author: Philbert Bahati
#Date: Jan 25, 2022.
#Python Version: 3.9
import time
import json
import hashlib
import random
import string
import dataclasses
from dataclasses import dataclass


@dataclass
class Block:
    id: int
    transactions: list
    timestamp: float
    prev_block_hash: str
    block_hash: str

    def __post_init__(self):
        if self.block_hash is None:
            self.block_hash = ""

@dataclass
class Account:
    address: str
    coins: int

class Blockchain:

    def __init__(self, name="BahatiChain"):
        
        self.name = name
        self.blocks = []
        self.accounts = []
        self.transactions = []

        # Initialize the genesis block
        self.create_block(id=0, transactions=[])
        

    def create_block(self, id, transactions, prevblock_hash=""):
        time_stamp = time.time()
        new_block = Block(id, transactions,time_stamp,prevblock_hash, None)

        #hashing the block
        new_block_dict = dataclasses.asdict(new_block)
        encoded_block_data = json.dumps(new_block_dict).encode()
        hash_the_block = self.hash_theblock(encoded_block_data)
        new_block.block_hash = hash_the_block
        self.blocks.append(new_block)

    def get_last_block(self):
        return self.blocks[-1]

    def create_transaction(self, id, amount, from__, to__):
        new_trans =  {"id": id, "amount":amount, "from":from__, "to":to__}

        for account in self.accounts:
            if account.address == from__:
                account.coins -= amount

            if account.address == to__:
                account.coins += amount


        return new_trans


    def hash_theblock(self, data):
        return hashlib.sha256(data).hexdigest()


    # NOT REQUIRED BY HW-1
    def create_account(self, coins=100):
        address = '0b'+''.join(random.choices(string.ascii_letters, k=5))
        new_account = Account(address, coins)
        self.accounts.append(new_account)
        return new_account


def main():

    #Decoration
    print("")
    print("########################################################")
    print("############# THIS IS A SIMPLE BLOCKCHAIN ##############")
    print("#############@@ Author: Philbert Bahati @@##############")
    print("########################################################")
    print("")

    ##STEP-1: Initialize the blockchain
    print(">>Creating the blockchain......")
    time.sleep(1)
    print(">>Generating the GENESIS block......")
    print("")
    blockchain = Blockchain()
    time.sleep(1)
    print("DONE....")
    print("")

    ##step-2: Get the last Block. For this time it should be the genesis block
    print("Let's get the latest block infomation for now, ")
    print("Which is the Genesis block for now")
    print("")
    last_block = blockchain.get_last_block()
    print("---------------------------------------------------------------")
    print("The last Block ID: ", last_block.id)
    print("The last block hash Value : ", last_block.block_hash)
    print("The last block Timestamp : ", last_block.timestamp)
    print("The last block List of transactions : ", last_block.transactions)
    print("---------------------------------------------------------------")
    print("")



    ##STEP-3: Create Accounts(users) on the block | at least 3.
    time.sleep(2)
    print("Let's create 3 addresses(users) in the blockchain")
    print("DONE...")
    time.sleep(1)
    print("")
    alice_ = blockchain.create_account(150) # Alice accounnt
    bob_ = blockchain.create_account(750) # Bob accounnt
    zeke_ = blockchain.create_account(80)  # Zeke accounnt
    
    print(">> Address-1 (Let's call her Alice) :", alice_.address)
    print(">> Address-2 (Let's call her Bob) :", bob_.address)
    print(">> Address-3 (Let's call her Zeke) :", zeke_.address)
    print("")


    ##STEP-4: Initiate  transactions| at least 2.
    print("Let's create some transaction in the blockchain")
    time.sleep(1)
    transaction_1 = blockchain.create_transaction(0, 10, alice_.address, bob_.address)  #From Alice to Bob
    transaction_2 = blockchain.create_transaction(1, 25,bob_.address,zeke_.address)  #From Bob to zeke
    print(">> TRANSACTION-1: Sending.. ", transaction_1["amount"], "Coins.  [FROM]:",transaction_1["from"], " [TO]:", transaction_1["to"])
    time.sleep(0.5)
    print(">> TRANSACTION-2: Sending.. ", transaction_2["amount"], "Coins.  [FROM]:",transaction_2["from"], " [TO]:", transaction_2["to"])
    time.sleep(0.5)
    print(">> Adding Transactions to the block...")


    ##STEP-5: Create a block. Add those 2 transaction in a block.
    prev_hash = blockchain.get_last_block()
    prev_hash = prev_hash.block_hash
    blockchain.create_block(1, [transaction_1, transaction_2], prev_hash)
    print("DONE...")
    print("")

    ##STEP-6: Get the last block.
    print("Let's get the latest block infomation Again, ")
    print("It should include the latest transactions..")
    print("")
    time.sleep(1)


    last_block = blockchain.get_last_block()
    print("---------------------------------------------------------------")
    print("The last Block ID: ", last_block.id)
    print("The last block hash Value : ", last_block.block_hash)
    print("The last block Timestamp : ", last_block.timestamp)
    print("The last block List of transactions : ", last_block.transactions)
    print("---------------------------------------------------------------")
    print("")
    print("DONE & BYE")





if __name__ == "__main__":
    main()
