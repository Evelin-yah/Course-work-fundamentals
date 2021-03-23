lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
repairs_cost = 0

for lost in range(1, lost_fights + 1):

    if lost % 2 == 0:
        repairs_cost += helmet_price
    if lost % 3 == 0:
        repairs_cost += sword_price
    if lost % 6 == 0:
        repairs_cost += shield_price
    if lost % 12 == 0:
        repairs_cost += armor_price

print(f"Gladiator expenses: {repairs_cost:.2f} aureus")