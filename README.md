# What's CCPR?
  
  CCPR is the abbreviation of Chinese Calligraphy and Painting Recognition.
  
  This project's purpose is to try using the way of comparison to recognize the famous Chinese calligraphies and Paintings. The algorithm is based on the judicial expertise principles.

# Version

- This CWPR 0.0.1 only includes the method of decerning regular script, with 18 famous ancient Chinese calligraphers' characteristic values.  

- The ongoing version will be extended to more calligraphers, running script and cursive script , and paintings.

- Updated to intelligent pretreatment.

# System

- Windows 10

# Python Version

- Python 3.6

# Necessary libs

- numpy 1.19.5
- PIL
- csv
- pandas 1.1.5

# How to use

- Preparation
 -Choose a to-be-tested regular script image, turn it into black-and_white model with photoshop. If the charactors are in black, use reverse to make the handwritings into white, and the background into black.
 -Take out the following strokes with the pen tool of photoshop, rub the background as clean as possible.
  - Five vertical("shu") images
  - Five right-falling stroke("na") images
  - Five horizontal-turning("hengzhe") images
  - The widest vertical and the slimmest vertical images
 -Replace those images of the following dir: /check/pre_settlement with correct file_names("kuan_1" for the widest vertical and "kuan_2" for the  slimmest vertical)

- If you want to compare the  to-be-tested handwriting with one of the 18  calligraphers, use the function "Check_if_somebody("")" in IR_check.py, and enter the abbreviation of the  calligrapher' name.

- If you don't know who to compare with, use the function " Check_similarity()" function in IR_check.py, it may provide three of the neareast and the similiarity with this calligrapher's style.

# The 18 in the database:
  
  - A complete list of the abbreviation of their names:
    - "zy" for "Zhong You"("钟繇")
    - "wxz" for "Wang Xizhi"("王羲之")
    - "xianzhi" for "Wang Xianzhi"("王献之")
    - "csl" for "Chu Suiliang"("褚遂良")
    - "ysn" for "Yu Shinan"("虞世南")
    - "oyx" for "Ouyang Xun"("欧阳询")
    - "yzq" for "Yan Zhenqing"("颜真卿")
    - "lgq" for "Liu Gongquan"("柳公权")
    - "ss" for "Su Shi"("苏轼")
    - "mf" for "Mi Fu"("米芾")
    - "cx" for "Cai Xiang"("蔡襄")
    - "zj" for "Zhao Ji"("赵佶")
    - "zmf" for "Zhao Mengfu"("赵孟頫")
    - "nz" for "Ni Zan"("倪瓒")
    - "dqc" for "Dong Qichang"("董其昌")
    - "wzm" for "Wen Zhengming"("文征明")
    - "dsr" for "Deng Shiru"("邓石如")
    - "qg" for "Qi Gong"("启功")


# License and Use

Greenleaf © 2021 



    

  


