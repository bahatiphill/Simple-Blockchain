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
        #genesis_block_hash =  self.hash_theblock(b"genesis")
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


    # NOT REQUIRED BY HW
    def create_account(self, coins=100):
        address = '0b'+''.join(random.choices(string.ascii_letters, k=5))
        #new_account = {"address": address, "coins":coins}
        new_account = Account(address, coins)
        self.accounts.append(new_account)
        return new_account


def main():

    ##STEP-1: Initialize the blockchain
    blockchain = Blockchain()

    ##STEP-2: Create Accounts(users) on the block | at least 3.
    alice_ = blockchain.create_account(150) # Alice accounnt
    bob_ = blockchain.create_account(750) # Bob accounnt
    zeke_ = blockchain.create_account(80)  # Zeke accounnt

    ##step-2.5: Get the last Block. For this time it should be the genesis block
    last_block = blockchain.get_last_block()
    print("The last Block ID: ", last_block.id)
    print("The last block hash Value : ", last_block.block_hash)

    ##STEP-3: Initiate  transactions| at least 2.
    transaction_1 = blockchain.create_transaction(0, 10, alice_.address, bob_.address)  #From Alice to Bob
    transaction_2 = blockchain.create_transaction(1, 25,bob_.address,zeke_.address)  #From Bob to zeke


    ##STEP-4: Create a block. Add those 2 transaction in a block.
    prev_hash = blockchain.get_last_block()
    prev_hash = prev_hash.block_hash
    blockchain.create_block(1, [transaction_1, transaction_2], prev_hash)
    
    ##STEP-7: Get the last block.
    last_block = blockchain.get_last_block()
    print("")
    print("The last Block ID: ", last_block.id)
    print("The last block hash Value : ", last_block.block_hash)




if __name__ == "__main__":
    main()
