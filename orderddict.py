#You will have to initialize your dict as OrderedDict. Create a new empty
#OrderedDict,
#go through all keys of the original dictionary and insert before/after
#when the key name matches.


from pprint import pprint
from collections import OrderedDict


def insert_key_value(a_dict, key, pos_key, value):
    new_dict = OrderedDict()
    for k, v in a_dict.items():
        if k==pos_key:
            new_dict[key] = value  # insert new key
        new_dict[k] = v
    return new_dict


mydict = OrderedDict([('Name', 'Zara'), ('Age', 7), ('Class', 'First')])
my_new_dict = insert_key_value(mydict, "Phone", "Name", "1234")
pprint(my_new_dict)
