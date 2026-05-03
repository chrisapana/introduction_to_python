# import  module by package


from pack import items
# OR
# from pack.items import calc_shipping
# from pack.items import is_item

print(items.calc_shipping())
print(items.is_item)


'''
# import specific item or function
from  pack.items import calc_shipping
from  pack.items import is_item

print(is_item.get("men", "shoe"))
print(is_item.get("man", "like jack"))

print(calc_shipping())
'''

# OR


"""
# import sigle  module
import pack.items
isCalc = pack.items.calc_shipping()

print(isCalc)
"""

