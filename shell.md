## for 循环
```
for skill in Ada Coffe Action Java; do
    echo "I am good at ${skill}Script"
done
```
## 删除变量

```
#!/bin/sh
myUrl="http://www.runoob.com"
unset myUrl
echo $myUrl
```
## 多行注释

```
:<<EOF
注释内容...
注释内容...
注释内容...
EOF
```
## 传参数

```
#!/bin/bash

echo "Shell 传递参数实例！";
echo "执行的文件名：$0";
echo "第一个参数为：$1";
echo "第二个参数为：$2";
echo "第三个参数为：$3";
```
## 关系运算符

```
-eq	检测两个数是否相等，相等返回 true。
-ne	检测两个数是否不相等，不相等返回 true。
-gt	检测左边的数是否大于右边的，如果是，则返回 true。	
-lt	检测左边的数是否小于右边的，如果是，则返回 true。
-ge	检测左边的数是否大于等于右边的，如果是，则返回 true。
-le	检测左边的数是否小于等于右边的，如果是，则返回 true。
```

## if then else

```
#!/bin/bash
a=10
b=20

if [ $a -eq $b ]
then
   echo "$a -eq $b : a 等于 b"
else
   echo "$a -eq $b: a 不等于 b"
fi
```

## 逻辑运算符


```
&&	逻辑的 AND
||	逻辑的 OR
#!/bin/bash

a=10
b=20

if [[ $a -lt 100 && $b -gt 100 ]]
then
   echo "返回 true"
else
   echo "返回 false"
fi

if [[ $a -lt 100 || $b -gt 100 ]]
then
   echo "返回 true"
else
   echo "返回 false"
fi
```

## echo

```
显示结果定向至文件
echo "It is a test" > myfile
追加结果定向至文件
echo "It is a test" >> myfile
```
## if elif else

```
if condition1
then
    command1
elif condition2 
then 
    command2
else
    commandN
fi
```
## for 循环

```
for var in item1 item2 ... itemN
do
    command1
    command2
    ...
    commandN
done

for loop in 1 2 3 4 5
do
    echo "The value is: $loop"
done
输出结果：

The value is: 1
The value is: 2
The value is: 3
The value is: 4
The value is: 5
```

## while

```
while condition
do
    command
done

#!/bin/bash
int=1
while(( $int<=5 ))
do
    echo $int
    let "int++"
done
```
## case

```
case 值 in
模式1)
    command1
    command2
    ...
    commandN
    ;;
模式2）
    command1
    command2
    ...
    commandN
    ;;
esac
```

