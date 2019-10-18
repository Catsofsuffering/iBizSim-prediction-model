# iBizSim软件预测模拟程序

## iBizSim 软件介绍

iBizSim是由来自北京大学光华管理学院的教授带领专业团队开发的一款企业竞争模拟软件。学员组成虚拟公司的高层管理团队，在模拟的市场环境里展开竞争，进行多期经营决策的演练，通过竞赛对抗的手段，锻炼学员正确制定企业的经营决策，并培养其宏观企业管理的能力。主要用于大学MBA教学、大学生创业教育、企业管理层培训等。

网址：http://www.ibizsim.cn/

## iBizsim prediction软件介绍

- **作者：**
Peony Guo
- **开发目的：**
方便参加企业模拟大赛同学更加智能方便进行比赛的辅助软件。

## 预测模拟实现功能清单

- **客户端**
- [x] 通过用户名和密码实现代理登录功能
    - [ ] 查找队名对应的teamid
    - [ ] 查找比赛对应的gameid
- [ ] 初始比赛参数一键导出
    - [ ] 从网页上爬取对应的数据
    - [ ] 将爬取的数据写入到本地表格中
- [ ] 一键更新往期数据
    - [ ] 检测当前数据更新状况
    - [ ] 检测往期是否有错误
    - [ ] 爬取对应的数据
    - [ ] 将爬取的数据写入本地表格
- [x] 一键提交决策（用规范模板）
    - [x] 从本地表格读取数据
    - [x] 将读取的数据提交
    - [ ] 自动更新往期数据
- [ ] 添加GUI界面
    - [ ] 实现本地登录框
    - [ ] 获取手动输入的比赛ID
    - [ ] 实现选取本地表格提交
    - [ ] 实现选取提交决策的期数
    - [ ] 实现更新按钮，一键更新数据
    - [ ] 实现生成决策按钮，一键生成当期决策
    - [ ] 实现选择是否自动生成决策
    - [ ] 设置定期提交决策的时间

- **服务器端**
- [ ] 自动预测每期决策，与每期模拟结束后5分钟自动提交下一期预测结果（无需手动提交）
- [ ] 自动预测每期决策，一键在模板生成预测数据方便修改


## 开发计划

1. 实现爬虫功能，分辨实现参数导出，数据更新，**提交决策（2019/10/19）**功能。

2. 爬取现在已有的比赛数据（173654场），保存到数据库。

3. 建立预测模型，通过已有的比赛数据进行机器学习训练。

4. 实现自动预测决策功能。

5. 实现客户端GUI。

6. 将程序逻辑分为客户端和服务器端。
