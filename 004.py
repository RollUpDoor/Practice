def main():
    """
    Day4-2025/08/03 
    因為昨天接觸到LIST 和 DICTONARY不太熟悉，是新的東西，所以今天一步一步學習
    今天學會建立 list
    今天學會建立 dict
    今天學會把 dict 加到 list 裡
    今天學會取出 list 裡的每個 dict 的內容並印出來
    """
    # 會建立 list
    user_list=[]
    print(user_list)

    # 會建立 dict
    user1={'name':'Amy', 'age':20}
    print(user1)

    # 把 dict 加進 list
    user_list.append(user1)
    print(user_list)

    #  再加一個
    user2={'name':'bob','age':30}
    user_list.append(user2)
    print(user_list)

    # 印出資料, 字典（dict）裡，你要用中括號和 key，
    # 例如：user["name"]、user["age"]
    for user in user_list:
        print(user['name'],user['age'])

    # 如果要有序號可以用 enumerate 然後可以指定序號從己開始，如果沒寫就是預設0
    for idx, user in enumerate(user_list,2):
        print(f"{idx}.{user['name']}:{user['age']}")
if __name__ == "__main__":
    main()
