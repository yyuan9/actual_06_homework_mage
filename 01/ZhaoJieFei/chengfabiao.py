#encoding: utf-8

ss=input('请输入打印的行数：')
ss=int(ss)
print("-------")
hang=1
while hang <= ss :
    lie=1
    while lie < hang :
        print(lie,"*", hang,"=", lie*hang,end=" ")
        lie=lie +1
    print(lie,"*", hang,"=", lie*hang)
    hang=hang +1
print("-------\nThe END")
