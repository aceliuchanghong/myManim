### myManim

Manim学习

### create a test env

```shell
pip freeze > requirements.txt
conda create -n Manim python=3.8
conda activate Manim
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
pip install -r requirements.txt
```

### install

```text
Install FFmpeg.
Install MiKTeX(https://miktex.org/download)
```

### run

```shell
manim main.py
manim main.py -p
```

### referenceq

* [快速入门](https://docs.manim.org.cn/cairo-backend/getting_started/index.html)
