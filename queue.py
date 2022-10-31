from collections import deque

# এখানে যে আগে আসবে সে আগে যাবে 

bank = deque(["Anis","Rokon","Rabbi"])

print(bank)

bank.popleft()
print(bank)

bank.popleft()
print(bank)

bank.popleft()
if not bank:
    print("No person bank")
