player_inventory = {
    'sword' : 1,
    'axe' : 1,
    'mana_potion' : 1,
    'torch' : 22,
    'gold' : 99
}

dragon_loot = ['gold', 'gold', 'axe', 'gold', 'torch', 'mana_potion', 'mana_potion']


def display_inventory(inventory):
    print('Inwentarz:')
    item_total = 0

    for k, v in inventory.items():
        print(f'{v} of {k}')
        item_total += v
    
    print(f'There are {str(item_total)} total items in inventory')

def add_to_inventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item, 0)
        if item in inventory.keys():
            inventory[item] += 1




display_inventory(player_inventory)
add_to_inventory(player_inventory, dragon_loot)
display_inventory(player_inventory)
