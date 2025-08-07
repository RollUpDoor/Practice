def main():
    """
    Day8-專精練習 Tuple 我今天要把Tuple瞭解熟悉
    """

    #  基本建立與取值，建立一個含三個動物的 tuple，請印出第二個動物
    animal=('cat','dog','bird')
    print("第1題:")
    print(animal[1])

    #  題目：用 for 迴圈把這個 tuple 所有動物都印出來。 印出結果：
    print("第2題:")
    for i in animal:
        print(i)

    #  題目：用切片印出 tuple 的前兩個元素。
    print("第3題:")
    print(animal[:2])

    #  反轉
    print("第4題:")
    print(animal[::-1])

    # 如果題目要「只含一個城市」的 tuple，必須這樣寫：
    print("第5題:")
    city=("Taipei",)
    print(type(city))

    # 將一個 tuple 轉成 list，新增一個資料，再轉回 tuple 並印出
    print("第6題:")
    a_list=[]
    for i in animal:
        a_list.append(i)
    a_list.append('fish')

    animal2=tuple(a_list)
    print(animal2)
    """
    第六題解答
    你可以這樣做（步驟提示）：
    先有一個 tuple
    例如：animal = ('cat', 'dog', 'bird')

    把 tuple 轉成 list
    用 list(你的tuple名)
    例如：animal_list = list(animal)
    
    用 list 的 append 新增一個資料
    例如：animal_list.append('fish')
    
    把 list 轉回 tuple
    用 tuple(你的list名)
    例如：animal = tuple(animal_list)
    
    印出來
    """
    print("第7題:")
    a,b=(100,200)
    print(a,b)

    print("第8題:")
    for idx, i in enumerate(animal,1):
        print(f'{idx}: {i}')

    print("第9題:")
    for i in animal2:
        if i == 'dog':
            print("True")
    """
    第九題精簡寫法:
    print("第9題:")
    print('dog' in animal2)
    """

    print("第10題:")
    ten=(3,'apple',(7,8))
    print(ten)
    """
    a, b, c = ("Amy", 20, "Taipei")
    print(a, b, c)
    """

    fruits = ("apple", "banana", "orange")
    # fruits[0] = "grape"  # 這行會報錯！tuple不能直接改 'tuple' object does not support item assignment



if __name__ == "__main__":
    main()
