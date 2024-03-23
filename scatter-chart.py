import matplotlib.pyplot as plt

# 設定自行維 Window 內建的微軟正黑體，支援中文顯示
plt.rc("font", family="Microsoft JhengHei")

# 繪製一組資料點的散佈圖，設定樣式
"""
    一組資料點
        (2, 4), (4, 3), (3, 6)
"""
# plt.scatter([2, 4, 3], [4, 3, 6], c="red", s=100)
# plt.show()

# 繪製兩組資料點的散步圖，加上標籤與圖例
"""
    兩組資料點
        第一組  (2, 4), (4, 3), (3, 6)
        第二組  (1, 2), (3, 5), (4, 4)
"""
# plt.scatter([2, 4, 3], [4, 3, 6], s=100, label = "標籤一")
# plt.scatter([1, 3, 4], [2, 5, 4], s=100, label = "標籤二")
# plt.legend()
# plt.show()

# 載入 CSV 檔案格式的資料，繪製適當的散步圖加標示
import csv
with open("scatter-chart-data.csv", encoding="utf-8") as file:
    reader = csv.reader(file)
    header = next(reader)
    # print(header)
    data = {
        "男": {"x":[], "y":[]},
        "女": {"x":[], "y":[]}
    }
    for row in reader:
        # print(row)
        gendor = row[0]
        data[gendor]["x"].append(int(row[1]))
        data[gendor]["y"].append(int(row[2]))

# print(data)
plt.scatter(data["男"]["x"], data["男"]["y"], label="男生", c="blue", s=50)
plt.scatter(data["女"]["x"], data["女"]["y"], label="女生", c="red", s=50)
plt.legend()
plt.show()

