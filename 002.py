"""
Day2程式內容-20250801
練習：反覆輸入名字和年齡，直到輸入-10結束，最後印出所有名單。
"""

def main():
    # create a list to store the name and age。
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
            user_list.append({"name":name,"age":age}) # 存入資料
        else:
            print("名字只可有英文或中文，不可有特殊符號和數字!")
    print("\n【已輸入的名單】")
    for number, user in enumerate(user_list,1):
        print(f"{number}.{user['name']}({user['age']}歲)")

    print("已離開名單工具，再見!")



if __name__ == "__main__":
    main()
