"""
Day3程式內容-20250802
練習：計算名單裡面年齡的平均、和四分位數
"""

# 自製計算中位數的方法 (回傳一個值」——這個值可以是任何型別（int、float、str、list、dict…）)
def median(lst):
    n = len(lst) # 我去計算 LIST 的長度
    if n == 0:
        return None # 如果是空list，就回傳None（防呆）
    mid = n // 2  # 中位數就是長度/2
    if n % 2 == 1:
        return lst[mid] # 如果元素個數是奇數，中位數就是正中間那個
    else:
        return (lst[mid - 1] + lst[mid]) / 2  # 偶數個：取中間兩個的平均

def main():
    #  Part1輸入姓名、年齡，然後顯示自我介紹句子。
    user_list=[]
    while True:
        name=input("請輸入你的名字，若要離開請輸入-10:")
        if name=="-10":
            break

        age=input("請輸入你的年齡，若要離開請輸入-10:")
        if age == "-10":
            break
        #  加入判斷，名字不能有空白，數字，只可以有中文和英文
        if name.isalpha() and age.isdigit():
            user_list.append({"name":name,"age":int(age)})
        else:
            print("名字只可有英文或中文，不可有特殊符號和數字!")
    print("\n【已輸入的名單】")
    for number, user in enumerate(user_list,1):
        print(f"{number}.{user['name']}({user['age']}歲)")



    # 年齡統計
    if user_list:  #  如果user_list這個名單有資料（不是空的）

        #  產生一個新list，裡面是所有名單的年齡欄位（user['age']），並且排序
        ages = sorted([user['age'] for user in user_list])
        n = len(ages) # 計算名單裡有幾個年齡（也就是總人數）
        avg = round(sum(ages)/n,1)

        #Q2
        q2 = median(ages)

        # Q1 (lower half，不包含Q2)
        if n % 2 == 0:
            lower_half = ages[:n // 2]
            upper_half = ages[n // 2:]
        else:
            lower_half = ages[:n // 2]
            upper_half = ages[n // 2 + 1:]
        q1 = median(lower_half)
        q3 = median(upper_half)

        """
        Example:
        舉例: 算四分位數的標準切法
            例1：偶數個（6個）
            ages = [10, 15, 18, 22, 27, 30]
            
            lower_half = [10, 15, 18]
            
            upper_half = [22, 27, 30]
            
            例2：奇數個（7個）
            ages = [10, 15, 18, 22, 27, 30, 35]
            
            n//2 = 3
            
            lower_half = [10, 15, 18]
            
            upper_half = [27, 30, 35] # 跳過正中間那個（22）
            
            然後
            q1 = median(lower_half) ：Q1 就是前半部的中位數
            
            q3 = median(upper_half) ：Q3 就是後半部的中位數
        """

        print(f"\n平均年齡：{avg} 歲")
        print(f"Q1（第一四分位數）：{q1} 歲")
        print(f"Q2（中位數）：{q2} 歲")
        print(f"Q3（第三四分位數）：{q3} 歲")
    else:
        print("（沒有任何有效資料）")

    print("已離開名單工具，再見!")



if __name__ == "__main__":
    main()
