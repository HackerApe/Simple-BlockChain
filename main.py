import hashlib


class MegaBlock:
    def __init__(self, prev_hash, transactions):
        self.prev_hash = prev_hash
        self.transactions = transactions

        self.block_data = " - ".join(transactions) + " - " + prev_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()


t1 = "Shin sends 2 MB to Mike"
t2 = "Daniel sends 4.1 MB to Mike"
t3 = "Mike sends 5 MB to Bob"
t4 = "John sends 12 MB to Marie"
t5 = "Jay sends 0.3 MB to John"
t6 = "Marie sends 100 MB to Jay"

initial_block = MegaBlock("Initial String", [t1, t2])
print(initial_block.block_data)
print(initial_block.block_hash)

second_block = MegaBlock(initial_block.block_hash, [t3, t4])
print(second_block.block_data)
print(second_block.block_hash)
