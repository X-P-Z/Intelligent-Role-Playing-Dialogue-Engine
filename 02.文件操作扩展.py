
#路径写法：
    #相对路径：
        # . ：当前目录-----------》./可以省略
        #..：上一级目录-------------》.././././
    #绝对路径：
        #从文件系统的根目录开始找，文件位置的完整路径（\这个是转义字符，\n是换行，\t是制表符）






#读文件
with open("./resources/望庐山瀑布.txt","r",encoding="utf-8") as f:
    content = f.read()
    print(content)
with open("..\\第二章\\邹忌讽齐王纳谏.txt","r",encoding="utf-8") as f:
    content = f.read()
    print(content)


#写文件 w是写，会覆盖掉原来的内容，a是追加，没有这个文件都会创建一个文件
with open("./resources/静夜思.txt","w",encoding="utf-8") as f:
    f.write("静夜思（李白）\n\n")
    f.write("床前明月光\n")
    f.write("疑是地上霜\n")
    f.write("举头望明月\n")
    f.write("低头思故乡\n")
with open("./resources/静夜思.txt","a",encoding="utf-8") as f:
    f.write("静夜思（李白）\n\n")
    f.write("床前明月光\n")
    f.write("疑是地上霜\n")
    f.write("举头望明月\n")
    f.write("低头思故乡\n")

