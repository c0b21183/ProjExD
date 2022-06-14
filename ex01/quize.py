from random import randint
def main():
    print("問題:")
    a = shutudai()
    kaitou(a)

def shutudai():
    q = {}
    q[0] = ("サザエの旦那の名前は？", "マスオ", "ますお")
    q[1] = ("カツオの妹の名前は？", "ワカメ", "わかめ")
    q[2] = ("タラオはカツオから見てどんな関係？", "甥", "おい", "甥っ子", "おいっこ")
    s = randint(0, 2)
    print(q[s][0])
    return q[s]

def kaitou(a):
    kai = input("答え:")
    if kai in a:
        print("正解!")
    else:
        print("不正解")

if __name__ ==  "__main__":
    main() 