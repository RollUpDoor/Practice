def main():
    """
    Day5-2025/08/05 List+tuple+dict三種Python 資料結構
    """
    """
    1️⃣ List（清單）
    練習題
    建立一個裝有3個人名的 list，印出第三個人名。
    把這個 list 反轉，再印出全部內容。
    新增一個人到 list 結尾，然後印全部。
    """

    name_list=[]
    for i in range(3):
        i=+1 # --> # 這一行其實可以刪掉，沒意義
        name=input("請輸入人名: ")
        name_list.append(name)
    print(name_list[2])
    print(name_list[::-1])
    name_list.append("NewName")
    print(name_list)
    """
    第一題小提醒
    i=+1 這一行可以刪掉，for 迴圈會自動處理 i
    name_list[::-1] 是反轉，原本的 list 不會改變
    name_list.append("NewName") 會在名單最後加上一個 "NewName"
    """

    """
    2️⃣ Tuple（元組）
    練習題
    建立一個存放三個城市名的 tuple，印出所有城市。
    試著改變其中一個城市，觀察 Python 給你的錯誤訊息。
    用 for 迴圈把所有城市名稱印出來。
    """

    cities=("Taipei","NewYork","London")
    print(cities)
    # cities[1]="Taichung" # 'tuple' object does not support item assignment
    for city in cities:
        print(city)

    """
    3️⃣ Dict（字典）
    練習題
    建立一個 dict，存放一個人的名字、年齡、城市。
    印出這個人的所有欄位（key），所有內容（value）。
    新增一個欄位 "hobby"，然後印出整個 dict。
    用 for 迴圈把 key 和 value 全部印出。
    """
    info={"name":"Amy","age":20,"City":"NewYork"}
    print(info.keys())
    info["hobby"]="sing"
    print(info)

    # 這是一個字典（dict）常用的遍歷用法，在 Python 裡，for k, v in info.items(): 讓你一次拿到每個 key 跟 value，然後印出來。
    for k,v in info.items():
        print(k,v)
    for k, v in info.items():
        print(f"{k} : {v}")


if __name__ == "__main__":
    main()
