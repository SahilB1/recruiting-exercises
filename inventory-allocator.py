def shipments(order, warehouse_inventory):
    print("order:", order)
    print("warehouse inventory:", warehouse_inventory)
    print()
    best_order = []

    # create a map to count the total inventory of each item in warehouse to see if there's enough to meet order
    item_total = 0
    item_count_map = {key:0 for key in order}

    for item in order:
        for obj in warehouse_inventory:
            if item in obj['inventory'].keys():
                item_total += obj['inventory'][item]
        item_count_map[item] = item_total
        item_total = 0

    # check to see that the total inventory of each item in order placed is enough to satisfy order and add to best order array
    for item in order:
        for obj in warehouse_inventory:
            if item in obj['inventory'].keys() and item_count_map[item] >= order[item] and order[item] > 0:
                best_order.append({obj['name']: {item: min(obj['inventory'][item], order[item])}})
                order[item] -= obj['inventory'][item]
                
    
    print("optimized order:", best_order)
    return best_order

order_1 = {'apple': 5, 'banana': 5, 'orange': 5}
inventory_1 = [ { 'name': 'owd', 'inventory': { 'apple': 5, 'orange': 10 } }, { 'name': 'dm', 'inventory': { 'banana': 5, 'orange': 10 } } ]

order_2 = {'apple': 1}
inventory_2 = [{'name': 'owd', 'inventory': {'apple': 1}}]

order_3 = {'apple': 10}
inventory_3 = [{ 'name': 'owd', 'inventory': { 'apple': 5 } }, { 'name': 'dm', 'inventory': { 'apple': 5 }}]

order_4 = {}
inventory_4 = {}

order_5 = {}
inventory_5 = [{ 'name': 'owd', 'inventory': { 'apple': 5 } }, { 'name': 'dm', 'inventory': { 'apple': 5 }}]

order_6 = {'apple': 10}
inventory_6 = [{ 'name': 'owd', 'inventory': { 'apple': 5 } }, { 'name': 'dm', 'inventory': { 'orange': 5 }}]

print()
print("TEST CASES")
print('----------------------------------')
print()
shipments(order_1, inventory_1)
print()
print('----------------------------------')
print()
shipments(order_2, inventory_2)
print()
print('----------------------------------')
print()
shipments(order_3, inventory_3)
print()
print('----------------------------------')
print()
shipments(order_4, inventory_4)
print()
print('----------------------------------')
print()
shipments(order_5, inventory_5)
print()
print('----------------------------------')
print()
shipments(order_6, inventory_6)
