def list_to_dict(my_list):
    return {'i': list(filter(lambda item: isinstance(item, int), my_list)),
            'f': list(filter(lambda item: isinstance(item, float), my_list)),
            'c': list(filter(lambda item: isinstance(item, str) and len(item) == 1, my_list)),
            'o': list(filter(
                lambda item: type(item).__name__ not in ('int', 'float') and (isinstance(item, str) and len(item) > 1),
                my_list))}

my_list = [10,4.0,'a','c','acs']
print(list_to_dict(my_list))