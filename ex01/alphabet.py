import random
import datetime

kaisu= 5
mozi = 10
chars = 2

def main():
    st = datetime.datetime.now()
    for _ in range(kaisu):
        kotae=mondai()
        f = ans(kotae)
        if f == 1:
            break
    ed = datetime.datetime.now()
    print(f"{(ed-st).seconds}秒かかりました")


def mondai():
    all_chr_lst=random.sample(alphabets,mozi)
    alphabets=[chr(c+65) for c in range(26)]
    print(f"対象文字:{all_chr_lst}")

    pre_char_lst=[zzzz]
    print(f"表示文字:{pre_char_lst}")
    return abs_char_lst

def ans(kotae):
    num = int(input("欠損文字はいくつあるでしょうか"))
    if num != kaisu:
        print("不正解")
        return 0 
    
 if __name__ ==  "__main__"
    main()
