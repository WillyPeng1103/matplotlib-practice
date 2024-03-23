import matplotlib.pyplot as plt
import csv

plt.rc("font", family="Microsoft JhengHei")

# """
#     一組資料點
#     (1, 2), (2, 4), (3, 6)
# """
# plt.plot([1, 2, 3], [2, 4, 6])
# plt.show()
"""
    兩組資料點
        第一組 (1, 2), (2, 4), (3, 6)
        第二組 (1, 1), (1, 2), (1, 3)
"""
# plt.plot([1, 2, 3], [[2, 1], [4, 2], [6, 3]], label=["第一組的標籤", "第二組的標籤"])  #設定每一組資料和對應的標籤
# plt.legend()  #產生圖列
# plt.xlabel("x 軸的文字說明")
# plt.ylabel("y 軸的文字說明")
# plt.show()

"""
    標頭 =  ['年度', '小王', '小美']
    每列的資料 ['2010', '40000', '30000']
    每列的資料 ['2011', '42000', '60000']
    每列的資料 ['2012', '45000', '50000']
"""
file  = open("data.csv", encoding= "utf-8")
reader = csv.reader(file)
header = next(reader)    #讀取第一列

print("標頭 = ", header)
x = []  # 預期 [2010, 2011, 2012]
y = []  # 預期 [[40000, 30000], [42000, 60000], [45000, 50000]]
for row in reader:
    print ("每列的資料", row)
    x.append(int(row[0]))
    y.append([int(row[1]), int(row[2])])

file.close()


plt.figure(figsize=(10, 6))
plt.title("薪資表")
plt.plot(x, y)
plt.legend([header[1], header[2]])  #產生圖列
plt.xlabel(header[0])
plt.ylabel("薪水")
plt.show()