def test_sanity_1(a):
    order = {"apple": 1}
    warehouses = [{"name": "owd", "inventory": {"apple": 1}}]

    shipment = a.allocate(order, warehouses)

    assert shipment == [{"owd": {"apple": 1}}]

def test_sanity_2(a):
    order = {"apple": 1}
    warehouses = [{"name": "owd", "inventory": {"apple": 0}}]
    shipment = a.allocate(order, warehouses)
    assert shipment == [] 

def test_sanity_3(a):
    order = {"apple": 10}
    warehouses = [{"name": "owd", "inventory": {"apple": 5}}, 
                   {"name": "dm", "inventory": {"apple": 5}}]

    shipment = a.allocate(order, warehouses)

    assert shipment == [{"dm": {"apple": 5}}, 
                        {"owd": {"apple": 5}}]

def test_empty_order_warehouse(a):
    order = {}
    warehouses = []
    shipment = a.allocate(order, warehouses)
    assert shipment == []

def test_empty_order(a):
    order = {}
    warehouses = [{"name": "king", "inventory": {"apple": 10}}]
    shipment = a.allocate(order, warehouses)
    assert shipment == []

def test_empty_warehouse(a):
    order = {"banana": 5, "orange": 7, "apple": 2}
    warehouses = []
    shipment = a.allocate(order, warehouses)
    assert shipment == []

def test_zero_warehouse(a):
    order = {"banana": 1}
    warehouses = [{"name": "dm", "inventory": {"banana": 0}}]
    shipment = a.allocate(order, warehouses)
    assert shipment == []

def test_single_item(a):
    order = {"apple": 2}
    warehouses = [{"name": "king", "inventory": {"apple": 8}}]
    shipment = a.allocate(order, warehouses)
    assert shipment == [{"king": {"apple": 2}}] 

def test_single_item_across_warehouses_1(a):
    order = {"apple": 10}
    warehouses = [{"name": "queen", "inventory": {"apple": 3}},
                  {"name": "king", "inventory": {"apple": 5}},
                  {"name": "jack", "inventory": {"apple": 2}}]

    shipment = a.allocate(order, warehouses)

    assert shipment == [{"jack": {"apple": 2}},
                        {"king": {"apple": 5}},
                        {"queen": {"apple": 3}}] 
    
def test_single_item_across_warehouses_2(a):
    order = {"apple": 10}
    warehouses = [{"name": "queen", "inventory": {"apple": 6}},
                  {"name": "king", "inventory": {"apple": 8}},
                  {"name": "jack", "inventory": {"apple": 10}}]

    shipment = a.allocate(order, warehouses)

    assert shipment == [{"king": {"apple": 4}},
                        {"queen": {"apple": 6}}] 

def test_multiple_items_1(a):
    order = {"apple": 10, "banana": 7, "orange": 20}
    warehouses = [{"name": "heart", 
                   "inventory": {"orange": 20, 
                                 "apple": 12, 
                                 "banana": 10}}]

    shipment = a.allocate(order, warehouses)

    assert shipment == [{"heart": {"apple": 10, "banana": 7, "orange": 20}}]

def test_multiple_items_2(a):
    order = {"apple": 10, "banana": 7, "orange": 20}
    warehouses = [{"name": "heart",
                   "inventory": {"orange": 18,
                                 "apple": 10, 
                                 "banana": 7}}]

    shipment = a.allocate(order, warehouses)

    assert shipment == []

def test_multiple_items_across_warehouses_1(a):
    order = {"plum": 8, "cucumber": 15, "melon": 10}
    warehouses = [{"name": "red", 
                   "inventory": {"banana": 20, "plum": 20}},
                  {"name": "green",
                   "inventory": {"melon": 7, "apple": 10}},
                  {"name": "blue",
                   "inventory": {"melon": 20, "cucumber": 100}}]

    shipment = a.allocate(order, warehouses)

    assert shipment == [{"blue": {"melon": 3, "cucumber": 15}},
                        {"green": {"melon": 7}},
                        {"red": {"plum": 8}}]

def test_multiple_items_across_warehouses_2(a):
    order = {"rose": 20, "pear": 15, "broccolli": 10, "banana": 8}
    warehouses = [{"name": "yellow",
                   "inventory": {"banana": 2, "broccolli": 8}},
                  {"name": "violet",
                   "inventory": {"pear": 6, "broccolli": 20, "banana": 5}},
                  {"name": "white",
                   "inventory": {"pear": 5, "broccolli": 2, "banana": 2}},
                  {"name": "black",
                   "inventory": {"rose": 20, "pear": 10, "banana": 10}}]

    shipment = a.allocate(order, warehouses)

    assert shipment == [{"black": {"rose": 20, "pear": 4}},
        {"violet": {"pear": 6, "broccolli": 2, "banana": 5}},
        {"white": {"pear": 5, "banana": 1}},
        {"yellow": {"banana": 2, "broccolli": 8}}]

def test_multiple_items_across_warehouses_3(a):
    order = {"rose": 10, "apple": 20, "orange": 10}
    warehouses = [{"name": "john",
                   "inventory": {"orange": 4, "apple": 2, "rose": 5}},
                  {"name": "nick",
                   "inventory": {"apple": 8, "rose": 2, "orange": 2}},
                  {"name": "paul",
                   "inventory": {"apple": 12, "orange": 10, "rose": 10}}]
    shipment = a.allocate(order, warehouses)
    assert shipment == [{"john": {"orange": 4, "apple": 2, "rose": 5}},
        {"nick": {"apple": 8, "rose": 2, "orange": 2}},
        {"paul": {"apple": 10, "orange": 4, "rose": 3}}]

def test_multiple_items_across_warehouses_not_enough_1(a):
    order = {"apple": 10, "orange": 20, "banana": 10}  
    warehouses = [{"name": "red",
                   "inventory": {"apple": 2, "orange": 10}},
                  {"name": "blue",
                   "inventory": {"banana": 8}}]
    shipment = a.allocate(order, warehouses)
    assert shipment == []

def test_multiple_items_across_warehouses_not_enough_2(a):
    order = {"apple": 10, "orange": 20, "banana": 10}
    warehouses = [{"name": "green",
                   "inventory": {"apple": 10, "orange": 5}},
                  {"name": "blue",
                   "inventory": {"apple": 10, "orange": 15, "banana": 2}},
                  {"name": "white",
                   "inventory": {"banana": 2, "apple": 10}}]
    shipment = a.allocate(order, warehouses)
    assert shipment == []

