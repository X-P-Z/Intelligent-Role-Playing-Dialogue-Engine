import json

user = {
    "name": "张三",
    "age": 18,
    "gender": "男",
    "city": "北京",
    "hobby": ["readding", "听音乐", "打游戏"]
}
#写入json文件
with open("./resources/user.json","w",encoding="utf-8") as f:
    #ensure_ascii=False,是保证让他中文不被转义，让他显示中文，默认是转义的，是False，所以这里写的是True
    #indent=2,是保证让他格式化
    json.dump(user,f,ensure_ascii=False,indent=2)

#把json输出
with open("./resources/user.json","r",encoding="utf-8") as f:
    user = json.load(f)
    print(user)
    print(type(user))
