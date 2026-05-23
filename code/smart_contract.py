# Smart Contract Simulation

balance = 1000
withdraw_amount = 300

print("📜 Smart Contract Activated")
print("💳 Current Balance:", balance)

# Contract logic
if withdraw_amount <= balance:
    balance -= withdraw_amount
    print("✅ Withdrawal Successful")
    print("💰 Withdraw Amount:", withdraw_amount)

else:
    print("⚠️ Insufficient Balance")

print("🏦 Remaining Balance:", balance)
