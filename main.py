try:
    sign=input('sign->')
    len=int(input("len->"))
    trig= input("vert=v|hor=h")
    for i in range(0,len):
        if trig=="v":
            print(sign)
        elif trig=="h":
            print(sign,end="")
        else:
            raise Exception("inccorect choose of trig")
except Exception as ex:
    print(f"error information:{ex}")
finally:
    print("\nexit")