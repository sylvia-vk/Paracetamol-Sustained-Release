import numpy as np
import matplotlib.pyplot as plt

# ================= 释放仿真模型 =================
def simulate_release():
    # 设定时间轴 (0 到 12 小时)
    t = np.linspace(0, 12, 100)
    
    # Korsmeyer-Peppas 模型参数 (反推设定，以匹配目标)
    # 目标: 1h≈25%, 4h≈55%, 8h≥80%
    k = 25.0
    n = 0.57
    
    # 计算累积释放度 (%)
    # 注意: 实际模型不应该超过 100%，所以在后面做截断处理
    release = k * (t ** n)
    release = np.clip(release, 0, 100) 
    
    # ================= 绘图 =================
    plt.figure(figsize=(8, 5))
    
    # 画理论仿真曲线
    plt.plot(t, release, label='Theoretical Simulation (K-P Model)', color='purple', linewidth=2)
    
    # 标记你的设计目标点
    target_t = [1, 4, 8]
    target_m = [25, 55, 80]
    plt.scatter(target_t, target_m, color='red', s=100, zorder=5, label='Design Targets')
    
    # 在每个目标点旁边写上具体数值
    for i, txt in enumerate(target_m):
        plt.annotate(f'{txt}%', (target_t[i], target_m[i]), xytext=(5, 10), 
                     textcoords='offset points', color='red', fontsize=10)

    # 美化图表
    plt.axhline(80, color='gray', linestyle='--', alpha=0.5) # 80% 达标线
    plt.title('Theoretical Release Profile of Paracetamol Sustained-Release Tablets')
    plt.xlabel('Time (h)')
    plt.ylabel('Cumulative Release (%)')
    plt.ylim(0, 110)
    plt.xlim(0, 12)
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

# ================= 主程序入口 =================
if __name__ == "__main__":
    print("正在生成理论释放曲线...")
    simulate_release()
