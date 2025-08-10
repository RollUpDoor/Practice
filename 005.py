def main():
    """
    Day5-2025/08/04 List練習
    題目1：找最大/最小值、總和、平均
    給你一串年齡 list，自己算出最大、最小、總和、平均（不用套件）。
    題目2：把所有年齡都加1，然後印出新 list
    題目3：移除 list 裡所有小於18歲的資料
    題目4：反轉 list（讓最後一筆變第一筆）
    題目5：list 裡每個人都要印出「我是XX，今年XX歲」（搭配dict）
    """
    age_list=[5,10,15,20,25,30,35]
    print(f"age_list最大的是{max(age_list)}")
    print(f"age_list最小的是{min(age_list)}")
    print(f"age_list總和是{sum(age_list)}")
    print(f"age_list平均是{sum(age_list)/len(age_list)}")

    new_age=[age+1 for age in age_list]
    print(new_age)

    ages_18up = [age for age in age_list if age>=18]
    print(ages_18up)

    listnew=[]
    for age in age_list:
        if age>18:
            listnew.append(age)
    print(listnew)

    # 這是「切片（slice）」語法：ages[start:stop:step][::-1] 的意思：
    # start 和 stop 都省略，代表「從頭到尾」
    #
    # step = -1，代表「每次往回倒著走一格」
    age_re=age_list[::-1]
    print(age_re)

    user_list = [
        {"name": "Amy", "age": 20},
        {"name": "Bob", "age": 17},
        {"name": "Coco", "age": 25}
    ]

    for a in user_list:
        print(a['name'],a['age'])

    # 用於 list of dict 找KEY值
    if user_list:
        print(user_list[0].keys())

if __name__ == "__main__":
    main()
