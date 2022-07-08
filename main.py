import hashlib


class MegaBlock:
    def __init__(self, prev_hash, transactions):
        self.prev_hash = prev_hash
        self.transactions = transactions
