library = [
    {'bookname': '西游记', 'author': '吴承恩', 'price': 100, 'number': 40},
    {'bookname': '水浒传', 'author': '施耐庵', 'price': 100, 'number': 40},
    {'bookname': '红楼梦', 'author': '曹雪芹', 'price': 100, 'number': 40},
    {'bookname': '天珠变', 'author': '唐三少', 'price': 100, 'number': 40},
    {'bookname': '西游记', 'author': '吴成恩', 'price': 100, 'number': 40}
]

while True:
    oper = input('\n1. 借书 \n2. 还书\n3. 查询\n4. 查看所有\n5. 退出\n请选择你需要的服务：')
    if oper == '1':
        print('1.借书模块')
        # 输入书名 --->
        bookname = input('请输入书名：')
        for book in library:
            if  bookname in book.values():
                if book['number']>0:
                    book['number']-=1
                    print('借书成功！')
                else:
                    print('库存不足')
                break
        else:
            print('没有这本书呢！')
    elif oper == '2':
        print('2.还书模块')
        bookname = input('请输入书名：')
        for book in library:
            if  bookname in book.values():
                book['number']+=1
                print('还书成功！')
                break
        else:
            print('没有这本书呢！')
    elif oper == '3':
        print('3.查询模块(书名/作者)')
        message = input('请输入书名/作者名：')
        for book in library:
            if  message in book.values():
                print('有这本书哦！可以借阅的')
                break
        else:
            print('没有这本书或者用户名')

    elif oper == '4':
        print('4.查看所有模块')
        for book in library:
            print(f"图书名：{book['bookname']}，作者：{book['author']}，价格：{book['price']}，库存剩余{book['number']}")

    elif oper == '5':
        print('5.退出')
        print('系统正常退出')
        break
    else:
        print('请从新选择')
