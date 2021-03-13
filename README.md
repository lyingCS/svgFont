### 环境
fontforge python3

---
### 配置

相关配置均在`myConfig.py`文件中，务必按照注释操作

----

### module

#### gmssl
提供SM3签名算法

---
### 文件说明

#### 1. export.py
从字体库中导出字形的.svg文件，存储在*svg*文件夹下.

---
#### 2. transform.py
包含svg矢量图片处理函数（核心算法）。

---
#### 3. generate.py
将处理完的svg文件（存放在*svg_out*文件夹下）导入到fontforge中并得到改变后的字体库文件*out.ttf*。

---
#### 4. GetFont.py
1，2，3的整合文件，使用ffpython解释器运行此文件即可得到*out.ttf*,并能从中提取出加入的信息。

----
#### 5. extract.py
包含在生成*out.ttf*后，从中提取出信息的函数。

---

#### 6. verify.py
调用extract.py中的函数从*out.ttf*中提取出信息。

---


#### 7. beautify.py
字体美化处理（平滑处理）。

---

#### 8. myConfig.py

配置文件，遵守逻辑与配置分离原则

---

#### 9. myUtils.py

方便编写和维护代码的小工具（经常使用的代码片段）

-----

### 使用方法

将`ffpython`安装目录下的`bin`目录加入`path`

命令行执行 `ffpython GetFont.py`

-----

### 算法思想
见*algm.pdf*

---


