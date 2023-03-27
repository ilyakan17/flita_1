multiplicity_1 = set()
multiplicity_2 = set()
digits = '1234567890'


def changer(str):
    k = 0
    for i in str:
        if i in digits:
            k += 1
        else:
            return str
    if k == len(str):
        return int(str)

def enter(a):
    try:
        inp = input("Write your elements separated by spaces: ").split(' ')
        for i in inp:
            a.add(changer(i))
    except:
        print("Try again, please")

def remove(d):
    elements = changer(input("Write element which you want to remove in set: "))
    if elements in d:
        d.remove(elements)
        print("Success")
    else:
        print("This element not in set")

def output(b):
    if len(b) == 0:
        print("Empty set(")
    else:
        print("Elements: ", *b)


def add(c):
    elements = changer(input("Write element which you want to enter in set: "))
    if elements not in c:
        c.add(elements)
        print("Success")
    else:
        print("This element is already exist")


def main():
    try:
        while True:
            print('Choose set, enter 1 or 2:')
            ans = int(input())
            print('Input elements - 1')
            print('Output elements - 2')
            print('Enter ONE element - 3')
            print('Remove ONE element - 4')
            print('Leave - 5')
            if ans == 1:
                while True:
                    make = int(input('Write 1,2,3,4 or 5: '))
                    if make == 1:
                        enter(multiplicity_1)
                    if make == 2:
                        output(multiplicity_1)
                    if make == 3:
                        add(multiplicity_1)
                    if make == 4:
                        remove(multiplicity_1)
                    if make == 5:
                        break
            elif ans == 2:
                while True:
                    make = int(input('Write 1,2,3,4 or 5: '))
                    if make == 1:
                        enter(multiplicity_2)
                    if make == 2:
                        output(multiplicity_2)
                    if make == 3:
                        add(multiplicity_2)
                    if make == 4:
                        remove(multiplicity_2)
                    if make == 5:
                        break
            else:
                print('Set is not exist:(')
    except:
        print('It is not number, please, write 1 or 2')
        main()

main()
