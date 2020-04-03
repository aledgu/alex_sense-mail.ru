# tovar1 = {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.', 'название':'принтер', 'название':'ноут'}
# names = ('name', 'price', 'quantity')
all_dict = {}
poz_dict = {}
all_names = ['Компьютер', 'принтер', 'сканер']
all_price = [2000, 345, 345]
all_quantity = [2, 3, 4]
all_stic = ["шт", "шт", "шт"]
all_keys = ['название', 'цена', 'количество', 'ед.изм']
v = 1
# i = 0
s = 0
tovar_tuple = ()
tovar_list = []
# print(all_keys[s])
# print(all_names[s])
for i in range(len(all_names)):
    poz_dict[all_keys[s]] = all_names[i]
    print(poz_dict)
    poz_dict[all_keys[s + 1]] = all_price[i]
    print(poz_dict)
    poz_dict[all_keys[s + 2]] = all_quantity[i]
    print(poz_dict)
    poz_dict[all_keys[s + 3]] = all_stic[i]
    print(poz_dict)
    tovar_tuple = (i+1,poz_dict)
    print(tovar_tuple)
    tovar_list.append(tovar_tuple)
print(tovar_list)
# key_name = input('Vvedite key for name: ')
# all_keys.append(key_name)
# name_element = 1
# name = input(f'Vvedite {key_name} {name_element} producta(press enter for finish): ')
# while name != '':
#     all_names.append(name)
#     name_element += 1
#     name = input(f'Vvedite {key_name} {name_element} producta(press enter for finish): ')
# all_dict[key_name] = all_names

# key_price =  input('Vvedite key for price: ')
# all_keys.append(key_price)
# price_element = 1
# price = int(input(f'Vvedite {key_price} {price_element} producta(000 for finish): '))
# while price != 000:
#     all_price.append(price)
#     price_element += 1
#     price = int(input(f'Vvedite {key_price} {price_element} producta(000 for finish): '))
# all_dict[key_price] = all_price
#
# key_quantity = input('Vvedite key for quantity: ')
# all_keys.append(key_quantity)
# quantity_element = 1
# quantity = int(input(f'Vvedite {key_quantity} {quantity_element} producta(000 for finish): '))
# while quantity != 000:
#     all_quantity.append(quantity)
#     quantity_element += 1
#     quantity = int(input(f'Vvedite {key_quantity} {quantity_element} producta(000 for finish): '))
# all_dict[key_quantity] = all_quantity
#
# key_stic = input('Vvedite key for stic: ')
# all_keys.append(key_stic)
# stic_element = 1
# stic = input(f'Vvedite {key_stic} {stic_element} producta(end for finish): ')
# while stic != 'end':
#     all_stic.append(stic)
#     stic_element += 1
#     stic = input(f'Vvedite {key_stic} {stic_element} producta(end for finish): ')
# all_dict[key_stic] = all_stic

# print(all_names)
# print(all_price)
# print(all_quantity)
# print(all_stic)



# tovar_tuple = ()
# tovar_list =[]
# tovar2 = {}
# for t in range(0, len(all_names):
#     for i in names:
#         print('Vvedite', i, t+1, 'producta:')
#         a = input()
#         tovar2[i] = a
#     tovar_tuple = (t+1,tovar2)
#     print(tovar_tuple)
#     tovar_list.append(tovar_tuple)
# print(tovar_list)
