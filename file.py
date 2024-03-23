# 儲存檔案
file = open("data.txt", mode="w")  # 開啟
file.write("測試中文\n好棒棒")    # 操作
file.close()  # 關閉

with open("data.txt", mode="w") as file:  # 最佳實務操作，會自動、安全的關閉檔案
    file.write("5\n3")

# 讀取檔案
# 把資料讀取出來，一行一行讀取，並且加總起來
data = 0
with open("data.txt", mode="r") as file:
    for line in file:   # 一行一行讀取
        data += int(line) 
print(data)