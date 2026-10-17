# Paracetamol Sustained-Release Tablets: Modeling & Simulation
## 📌 项目简介
本项目为药剂学实验设计配套代码。由于实验课时限制导致体外释放度实验未能获得完整的多点数据，本项目采用**数学建模与 ODE 仿真**的方法，对包衣工艺及药物释放动力学进行理论探究与预测。
## 📂 代码内容
- `src/film_coating_ode.py`：薄膜包衣过程 ODE 仿真（干衣层沉积与水分蒸发动力学）。包含**参数敏感性分析**（对比不同蒸发系数下的水分变化）。
- `src/release_simulation.py`：基于 Korsmeyer-Peppas 方程的药物释放理论仿真。反推参数以验证设计方案目标（1h 释放 25%，4h 释放 55%，8h 释放 ≥80%）。
## 🚀 运行指南
```bash
# 运行包衣敏感性分析
python src/film_coating_ode.py
# 运行理论释放曲线仿真
python src/release_simulation.py
