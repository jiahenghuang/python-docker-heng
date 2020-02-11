#codinhg:utf-8
#为了让代码pythonic，经常会用到装饰器这个东西。装饰器也是为了简约代码。当函数被调用的时候才执行，日志用这个东西较多
#所谓装饰器就是输入一个函数再返回一个函数，这个函数已经不再是原来的函数，而是一个新的函数，新的函数在原来函数基础上加了一些东西。
#理解装饰器就是要通过python变量作用域理解为什么这个函数不再是旧的函数而是新的函数
#为了实现这个功能，需要了解函数调用的过程是怎样的。

def func_print(func):
    def wrapper(*args,**kwargs):
        print(func.__name__)
        return func(*args,**kwargs)
    return wrapper

sum=func_print(sum)


def my_sum(*arg):
    print('in my_sum,arg=',arg)
    return sum(arg)

def dec(func):
    def in_dec(*arg):
        print('in in_dec,arg=', arg)
        if len(arg) == 0:
            return 0
        for val in arg:
            if not isinstance(val, int):
                return 0
        return func(*arg)

    return in_dec


my_sums = dec(my_sum)  # 命名为my_sums，是为了和my_sum进行区分，便于理解
# ①调用dec()函数，将dec的返回值赋值给my_sums，相当于my_sums=in_dec，②将函数my_sum赋值给func，相当于func=my_sum
result = my_sums(1, 2, 3, 4, 5)  
# ③相当于将(1, 2, 3, 4, 5)赋值给in_dec函数中的arg，调用并执行函数in_dec()，
# ④in_dec()函数的return返回值是func()函数，将in_dec函数中的arg赋值给func()函数中的arg,也就是赋值给my_sum()中的arg
# ⑤调用并执行函数my_sum()，将sum(arg)结果返回给变量result
print(result)

in in_dec,arg= (1, 2, 3, 4, 5)
in my_sum,arg= (1, 2, 3, 4, 5)

#整个过程可以简单的理解为，先运行dec()函数，其返回值是in_dec函数，再运行in_dec函数，其返回值为func函数，也就是my_sum函数，再运行my_sum函数
#dec() -> in_dec() -> my_sum()





