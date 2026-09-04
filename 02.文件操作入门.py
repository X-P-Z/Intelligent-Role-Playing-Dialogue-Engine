from pyarrow.lib import utf8

# #打开文件
# f = open("./resources/望庐山瀑布.txt","r",encoding="utf-8")
#
# #操作文件
# # content = f.read()
# # print(content)
#
# content_list = f.readlines()
# for line in content_list:
#     print(line.strip())
#
# #关闭文件
# f.close()


#写文件
# #打开文件
# f = open("./resources/望庐山瀑布.txt","w",encoding="utf-8")
#
# #操作文件
# try:
#     f.write("静夜思(李白)\n")
#     f.write("床前明月光\n")
#     f.write("疑是地上霜\n")
#     f.write("举头望明月\n")
#     f.write("低头思故乡\n")
#
# #关闭文件-----------------------释放资源-------------------------------
# finally:
#     f.close()
#

#项目在释放资源时，推荐的方式，比finally更加的便捷
with open("./resources/望庐山瀑布.txt","w",encoding="utf-8") as f:
        f.write("静夜思(李白)\n")
        f.write("床前明月光\n")
        f.write("疑是地上霜\n")
        f.write("举头望明月\n")
        f.write("低头思故乡\n")

