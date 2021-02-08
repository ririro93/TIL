# vmmem
[stackexchange](https://superuser.com/questions/1559170/how-can-i-reduce-the-consumption-of-the-vmmem-process)
The memory is being consumed by Linux to cache files. It can be seen in the buff/cache section of free command. To drop the cache, simply run echo 3 | sudo tee /proc/sys/vm/drop_caches