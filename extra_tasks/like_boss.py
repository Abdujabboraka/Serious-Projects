def like(likes: list):

    if not likes:
        print("bu xech kimga yoqmadi")
    elif len(likes) == 1:
        print(f"bu {likes[0]}ga yoqdi")
    elif len(likes) == 2:
        print(f"bu  {likes[0]} va {likes[1]}ga yoqdi")
    elif len(likes) == 3:
        print(f"bu {likes[0]}, {likes[1]} va {likes[0]}ga yoqdi")
    elif len(likes) == 4:
        print(f"bu {likes[0]}, {likes[1]}, {likes[2]} va {likes[3]}ga yoqdi")
    else:
        xabar = f"{likes[0]}, {likes[1]}, {likes[2]}, {likes[3]} va yana {len(likes)-4} ta odamga yoqdi!"
        print(xabar)


users = ['Brown', 'Jones', 'Miller', 'Davis', 'Garcia', 'Rodriguez', 'Wilson', 'Alice', 'Bob', 'Charlie', 'David', 'Emily', 'Frank', 'Grace', 'Henry', 'Isabella', 'Jack']
user = []
like(user)