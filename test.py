import csv

def main():

    what = input('1: 이름 검색 / 2: 특성 검색\n')
    
    if what == '이름' or what == '1':
        name = input('Name\n')
        with open("./리스트.csv", 'r') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                if name in row:
                    print(row)
    else:
        type1 = input('Type 1\n')
        type2 = input('Type 2\n')
        with open("./리스트.csv", 'r') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                if type1 in row:
                    if type2 != '':
                        if type2 in row:
                            print(row)
                    else:
                        print(row)

    print('-------굿--------')

    

if __name__ == '__main__':
    main()