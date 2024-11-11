import sys
input = sys.stdin.readline

def menu(count, dictionary):
    for _ in range(count):
        menu, price = input().split()
        price = int(price)
        dictionary[menu] = price

a, b, c = map(int, input().split())

normal = {}
special = {}
service = []

menu(a, normal)
menu(b, special)
for _ in range(c):
    menu_name = input().strip()
    service.append(menu_name)

normal_price = 0
special_price = 0
service_count = 0

n = int(input())
for _ in range(n):
    order = input().strip()
    if order in normal.keys():
        normal_price += normal[order]
    elif order in special.keys():
        special_price += special[order]
    elif order in service:
        if service_count == 0:
            service_count += 1
        else:
            print("No")
            sys.exit()

if special_price > 0 and normal_price < 20000:
    print("No")
elif special_price + normal_price < 50000 and service_count > 0:
    print("No")
elif service_count > 1:
    print("No")
else:
    print("Okay")