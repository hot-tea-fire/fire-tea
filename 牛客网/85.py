"""
 有一个特殊的五键键盘
    上面有A、Ctrl-C、Ctrl-X、Ctrl-V、Ctrl-A
    A键在屏幕上输出一个字母A
    Ctrl-C将当前所选的字母复制到剪贴板
    Ctrl-X将当前选择的字母复制到剪贴板并清空所选择的字母
    Ctrl-V将当前剪贴板的字母输出到屏幕
    Ctrl-A选择当前屏幕中所有字母
    注意：
      1. 剪贴板初始为空
      2. 新的内容复制到剪贴板会覆盖原有内容
      3. 当屏幕中没有字母时,Ctrl-A无效
      4. 当没有选择字母时Ctrl-C、Ctrl-X无效
      5. 当有字母被选择时A和Ctrl-V这两个输出功能的键,
         会先清空所选的字母再进行输出

    给定一系列键盘输入,
    输出最终屏幕上字母的数量

    输入描述:
       输入为一行
       为简化解析用数字12345分别代替A、Ctrl-C、Ctrl-X、Ctrl-V、Ctrl-A的输入
       数字用空格分割

    输出描述:
        输出一个数字为屏幕上字母的总数量

    示例一:
        输入:
          1 1 1
        输出:
          3

   示例二:
        输入:
          1 1 5 1 5 2 4 4
        输出:
          2
"""


def solution():
    while True:
        try:
            in_num = list(map(int, input().split()))
        except:
            break
        else:
            screen = 0
            cut = 0
            flag = False
            for item in in_num:
                if item == 1:
                    if flag:
                        screen = 1
                        flag = False
                    else:
                        screen += 1
                        flag = False
                if item == 2:
                    if flag:
                        cut = screen
                if item == 3:
                    if flag:
                        cut = screen
                        screen = 0
                if item == 4:
                    if flag:
                        screen = cut
                        flag = False
                    else:
                        screen += cut
                if item == 5:
                    flag = True
            print(screen)


if __name__ == '__main__':
    solution()
