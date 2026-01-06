#Union类型注解
from typing import Union
mylist:list[Union[int,str]] = [1,2,"gem"]

def func(data:Union[int,str]) -> Union[int,str]:
    pass

func()