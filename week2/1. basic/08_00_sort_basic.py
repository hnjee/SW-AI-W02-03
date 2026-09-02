# 리스트 중 가장 작은 데이터를 선택해서 앞으로 보내는 과정을 반복  
def selection_sort(arr):
    # i번째 요소에 들어갈 숫자 고르기 
    for i in range(len(arr)):
        # 최소값 구하기
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        # 옮기기
        if min_index != i: 
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# "정렬된 부분"과 "정렬 안 된 부분"을 나눠서, 정렬 안 된 부분의 첫 원소를 정렬된 부분의 알맞은 위치에 끼워 넣습니다.
def insertion_sort_swap(arr):
    # i 이전까지는 정렬된 것이라고 판단함 
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break
    return arr

def insertion_sort_shift(arr):
    # i 이전까지는 정렬된 것이라고 판단함 
    for i in range(1, len(arr)):
        key = arr[i] #i번째는 비었다고 생각 
        j = i
        while j > 0 and key < arr[j-1]:
            arr[j] = arr[j-1] #뒤로 옮기기
            j-=1 #앞으로 이동
        arr[j] = key
    return arr

# 인접한 두 원소를 계속 비교하면서, 순서가 틀리면 바로 옆으로 교환합니다.
def bubble_sort(arr):
    # 한번 정렬되면 가장 큰 수가 맨 뒤로 가게 됨 -> n-1번의 정렬이면 완료
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i): #이미 확정된 오른쪽 부분은 확인할 필요 없음 
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def bubble_sort_early_end(arr):
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                is_sorted = False        
    return arr



if __name__ == "__main__":
    arr = [5, 2, 4, 1, 3]
    #sorted_arr = selection_sort(arr)
    #sorted_arr = insertion_sort(arr)
    sorted_arr = insertion_sort_shift(arr)
    #sorted_arr = bubble_sort(arr)
    #sorted_arr = bubble_sort_early_end(arr)
    #for num in sorted_arr:
        #print(num, end = " ")

    print(arr[::])