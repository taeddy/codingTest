from collections import Counter
from datetime import datetime
import os
import re

DIRECTORY_LIST = ['solved_ac', 'programmers', 'codeforces']


def count_problem_source_code():
    total_code_num = 0
    code_cnt_info = {}

    for directory in DIRECTORY_LIST:
        code_list = os.listdir(f"./{directory}")
        total_code_num += len(code_list)
        code_cnt_info[directory] = len(code_list)

    return total_code_num, code_cnt_info


def make_count_info(total_code_num: int, code_cnt_info: dict):
    count_info = f"#### 현재까지 풀어본 총 문제 수 : {total_code_num}개\n"

    for name, cnt in code_cnt_info.items():
        temp = f"- {name} - {cnt}개\n"
        count_info += temp

    return count_info


def make_read_me(count_info):
    return f"""## 코딩 알고리즘 문제 풀이 모음
|플랫폼|등급|
|----|----|
|Baekjoon(Solved.ac)|<img src="https://static.solved.ac/class/c4s.svg" width="45px">|
    
{count_info}

#### 아래의 페이지에서 제공하는 문제들로 구성되어 있습니다.
- [BaekJoon(Solved.ac)](https://solved.ac/en/profile/stz3148)
- [Programmers](https://programmers.co.kr/)
- [Codeforces](https://codeforces.com/profile/Taeddy)
- [Atcoder](https://atcoder.jp/)
<!--
[Samsung_SW_Academy](https://swexpertacademy.com/main/main.do)
[LeetCode](https://leetcode.com/)
[HackerRank](https://www.hackerrank.com/)
[Jungol](http://www.jungol.co.kr/)
[Codeup](https://codeup.kr/)
-->"""


def update_readme_md():
    total_code_num, code_cnt_info = count_problem_source_code()

    count_info = make_count_info(total_code_num=total_code_num, code_cnt_info=code_cnt_info)

    readme = make_read_me(count_info=count_info)

    return readme


if __name__ == "__main__":
    readme = update_readme_md()
    with open("./README.md", 'w', encoding='utf-8') as f:
        f.write(readme)
