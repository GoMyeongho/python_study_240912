# 상근이 알람 : 45분 일찍 알람을 울리 도록 하는 문제
# 입력 : 시간과 분을 입력 받음, 24시간제
# 22:40 => 21:55
# 0:30  => 23:45

# 입력은 H, M으로 ':'기준으로 입력받음

# 시간을 분으로 환산하기
# 분으로 환산한 시간이 45보다 작으면 시간을 별도 계산
# 45분을 빼줌
# 다시 시간고 분으로 환산해 출력

H , M = map(int,input("알람을 맞출 시간을 입력하시오 : ").split(":"))
# 1번 풀이

'''

time = H * 60 + M - 45
if time < 0:
    time += 1440
h = time // 60
m = time % 60
print(f"알람 시간은 {h}:{m}입니다.")

#'''

# 2번 풀이

#'''

m = M - 45
h = H + m // 60
print(f"알람 시간은 {h % 24}:{m % 60} 입니다.")

#'''






























