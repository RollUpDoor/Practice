def main():
    """
    Day10 - 專精練習List
    會建立 list、會新增 / 刪除元素、會用 index 取值 & 修改、會用切片、會排序、反轉、會處理巢狀 list、會用迴圈處理 list
    """
    # 1. 建立一個包含三個水果的 list，並印出整個 list
    fruit=['apple', 'banana', 'cherry']
    print(f'1.{fruit}')
    # 2. 印出 list 的第一個水果
    print(f'2.{fruit[0]}')
    # 3. 把 list 裡第二個水果改成 'mango'，並印出結果
    fruit[1]='mango'
    print(f'3.{fruit}')
    # 4. 用 .append() 在最後加上 'grape'
    fruit.append('grape')
    print(f'4.{fruit}')
    # 5. 用 .insert() 把 'watermelon' 加到第2個位置
    fruit.insert(1,'watermelon')
    print(f'5.{fruit}')
    # 6. 用 .remove() 刪除 'banana'（或 .pop() 刪除第3個元素）
    fruit2 = ['apple', 'banana', 'cherry']
    fruit2.remove('banana')
    print(f'6-1.{fruit2}')
    fruit3 = ['apple', 'banana', 'cherry']
    fruit3.pop(2)
    print(f'6-2.{fruit3}')
    # 7. 建立一個數字 list，印出排序後的結果（.sort()）
    fruit.sort()
    print(f'7.{fruit}')
    # 8. 印出反轉排序後的結果
    print(f'8-1.{fruit[::-1]}')
    fruit.sort(reverse=True)
    print(f'8-2.{fruit}')
    # 9. 用切片印出前 3 個元素
    print(f'9.{fruit[:3]}')
    # 10. 建立一個巢狀 list，例如：[['Amy', 20], ['Bob', 25], ['Coco', 30]]
    name=[['Amy', 20], ['Bob', 25], ['Coco', 30]]
    print(f'10-1.{name}')
    print(f'10-2: {name[1][0]} 年齡{name[1][1]}')

    # 11. 用 for 迴圈印出巢狀 list 的所有人名
    for i in range(len(name)):
        print(f'11-{i}.{name[i][0]}')
    # 12. 把所有人的年齡加 1，再印出新的巢狀 list
    for i in range(len(name)):
        name[i][1]= name[i][1]+1
    print(f'12.{name}')

    """
    老師建議
    """
    print('老師建議11')
    """
    enumerate(name)會把清單「同時」變成 (索引, 元素) 的序列。
    (person, age) 是解包（unpacking）：因為 name 裡每個元素都是像 ['Amy', 20] 這樣長度 2 的小清單，所以可以直接一次拆成兩個變數。
    小優化：若想讓編號從 1 開始，比較貼近人類習慣：
    for i, (person, age) in enumerate(name, start=1):
    print(f'11-{i}.{person}')
    """
    for i, (person, age) in enumerate(name):
        print(f'11-{i}.{person}')

    print('老師建議12')
    """
    這裡的 p 不是複製品，而是指向同一個內層清單的參照（alias）
    所以改 p[1] 等於直接改動 name 裡的那個內層清單
    p[1] += 1：把內層清單的第 2 個元素（年齡）加 1。三圈後，資料會變成：
    """
    for p in name:
        p[1] += 1
    print(f'12.{name}')
    """
    為什麼要用 enumerate？
    少打一個 range(len(...))，更直覺，也不容易寫錯索引。
    
    為什麼能直接改 p[1]？
    因為內層是「list（可變）」。如果是 tuple（不可變），就會 TypeError。
    
    不想改原資料，想產生新清單？
    用列表生成式建立新結構：
    new_people = [[person, age + 1] for person, age in people]
    
    年齡如果是字串（例如 '20'），要先轉型：
    p[1] = int(p[1]) + 1
    
    不用解包也行，但比較不漂亮：

    for i, row in enumerate(people):
        print(f'11-{i}.{row[0]}')
    用索引改年齡（結果一樣）：
    for i in range(len(people)):
        people[i][1] += 1
    """






if __name__ == "__main__":
    main()
