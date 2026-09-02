"""
[머지 정렬 구현]

문제 설명:
- 머지 정렬(Merge Sort) 알고리즘을 구현합니다.
- 분할 정복(Divide and Conquer) 방식을 사용합니다.
- 배열을 절반으로 나누고, 각각을 정렬한 후 병합합니다.

입력:
- arr: 정렬되지 않은 정수 배열

출력:
- 오름차순으로 정렬된 배열

예제:
입력: [38, 27, 43, 3, 9, 82, 10]
출력: [3, 9, 10, 27, 38, 43, 82]

힌트:
- 배열을 절반으로 분할 (재귀)
- 각 부분을 재귀적으로 정렬
- 정렬된 두 부분을 병합
"""

# 방식 1: 새 리스트를 만들어서 넘김
def merge(left_arr, right_arr):
    merged = []
    left_i, right_i = 0, 0
    while  left_i<len(left_arr) and right_i<len(right_arr):
        if left_arr[left_i] < right_arr[right_i]: #맨 처음 요소부터 비교해서 둘 중 작은거 리스트에 추가  
            merged.append(left_arr[left_i])
            left_i += 1
        else: 
            merged.append(right_arr[right_i])
            right_i += 1
    # 파이썬은 슬라이싱할때 인덱스 범위를 넘어가도 에러가 안 나고 빈칸 반환 
    return merged + left_arr[left_i:] + right_arr[right_i:] 

def merge_sort(arr):
    if(len(arr)<=1):
        return arr
    mid = len(arr)//2
    # 분할은 단순히 절반으로 나누기가 끝 -> 돌아오는 병합 단계에서 비교 수행 (정렬)
    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    arr1 = [38, 27, 43, 3, 9, 82, 10]
    print("=== 테스트 케이스 1 ===")
    print(f"정렬 전: {arr1}")
    result1 = merge_sort(arr1.copy())
    print(f"정렬 후: {result1}")
    print()
    
    # 테스트 케이스 2
    arr2 = [12, 11, 13, 5, 6, 7]
    print("=== 테스트 케이스 2 ===")
    print(f"정렬 전: {arr2}")
    result2 = merge_sort(arr2.copy())
    print(f"정렬 후: {result2}")
    print()
    
    # 테스트 케이스 3: 역순
    arr3 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print("=== 테스트 케이스 3: 역순 ===")
    print(f"정렬 전: {arr3}")
    result3 = merge_sort(arr3.copy())
    print(f"정렬 후: {result3}")
    print()
    
    # 테스트 케이스 4: 중복 원소
    arr4 = [5, 2, 8, 2, 9, 1, 5, 5]
    print("=== 테스트 케이스 4: 중복 원소 ===")
    print(f"정렬 전: {arr4}")                                                                      
    result4 = merge_sort(arr4.copy())
    print(f"정렬 후: {result4}")


