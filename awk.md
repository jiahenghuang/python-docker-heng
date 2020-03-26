## awk -F

```
$cat /etc/passwd |awk  -F ':'  '{print $1}'  

root
daemon
bin
sys
```

```
如果只是显示/etc/passwd的账户和账户对应的shell,而账户与shell之间以tab键分割

$cat /etc/passwd |awk  -F ':'  '{print $1"\t"$7}'

root    /bin/bash
daemon  /bin/sh
bin     /bin/sh
sys     /bin/sh
```


```
如果只是显示/etc/passwd的账户和账户对应的shell,而账户与shell之间以逗号分割,而且在所有行添加列名name,shell,在最后一行添加"blue,/bin/nosh"。

$cat /etc/passwd |awk  -F ':'  'BEGIN {print "name,shell"}  {print $1","$7} END {print "blue,/bin/nosh"}'

name,shell
root,/bin/bash
daemon,/bin/sh
bin,/bin/sh
sys,/bin/sh
....
blue,/bin/nosh
```

```
搜索/etc/passwd有root关键字的所有行

//里面写正则表达式
$awk -F: '/root/' /etc/passwd
root:x:0:0:root:/root:/bin/bash
```


