import math
import time
from mpmath import mp, mpf

# 設置 mpmath 的精度（100 位小數）
mp.dps = 100  # 設置小數位數
print(f"計算精度設置為 {mp.dps} 位小數")

# 輸入係數
a = float(input("請輸入 a 值: "))
b = float(input("請輸入 b 值: "))
c = float(input("請輸入 c 值: "))
d = float(input("請輸入 d 值: "))

# 定義三次方程
def f(x):
    return a*x**3 + b*x**2 + c*x + d

# 定義導函數（牛頓迭代法需要）
def f_prime(x):
    return 3*a*x**2 + 2*b*x + c

# 牛頓迭代法
def newton_method(initial_guess, tolerance=1e-6, max_iterations=1000):
    x = initial_guess
    for i in range(max_iterations):
        fx = f(x)
        fpx = f_prime(x)
        
        if abs(fx) < tolerance:  # 找到根
            return x
        
        if fpx == 0:  # 導數為 0，無法繼續迭代
            break
        
        x = x - fx / fpx  # 牛頓迭代公式
        print(f"第 {i+1} 次迭代: x = {x}, f(x) = {fx}")
    
    return None  # 未找到根

# 找到實數根
initial_guess = 0  # 初始猜測值
root = newton_method(initial_guess)

if root is not None:
    print(f"三次方程的一個實數根為: {root}")
    
    # 多項式除法：將 ax^3 + bx^2 + cx + d 除以 (x - root)
    q2 = a
    q1 = b + q2 * root
    q0 = c + q1 * root
    remainder = d + q0 * root
    
    print(f"商式: {q2}x^2 + {q1}x + {q0}")
    print(f"餘式: {remainder}")
    
    if abs(remainder) < 1e-6:  # 如果餘式接近 0
        print(f"(x - {root}) 是三次方程的一個因式")
    else:
        print(f"(x - {root}) 不是三次方程的因式")
else:
    print("未找到三次方程的實數根")

# 複雜問題：計算高精度圓周率（π）
def calculate_pi(precision):
    print(f"開始計算圓周率（π），精度為 {precision} 位小數...")
    start_time = time.time()
    
    # 使用 mpmath 庫計算 π
    mp.dps = precision  # 設置精度
    pi = mp.pi  # 計算 π
    
    end_time = time.time()
    print(f"計算完成！耗時 {end_time - start_time:.2f} 秒")
    return pi

# 計算高精度圓周率
precision = 100  # 設置精度為 100 位小數
pi_value = calculate_pi(precision)
print(f"計算結果：π = {pi_value}")