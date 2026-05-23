# Blockchain Transaction Simulation

import random
import time

print("⛓ Blockchain Transaction Started")

time.sleep(1)

sender = "User_A"
receiver = "User_B"

amount = random.randint(10, 500)

print("📤 Sender:", sender)
print("📥 Receiver:", receiver)
print("💰 Amount:", amount, "Tokens")

time.sleep(1)

transaction_id = random.randint(100000, 999999)

print("🔐 Transaction ID:", transaction_id)
print("✅ Transaction Verified on Blockchain")
