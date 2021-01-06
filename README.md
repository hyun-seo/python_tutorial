# python_tutorial

## 1. package & module
Module is a single python file(*.py)
Package is composed of multiple modules and directory hierachy(namespace).

모듈은 파이썬 파일 1개를 의미.  
패키지는 여러개의 모듈 또는 디렉토리(namespace)로 구성됨.  
패키지는 __path__ attribute를 가짐.  

패키지 내부에서는 상대적인 import를 하고, 실행하는 파일은 패키지 외부에 두는 것이 정답.  
경로를 가지고 sys에 등록해서 import하는 것은 code intelligence가 안되기 때문에 좋지 않은 방법.  


## 2. Object methods & attributes

`__dict__`  
`__dir__()`  
`__doc__`  
`__getattribute__('att1')`  
`__module__`  
`__setattr__('att2',1)`  
`__str__()`  