routes = [[-20,15], [-14,-5], [-18,-13], [-5,-3]]

def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1]) # routes를 차량이 나간 지점 (진출) 기준으로 정렬
    camera = -30001 # -30001부터 카메라 위치를 찾음

    for route in routes:
        if camera < route[0]: # 현재 카메라 위치로 해당 차량을 만나지 못했다는 의미
            answer += 1
            camera = route[1] # 가장 최근 카메라의 위치 갱신
    return answer

print(solution(routes))