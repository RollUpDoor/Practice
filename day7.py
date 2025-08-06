def main():
    """
    題目
    建立一個 tuple 裡面有四個食物名稱，
    請把所有食物名字用 for 迴圈印出來，並試著印出第二個食物。
    """
    food=("apple","rice","cake","cookie")
    for i in range(4):
        print(food[i])
    print(f"第二個食物名字是:{food[1]}")

    """
    建立一個 list 裡面有五個數字，
    請計算總和、平均值、最大值與最小值。
    """
    number_list = [1,2,3,4,5]
    print(sum(number_list))
    print(sum(number_list)/len(number_list))
    print(max(number_list))
    print(min(number_list))

    """
    建立一個 dict，內容包含一個人的「名字」、「年齡」、「興趣」。
    請印出所有 key，所有 value，然後用 for 迴圈把 key 和 value 一起印出來。
    """
    person=[]
    for i in range(3):
        name=input('name:')
        age=input('age:')
        hobby=input('hobby:')

        p_dict={}
        p_dict['name']=name
        p_dict['age'] = age
        p_dict['hobby'] = hobby

        person.append(p_dict)
    print(person)

    for info in person:
        print("key：", list(info.keys()))
        print("value：", list(info.values()))
        print("key-value：", list(info.items()))
        print(f"我是{info['name']}，今年{info['age']}歲，興趣是{info['hobby']}。")
"""
小提醒
用 info['name'] 這種「key」的方式取值

你不能對 dict 用數字 index，dict 不是 list
"""
if __name__ == "__main__":
    main()
