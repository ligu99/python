library = [
    {'bookname': '西游记', 'author': '吴承恩', 'price': 100, 'number': 40},
    {'bookname': '水浒传', 'author': '施耐庵', 'price': 100, 'number': 40},
    {'bookname': '红楼梦', 'author': '曹雪芹', 'price': 100, 'number': 40},
    {'bookname': '天珠变', 'author': '唐三少', 'price': 100, 'number': 40},
    {'bookname': '西游记', 'author': '吴成恩', 'price': 100, 'number': 40}
]

while True:
    oper = input("\n1.借書 \n2.還書 \n3.查詢 \n4.查看所有 \n5.退出 \n請選擇：")
    if oper == "1":
        print("借書")
        bookname = input("書名：")
        for book in library:
            if bookname == book["bookname"]:
                if book['number']>0:
                    book["number"]-=1
                    print("借出1本"+bookname)
                else:
                    print("沒有庫存了")
                break
        else:
            print("沒有這本書")
    elif oper == "2":
        print("還書")
        bookname = input("書名：")
        for book in library:
            if bookname == book["bookname"]:
                book["number"]+=1
                print(bookname+"已還成功")
                break
        else:
            print("要捐書嗎")
    elif oper == "3":
        print("查詢")
        msg = input("書名/作者：")
        for book in library:
            if msg in book.values():
                print(f"{book['bookname']},數量：{book['number']}")
                break
        else:
            print("來到了知識的荒漠")
    elif oper == "4":
        print("查看所有")
        for book in library:
            print(f"{book['bookname']}，作者：{book['author']}，數量：{book['number']}")
    elif oper == "5":
        print("退出")
        break
    else:
        print("請重新選擇")