from 银行系统实战.admin import Admin
import time

def main():
  #存储所有用户的操作
  allUsers = {}

  #界面对象
  view = Admin()
  #管理员登陆
  view.printFunctionView()
  if view.adminLogin():
      return -1
  while True:
      #等待用户的操作
      option = input("请输入您的操作：")
      if option == "1":
              # 开户
              pass
      elif option == "2":
              # 查询
              pass
      elif option == "3":
              # 取款
              pass
      elif option == "4":
              # 存储
              pass
      elif option == "5":
              # 转账
              pass
      elif option == "6":
              # 改密
              pass
      elif option == "7":
              # 锁定
              pass
      elif option == "8":
              # 解锁
              pass
      elif option == "9":
              # 补卡
              pass
      elif option == "0":
              # 销户
              pass
      elif option == "t":
              # 推出
           if not view.adminLogin():
               return -1
      time.sleep(3)

if __name__ =="__main__":
    main()
