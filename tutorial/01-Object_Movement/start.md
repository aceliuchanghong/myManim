manim中坐标一般是三维的

```
坐标:
np.array([x,y,z])
```

一般整个画面高度为8,宽度由设定的长宽比和高度决定(一般14)

```
画面:
常用单位:
RIGHT,UP,LEFT,DOWN ==> np.array([1,0,0]) np.array([0,1,0])...
UP,UL,DR,DL ==> np.array([1,1,0])...
四边:
TOP,BOTTOM,LEFT_SIDE,RIGHT_SIDE
3D:
OUT,IN ==> np.array([0,0,1])...
```


