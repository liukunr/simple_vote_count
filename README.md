# 功能
这脚本可以统计简单的投票。

# 文件格式
data.txt：
第一行为数字，表示总共N的方面的投票。
后面各行依次为N个方面的投票，用数字表示投票结果。比如用1表示赞成，0表示反对；或者3表示优秀，2表示良好，1表示合格，0表示不合格。
每个人的投票数据占据一行，不用的投票表格中间使用一个空行隔开。

# 示例

第一个人的投票：

|      | 思想   | 表现   |
| ---- | ---- | ---- |
| 小明   | 优秀   | 良好   |
| 小王   | 良好   | 良好   |

第二个人的投票：

|      | 思想   | 表现   |
| ---- | ---- | ---- |
| 小明   | 优秀   | 良好   |
| 小王   | 优秀   | 优秀   |

data.txt:

```
2
32
22

32
33
```

# 使用

```bash
python main.py
```

# 投票统计结果实例

```
统计结果：
   0  1  2  3  4  5
0  0  0  0  1  0  0
1  0  2  1  1  1  0
2  1  0  1  0  1  2
3  1  0  0  0  0  0

统计结果：
   0  1  2  3  4  5
0  0  1  0  0  0  0
1  1  0  1  1  0  0
2  0  1  0  1  1  0
3  1  0  1  0  1  2

统计结果：
   0  1  2  3  4  5
1  2  0  0  2  0  0
2  0  2  1  0  2  1
3  0  0  1  0  0  1
```

从上到下分别是第一个人，第二个人...的统计结果，每行3表示优秀，2表示良好，1表示合格，0表示不合格，每列表示投票的N个方面。

# 开发者

[liukunr](https://github.com/liukunr) [cuixiaozeng](https://github.com/cuixiaozeng)

# 开源许可

MIT。
