# Paracetamol Sustained-Release Tablets: Modeling & Simulation
## 📌 项目简介
本项目为药剂学实验设计配套代码，围绕**对乙酰氨基酚缓释片**的处方设计与释放行为，包含包衣工艺 ODE 仿真与释放动力学拟合两部分。
## 📂 内容
- `src/film_coating_ode.py`：薄膜包衣过程 ODE 仿真（干衣层沉积 + 片床水分蒸发），用于分析工艺参数（喷速、固含量、蒸发系数）对包衣过程的影响。
- `src/kp_fitting.py`：释放度数据的 Korsmeyer-Peppas 模型拟合（待实验数据整理完成后加入）。
## 🛠️ 环境依赖
```bash
pip install -r requirements.txt
