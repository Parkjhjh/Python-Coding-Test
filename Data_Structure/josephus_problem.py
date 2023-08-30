# 배열, 링크드 리스트
# 요세푸스 문제
# https://www.acmicpc.net/problem/1158

n, k = map(int, input('n, k 입력').split())     # 공백 기준으로 split
peoples = [i for i in range(1,n+1)]
ans = '<'

idx = 0

for i in range(n):
    idx += (k-1)
    idx %= len(peoples)

    ans = ans + str(peoples.pop(idx)) + ', '

    
ans = ans[:-2]
print(ans+'>')

''' 리스트를 쉼표와 공백을 사이에 넣어서 출력하는 방법 (join 사용법) '''
# ', '.join(map(str, ans))      # '리스트값 사이에 넣을 구분자'.join(리스트)
                                # map(str, ans) : ans 리스트의 원소를 str 타입으로 변환



# 실수
# idx = k - 1
# for i in range(1,n):
#     ans = ans + str(peoples.pop(idx)) + ', '
#     idx += (k-1)
#     idx %= len(peoples)       # len=0 가능함