import random

whole_list = ['최 아무개', '송 아무개', '박 아무개', '류 아무개', '이 아무개',
              '김 아무개', '김유신']

whole_member = len(whole_list)
teams = int(input('몇 개의 팀으로 나누시겠습니까?.'))
team_member = int(whole_member/teams)

print(f'전체 인원 : {whole_member}명')
print(f'팀당 인원 : {int(whole_member/teams)}명')

for i in range(teams):
    team = []
    while len(team) < int(whole_member/teams):
        student = random.choice(whole_list)
        if student not in team:
            team.append(student)
            whole_list.remove(student)

    print(f'{i+1}조 :', team)

if len(whole_list) != 0:
    print(f'남은인원 : {whole_list}')