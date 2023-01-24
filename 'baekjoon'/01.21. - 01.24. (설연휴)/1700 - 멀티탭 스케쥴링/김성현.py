import sys

sys.stdin = open("1700test.txt")
n, k = map(int, input().split())

hole = []  # 멀티탭 만들기
lt = list(map(int, input().split(" ")))  # 리스트 받아오기


def findmin(left_idx):  # ! 멀티탭의 몇번 칸을 뽑아야 하는지 가르쳐주는 함수
    # ? 지금 시점에서 예약된 뽑기 배열 가져오기, 구현시 리스트를 자르지않고 탐색을 뒤 순서부터 하기(최적화)
    fmlst = lt[left_idx:]
    lt_max = 0  # 가장 늦게 꽂아야 하는 전자기기 인덱스 저장할 변수
    cnttt = 0  # 홀 인덱스 반환
    for idx, val in enumerate(hole):  # 멀티탭에 꽂혀있는 전자기기마다 가장 빨리 있는 다음 사용 순서 찾기
        try:  # ! 사용 예약이 없으면 즉시 뽑아도 되기 때문에 없을경우 try - catch 문으로 뽑기
            if lt_max < fmlst.index(val):  # index 는 가장 앞에 있는 인덱스를 반환한다는 성질을 이용
                lt_max = fmlst.index(val)  # 가장 멀리 있는 전자기기를 뽑기 위함
                cnttt = idx  # 멀티탭에 있는 전자기기를 반환하기
        except:  # 만약 멀티탭에 있는 전자기기가 사용 예정이 없다면
            return idx  # 반환 해주기
    return cnttt  # ! 멀티탭의 인덱스 형태로 반환


count = 0  # 멀티탭에서 전자기기를 뽑는 순서
hcnt = 0  # 빈멀티탭에 최초로 전자기기를 꽂기 위해 만든 변수
for idx, val in enumerate(lt):  # 예약 리스트에서 인덱스와 전자기기를 받아와서
    if val in hole:  # 만약 이미 그 전자기기가 멀티탭에 꽂혀있다면 넘어가기
        continue
    if hcnt < n:  # 빈 멀티탭 구멍이 있다면 전자기기 꽂아주기
        hole.append(lt[idx])
        hcnt += 1  # ! 멀티탭에 자리가 차고 있음
    else:
        hole[findmin(idx)] = val  # 멀티탭에서 뽑고 다른 전자기기 꽂기
        count += 1  # 뽑은 개수 카운트
print(count)  # 정답 출력
