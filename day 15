#coffee maker


menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            'milk': 0,
            "coffee": 18,
        },
        "cost": 15,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 25,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 30,
    }
}

Water = 100
Milk = 500
Coffee = 760


def report(ch,water,milk,coffee):
    water = water - menu[ch]['ingredients']['water']
    milk = milk - menu[ch]['ingredients']['milk']
    coffee = coffee - menu[ch]['ingredients']['coffee']
    return f'Water:{water}\nMilk: {milk}\nCoffee: {coffee}\n\n'


def make(ch, water, milk, coffee):
    water = water - menu[ch]['ingredients']['water']
    milk = milk - menu[ch]['ingredients']['milk']
    coffee = coffee - menu[ch]['ingredients']['coffee']
    if water < 0 or milk < 0 or coffee < 0:
        water = water + menu[ch]['ingredients']['water']
        milk = milk + menu[ch]['ingredients']['milk']
        coffee = coffee + menu[ch]['ingredients']['coffee']
        return 'Insufficient Ingredients'
    else:
        return f'Your {ch} is ready!'


def bill(coin, costs):
    total = coin[0]+coin[1]*2+coin[2]*5+coin[3]*10+coin[4]*20
    if total == cost:
        return 'Transaction Complete'
    elif total > cost:
        return f'Here is your change:{total - cost} Rupees\nTransaction Complete'
    else:
        return 'Insufficient Money, Money refunded.'


cost = 0
c = 'yes'
while c == 'yes':
    choice = input('What would you like? (espresso/latte/cappuccino): ').lower()

    if make(choice, Water, Milk, Coffee) == f'Your {choice} is ready!':
        cost += menu[choice]['cost']
    elif make(choice, Water, Milk, Coffee) == 'Insufficient Ingredients':
        print(make(choice, Water, Milk, Coffee))
    print(f'Your amount is {cost} Rupees\n')
    rep = input('Do you want to Generate the report? yes or no ').lower()
    if rep == 'yes':
        print(report(choice, Water, Milk, Coffee))
    c = input('Do you want something else? (yes or no)').lower()
print(f'Your final amount is {cost} Rupees\nPlease insert coins')

coin_names = ['One', 'Two', 'Five', 'Ten', 'Twenty']
coins = []
for a in coin_names:
    coi = int(input(f'How many {a} Rupee coins: '))
    coins.append(coi)

t = bill(coins, cost)
print(t)
