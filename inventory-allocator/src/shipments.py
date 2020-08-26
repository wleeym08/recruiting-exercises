class InventoryAllocator:
    """
    Implementing a class to produce cheapest shipment given the order and
    inventory information of warehouses.
    """

    def allocate(self, order, warehouses):
        """
        Arguments:
            - order:       A dict that includes info of the order.
            - warehouses:  A list of dict which includes info of the 
                           inventory stored in a warehouse. Warehouses are
                           ordered by their costs for shipment (ascending).
        Usage:
        >>> a = InventoryAllocator()
        >>> order = {'apple': 1}
        >>> warehouse = [{'name': 'owd', 'inventory': {'apple': 1}}]
        >>> a.allocate(order, warehouse)
        [{'owd': {'apple': 1}}]
        """

        shipment = []
        for w in warehouses:
            dist = {}
            finished_items = []

            # Iterate through each warehouse, prioritize cheaper warehouses 
            for item, order_amount in order.items():
                # Check item amount in stock, set 0 if out of stock
                stock_amount = w["inventory"].get(item, 0)
                if stock_amount > 0:
                    # Update the amount neeeded in the order
                    rest_amount = order_amount - stock_amount 
                    # How many of this kind of items we should get 
                    # from this warehouse 
                    dist[item] = stock_amount if rest_amount > 0 else order_amount 

                    # Update the remaining amount of the order, if it's 
                    # already fulfilled, remove this item from the order
                    if rest_amount > 0:
                        order[item] = rest_amount
                    else:
                        finished_items.append(item)

            for item in finished_items:
                del order[item]

            if dist:
                shipment.append({w["name"]: dist})
            
            # Check if we still need items for the order, if so 
            # return the sorted list of shipment
            if not order:
                return sorted(shipment, key=lambda x: list(x.keys())[0])
        
        # Return an empty list if the order cannot be satisfied under 
        # current situation
        return [] 
