"""
film_coating_ode.py
薄膜包衣过程 ODE 仿真 —— 对应简历: ODE-based process modeling
运行: python film_coating_ode.py
"""
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def coating_ode(t, y, spray_rate, solid_frac, k_evap):
    """
    简化的包衣锅-片床模型:
      y[0] m_coat  : 沉积干衣层质量 (g)
      y[1] moisture: 片床残留水分 (g)
    假设:
      - 包衣液以恒定喷速加入, 其中 solid_frac 为固含量(沉积), 其余为溶剂(水)
      - 水分蒸发速率与当前含水量成正比 (一阶蒸发), 系数 k_evap 体现进风温度/风量影响
    """
    m_coat, moisture = y
    dm_coat   = spray_rate * solid_frac
    dmoisture = spray_rate * (1 - solid_frac) - k_evap * moisture
    return [dm_coat, dmoisture]

# ============== 参数区: 可按文献/工艺常识自行调整 ==============
spray_rate = 5.0     # 喷液速率 (g/min)
solid_frac = 0.10    # 包衣液固含量 10%
k_evap     = 0.15    # 蒸发系数 (1/min), 进风温度越高越大
t_end      = 60      # 仿真时长 (min)
# ==============================================================

sol = solve_ivp(coating_ode, [0, t_end], [0, 0],
                args=(spray_rate, solid_frac, k_evap),
                dense_output=True, t_eval=np.linspace(0, t_end, 300))

t = sol.t
print(f"{t_end} min 后: 干衣层增重 = {sol.y[0][-1]:.1f} g, 片床水分残留 = {sol.y[1][-1]:.2f} g")
print("提示: 增大 k_evap (更高进风温度) 后对比水分残留变化, 体会 CPP 对过程的影响 —— 面试可讲")

plt.figure(figsize=(5, 4))
plt.plot(t, sol.y[0], label='dry coat mass (g)')
plt.plot(t, sol.y[1], '--', label='bed moisture (g)')
plt.xlabel('Time (min)'); plt.legend(); plt.tight_layout()
plt.savefig('coating_sim.png', dpi=150)
print("图已保存: coating_sim.png")
