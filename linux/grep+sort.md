# grep
> 검색

ex). `cat sample | grep Apple`

Option	Function
- -v	Shows all the lines that do not match the searched string
- -c	Displays only the count of matching lines
- -n	Shows the matching line and its number
- -i	Match both (upper and lower) case
- -l	Shows just the name of the file with the string

# sort
- -r : Reverses  sorting
- -n : Sorts numerically
- -f : Case insensitive sorting 

ex). cat sample | grep -v a | sort -r

: sample 아라는 파일에서 a 안들어가는 애들을 반대로 정렬해라