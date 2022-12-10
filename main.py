try:
    list_odd=[]
    list_even=[]
    list_9=[]
    begin=int(input('beginj->'))
    end=int(input('beginj->'))
    for i in range(begin,end+1):
        if i %2==0:
            list_even.append(i)
        elif i %2!=0:
            list_odd.append(i)
        elif i %9==0:
            list_9.append(i)
    print(f'Even numbers: {list_even}\nsum of even:{sum(list_even)}\navg of even:{sum(list_even) / len(list_even)}\n')
    print(f'list_odd: {list_odd}\nsum of odd:{sum(list_odd)}\navg of odd:{sum(list_odd) / len(list_odd)}\n')
    print(f'nine numbers: {list_9}\nsum of nine:{sum(list_9)}\navg of nine:{sum(list_9) / len(list_9)}\n')


except Exception as ex:
    print(f"error information:{ex}")
finally:
    print("exit")