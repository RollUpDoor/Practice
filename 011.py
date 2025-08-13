def main():
    # Day11 - 專精練習 Dict


    # 基礎篇

    # 1.建立一個簡單的 dict，包含姓名、年齡、城市，並印出整個 dict
    contact_dict={'name':'Vivien','age':20,'city':'Taipei'}
    print(f'1.{contact_dict}')
    # 2. 用 key 取出姓名並印出
    print(f"2.{contact_dict['name']}")
    # 3. 修改年齡的值，再印出結果
    contact_dict['age']=300
    print(f'3.{contact_dict}')
    # 4. 用 update() 一次更新多個欄位（例如城市與電話）
    contact_dict.update({'name':'Cindy','city':'OK','age':10})
    print(f'4.{contact_dict}')
    # 5. 用 pop() 刪除一個欄位（例如城市），並提供預設值避免 KeyError
    removed_city = contact_dict.pop('city', None)
    print(f'5.{contact_dict}（刪除的 city={removed_city}）')

    # 6. 用 in 判斷某個 key 是否存在（例：'phone' in dict）
    if 'phone' in contact_dict:
        print('Yes')
    else:
        print('No')

    # 6. 用 in 判斷某個 key 是否存在（例：'phone' in dict）
    print('6.Yes' if 'phone' in contact_dict else '6.No')

    print('----------進階篇------------')
    #  7.巢狀 list → 字典清單
    people = [['Amy', 21], ['Bob', 26], ['Coco', 31]]
    dict_list = [{'name': n, 'age': a} for n, a in people]
    print(dict_list)

    #  8.從 dict 清單中篩出年齡 ≥ 25 的人（列表生成式 + 條件）
    namename=[]
    for n,a in people:
        if a >= 25:
            namename.append(n)
    print(namename)

    age_25_plus = [d['name'] for d in dict_list if d['age'] >= 25]
    print(f'8.{age_25_plus}')

    # 9. 把所有名字轉成大寫（列表生成式 + .upper()）
    upper_names = [d['name'].upper() for d in dict_list]
    print(f'9.{upper_names}')

    name2=[]
    for n,a in people:
        name2.append(n.upper())
    print(name2)

    for n,a in people:
        print(f'{n}:{a}')

    for i, d in enumerate(dict_list, start=1):
        print(f'10-{i}.{d["name"]}:{d["age"]}')

    # 11. 建立巢狀 dict，取出 math 分數並印出
    student = {'name': 'Amy','scores': {'math': 90, 'english': 85}}
    print(student['scores']['math'])

    # 12. 把 english 分數 +5 並印出整個 student
    student['scores']['english']+=5
    print(student)

    # 13. 用 dict.items() 迭代輸出 key 和 value（解包更清楚）
    for k, v in student.items():
        print(f'13.{k} -> {v}')



if __name__ == "__main__":
    main()
