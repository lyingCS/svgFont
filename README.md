### 环境
fontforge 使用软件带的moudle就行
调用可以用*ffpython*文件下的ffpython运行.py文件


---
### 文件说明

#### 1. export.py
从字体库中导出字形的.svg文件，存储在*svg*文件夹下.

---
#### 2. processFun.py
包含svg文件处理函数，信息提取函数（也即处理字体的函数文件）

---
#### 3. import.py
将处理完的svg文件（存放在*svg_out*文件夹下）导入到fontforge中并得到改变后的字体库文件*out.ttf*

---
#### 4. GetFont.py
1，2，3的整合文件，使用python解释器运行此文件即可得到*out.ttf*,并提供加载的信息的控制。

### 算法思想
见*algm.pdf*

---
### 字体校验
processFun.py文件中提供了getAllsign()函数,返回字体加载的信息


