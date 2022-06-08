import re

#케이스 수 입력
case = int(input())

# case 수 만큼 반복
for i in range(case):
    score = 0
    quiz = input()
    score_l = re.split(r'[*X]', quiz)
    for _ in score_l:
        score += sum(range(1,len(_)+1))
    print(score)
