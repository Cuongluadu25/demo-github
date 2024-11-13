import pandas as pd
import numpy as np

# Đọc dữ liệu từ tệp Excel
dt = pd.read_excel("d:\TTNT\Book1.xlsx")

# Thiết lập các mảng đầu vào và đầu ra
p = np.array([dt['cao'], dt['rong'], dt['chin']]).T
t = np.array(dt['loai'])

# Sản phẩm cần kiểm tra
test = np.array([[8, 7, 8]])

# Khởi tạo trọng số và hệ số chặn
w = np.array([[5, 5, 5]])
b = -4

k = 0
m = len(p)

# Chuyển nhãn 'A', 'B', 'C' thành giá trị số tương ứng để tính toán
label_mapping = {'A': 1, 'B': -1, 'C': -2}
numeric_targets = np.array([label_mapping[x] for x in t])

# Vòng lặp huấn luyện
while True:
    d = True
    k += 1
    print("Lần lặp thứ:", k)
    
    for i in range(m):
      x = np.array([p[i]])
      n = w.dot(x.T) + b
    
      if n >= 2:
        predicted_value = 1
      elif n >= -1:
        predicted_value = -1
      else:
        predicted_value = -2

        
        if predicted_value != numeric_targets[i]:
            e = numeric_targets[i] - predicted_value
            w = w + np.dot(e, x)
            b = b + e
            d = False
    
    print("w =", w)
    print("b =", b)
    
    # Dừng nếu tất cả các mẫu đều được phân loại đúng
    if d ==True:  # Thêm điều kiện dừng nếu vượt quá 1000 lần lặp
        break

# Phân loại sản phẩm kiểm tra
n = w.dot(test.T) + b
# Phân loại sản phẩm kiểm tra


if n >= 2:
    test = "A"
elif n >= -2:
    test = "B"
else:
    test = "C"

print("Phân loại sản phẩm kiểm tra:", test)


