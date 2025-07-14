import os

DIRECTORY_LIST = ["solved_ac", "programmers", "codeforces"]


def count_problem_source_code():
    code_cnt_info = {}

    for directory in DIRECTORY_LIST:
        total_code_num = {"python": 0, "sql": 0}
        code_list = os.listdir(f"./{directory}")
        for file in code_list:
            if ".py" in file:
                total_code_num["python"] += 1
            elif ".sql" in file:
                total_code_num["sql"] += 1
        code_cnt_info[directory] = total_code_num

    return code_cnt_info


def make_count_info(code_cnt_info: dict):
    langs = ['python', 'sql']
    appearence = {'python': 'Python', 'sql': 'SQL'}
    res = """
"""

    for lang in langs:
        count_info = f"#### ➡️ 현재까지 해결한 {appearence[lang]}문제\n"
        for dir_name, cnt_info in code_cnt_info.items():
            temp = f"- {dir_name}: {cnt_info[lang]}개\n"
            if cnt_info[lang] == 0:
                continue
            count_info += temp
        res += count_info

    return res


def make_read_me(count_info):
    return f"""## 📁 코딩 알고리즘 문제 풀이 모음
<!--
|플랫폼|등급|
|----|----|
|Baekjoon(Solved.ac)|<img src="https://static.solved.ac/class/c4s.svg" width="45px">|
-->
    
{count_info}


---
#### 🗒️ 아래의 페이지에서 제공하는 문제들로 구성되어 있습니다.
- [BaekJoon(Solved.ac)](https://solved.ac/en/profile/stz3148)
- [Programmers](https://programmers.co.kr/)
- [Codeforces](https://codeforces.com/profile/Taeddy)

<!--
[Atcoder](https://atcoder.jp/)
[Samsung_SW_Academy](https://swexpertacademy.com/main/main.do)
[LeetCode](https://leetcode.com/)
[HackerRank](https://www.hackerrank.com/)
[Jungol](http://www.jungol.co.kr/)
[Codeup](https://codeup.kr/)
-->"""


def update_readme_md():
    code_cnt_info = count_problem_source_code()

    count_info = make_count_info(code_cnt_info=code_cnt_info)

    readme = make_read_me(count_info=count_info)

    return readme


if __name__ == "__main__":
    readme = update_readme_md()
    with open("./README.md", "w", encoding="utf-8") as f:
        f.write(readme)
