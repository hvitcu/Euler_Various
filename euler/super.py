import random

#the item class has a name and price properties
class Item( object ):
    def __init__( self, item_name, price ):
        self.item_name = item_name
        self.price = price
    def get_item_name( self ):
        return self.item_name
    def get_price( self ):
        return self.price

def create_item_list( *items ):
    ls = []
    for item in items:
        #create random item list i.e. random shopping cart
        items_ls_size = random.randrange( 1,10 )
        for i in range( items_ls_size ):
            ls.append( item )
    #shuffle the list
    random.shuffle( ls )
    return ls

# create offer using the name the required number of items needed to hit the offer and the price
def create_offer( item_name, num_req, price ):
    offer = { 'item_name': item_name, 'num_req': num_req, 'offer_price': price }
    return offer

# calculate the total shopping cart value
def calculate_total( items_ls, offer_ls ):
    # get distinct items
    distinct = set( item_ls )
    no_offer_items = set( item_ls )

    total_offer = 0
    total_no_offer = 0

    for item in distinct:
        for offer in offer_ls:
            if item.get_item_name() == offer['item_name']:
                # calculate how many times the offer price can be applied and do the calculation for the total
                count = items_ls.count( item )
                num_required = offer['num_req']

                total_offer += count / num_required * offer['offer_price']
                # calculate the total for number of items that do not fit inside the offer

                total_offer += count % num_required * item.get_price()
                # flag the items for which there are no offers
                no_offer_items.remove( item )

    # go through the items for which there are no offers and calculate the total
    for item in no_offer_items:
        total_no_offer += item_ls.count( item ) * item.get_price()

    return { 'offer total':total_offer, 'no offer total':total_no_offer }

if __name__ == '__main__':
    # create items
    A = Item( 'A', 2.00 )
    B = Item( 'B', 1.50 )
    C = Item( 'C', 1.25 )
    D = Item( 'D', 1.00 )

    # create item list i.e. the shopping cart
    item_ls = create_item_list( A,B,C,D )

    # create the list of offers
    offer_ls = []
    offer_ls.append( create_offer( 'A', 2, 3.00 ) )
    offer_ls.append( create_offer( 'B', 3, 3.50 ) )

    # calculate the total shopping cart value
    total =  calculate_total( item_ls, offer_ls )

    #print the total to console
    print total
    print "--------------"*100
    print 'Total shopping cart value %s' % ( total['no offer total'] + total['offer total'] )