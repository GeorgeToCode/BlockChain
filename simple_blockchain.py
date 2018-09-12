import hashlib as hsh
import datetime

class Block:
    def __init__(self,index,timestamp,data,previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()
        
    def hash_block(self):
        sha = hsh.sha256()
        sha.update(( str(self.index) +
                    str(self.timestamp) +
                    str(self.data) +
                    str(self.previous_hash) ).encode("utf-8"))
        return sha.hexdigest()

def create_genesis_block():
    return Block(0,datetime.datetime.now(),"Genesis block","0")


def next_block(prev_block):
    this_index = prev_block.index + 1
    this_timestamp = datetime.datetime.now()
    this_data = "I am block " + str(this_index)
    previous_hash = prev_block.hash
    return Block(this_index,this_timestamp,this_data,previous_hash)


blockchain = [create_genesis_block()]
previous_block = blockchain[0]

num_blk = 20

for i in range(0,num_blk):
    block_to_add = next_block(previous_block)
    blockchain.append(block_to_add)
    previous_block = block_to_add
    print("Block #{} ".format(block_to_add.index))
    print("hash : {} \n".format(block_to_add.hash))
