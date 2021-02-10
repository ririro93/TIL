# echo
- -e : **take escape sequences**
    - ex). `echo -e "abc\n def` 이거 실행하면 중간에 개행


# tee

## tee command
read from standard input and write to standart output and files

ex). `echo 'foo' | tee foo.txt` <br>
    - write to file

ex). `echo 'bar' | tee -a foo.txt` <br>
    - append to file