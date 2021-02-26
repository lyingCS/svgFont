### 环境
fontforge python3

---
### 配置

相关配置均在`myConfig.py`文件中，务必按照注释操作

----

### 文件说明

#### 1. export.py
从字体库中导出字形的.svg文件，存储在*svg*文件夹下.

---
#### 2. transform.py (暂定此名)
包含svg文件处理函数，信息提取函数（也即处理字体的函数文件）

---
#### 3. generate.py
将处理完的svg文件（存放在*svg_out*文件夹下）导入到fontforge中并得到改变后的字体库文件*out.ttf*

---
#### 4. GetFont.py
1，2，3的整合文件，使用ffpython解释器运行此文件即可得到*out.ttf*,并提供加载的信息的控制。

----

#### 5. myConfig.py

配置文件，遵守逻辑与配置分离原则

---

#### 6. myUtils.py

方便编写和维护代码的小工具（经常使用的代码片段）

-----

### 使用方法

将`ffpython`安装目录下的`bin`目录加入`path`

命令行执行 `ffpython GetFont.py`

-----

### 算法思想
见*algm.pdf*

---
### 字体校验
processFun.py文件中提供了getAllsign()函数,返回字体加载的信息


