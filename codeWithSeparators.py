# this program print to console item which you give it with special order and style


def defining_list():
    list = []
    while True: 
        print('Type the name of the item. If you want to stop typing next items, just press the enter')
        name = input()
        if name == '':
            break
        list.append(name)
    add_separator(list)





def add_separator(some_list):
    lastWord = ''
    for i in range(len(some_list)):
        if i == 0:
            lastWord += some_list[0]
        elif i == (len(some_list ) - 1):
            lastWord += f' and {some_list[i]}'
        else:
            lastWord += f', {some_list[i]}'
    print(lastWord)

def main():
    print('Ok, give me there list of your items')
    defining_list()

main()

