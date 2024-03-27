key_x = ''
key_y = ''
api_x = ''
api_y = 'your question'

api_key_x = 0
api_key_y = 0
api_key_z = 0

api_total_result = 0

api_num = 0

api_valut = 0

print_y = set()

def print_x(text):
    if text not in print_y:
        print(text)
        print_y.add(text)

for x in key_x:
    for api_xx in api_x:
        if x in api_xx:
            if api_y in api_xx:
                print_x(api_xx)
                api_key_x += 1
                if api_valut < 2:
                    api_valut += 1

for y in key_y:
    for api_yy in api_x:
        if y in api_yy:
            if api_y in api_yy:
                print_x(api_yy)
                api_key_y += 1
                if api_valut < 2:
                    api_valut += 1

if(api_valut < api_num):
    print('error api_valut')
else:
    if api_valut == 1:
        api_dec = '50%'
    elif api_valut == 2:
        api_dec = '100%'
    elif api_valut == 0:
        api_dec = '0%'
        for z in api_x:
            if api_y in z:
                print_x(z)
                api_key_z += 1
    else:
        api_dec = 'err invalid api_valut in api_dec'

api_total_result = api_key_x + api_key_y + api_key_z
