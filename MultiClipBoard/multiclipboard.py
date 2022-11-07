'''
Copies items in users clipboard
store multiple items from users' clipboard
takes in commands to save, view, list, load
'''

import clipboard
import sys
import json

'''
get data saved on users clipboard
data = clipboard.paste()

get data loaded to users clipboard

clipboard.copy('Hello World')
print(clipboard.paste())
'''

# print(sys.argv[2:]) slice the first 2 cmd line args passed

SAVED_DATA = 'clipboard.json'
# save data to some file
def save_data(file, data):
    with open(file, 'w') as f:
        json.dump(data, f)
# save_data('clipboard.json', {'key': 'value'})

# read the json file
def load_data(filepath):
    # handle error when the filename does not exist
    try:
        with open(filepath, 'r') as r:
            data = json.load(r)
            return data
    except:
        return {}
    

# print(load_data('clipboard.json'))


if len(sys.argv) == 2:
    command= sys.argv[1]
    data = load_data(SAVED_DATA)

    if command == 'save':
        key = input('Enter a key:')
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)
    elif command == 'load':
        key = input('Enter a key: ')
        if key in data:
            clipboard.copy(data[key])
            print('Data copied to Clipboard')
        else:
            print('Key DOES NOT exist!')

    elif command == 'list':
        print(data)
    else:
        print('Command Unknown')
else:
    print('Please pass in exactly 1 command')

