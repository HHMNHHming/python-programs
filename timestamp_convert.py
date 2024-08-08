from datetime import datetime

while True:
    date_str = input("请输入一个时间（格式：YYYYMMDDHHMMSS，输入'exit'退出）: ")
    
    if date_str.lower() == 'exit':  # 如果用户输入'exit'，则退出循环
        break
    
    try:
        dt = datetime.strptime(date_str, "%Y%m%d%H%M%S")
        timestamp = int(dt.timestamp() * 1000)
        print("输入的时间对应的13位时间戳为:", timestamp)
        
    except ValueError:
        print("输入的时间格式不正确，请重新输入。")
