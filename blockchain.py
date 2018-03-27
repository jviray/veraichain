import hashlib
import json
from time import time

class Blockchain():
	def __init__(self):
		"""Initializes the blockcahin"""
		self.chain =[]
		self.current_transactions = []

		# Create the genesis block
		self.new_block(previous_hash=1, proof=100)


	def new_block(self, proof, previous_hash=None):
		"""
		Creates a new block and adds it to the chain
		
		proof: <int> Proof return by the Proof of Work (POW) algorithm
		previous_hash: (Optional) <str> Hash of previous block

		Returns <dict> a new block
		"""

		block = {
			'index': len(self.chain) + 1,
			'timestamp': time(),
			'transactions': self.current_transactions,
			'proof': proof,
			'previous_hash': previous_hash or self.hash(self.chain[-1]), # !!!
		}

		# Reset the current list of transactions
		self.current_transactions = []

		self.chain.append(block)
		return block


	def new_transaction(self, sender, recipient, amount):
		"""
		Creates a new transaction to the list of transactions

		sender: <str> Address of the sender
		recipient: <str> Address fo the recipient
		amount: Amoutn exchanged

		Returns the index of the block that will hold this transaction
		"""

		self.current_transactions.append({
			'sender': sender,
			'recipient': recipient,
			'amount': amount,
		})


	@staticmethod # !!!
	def hash(block):
		"""
		Creates a SHA-256 hash of a block

		block: <dict> Block
		"""

		# Make sure the dict is ordered, or hashes will be inconsistent
		block_string = json.dumps(block, sort_keys=True).encode()
		return hashlib.sha256(block_string).hexdigest()
		

	@property
	def last_block(self):
		"""Returns the last block in the chain"""
		return self.chain[-1]

	def new_transaction(self, sender, recipient, amount):
		"""
		Creates a new transaction to go into the next mined block
		
		sender: <str> Address of the sender
		recipient: <str> Adress of the recipient
		amount: <int> Amount exchanged

		Returns the index of the block that will hold this transaction
		"""

		self.current_transactions.append({
			'sender': sender,
			'recipient': recipient,
			'amount': amount,
		})

		return self.last_block['index'] + 1