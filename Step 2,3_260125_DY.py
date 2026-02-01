# Step 2
# 전체 영화 개수, 평균 평점, 최고 평점, 최저 평점 출력

import numpy as np
import csv
import os

print("현재 작업 폴더:", os.getcwd())
file_name = "IMDB top 1000.csv"
with open(file_name, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    
# CSV 파일에서 첫번째 열 제거하는 코드_해당 코드를 사용하니 Excel에서 직접 수정 불필요해짐
    next(reader)

    data_list = [row for row in reader]

#np를 numpy로 사용하면 Error 발생_AI가 
data_array = np.array(data_list)

#rt_idx : Rate index(평점이 있는 열의 위치 번호라는 의미)
#astype은 float로 바꾸라는 코드. 기존 str이라 float로 바꾸어야 계산이 가능.
rt_idx = 5
data_rate = data_array[:, rt_idx].astype(float)

# 전체 영화 개수
data_mov_count = data_array.shape[0]

# 평균, 최고, 최저 평점 계산
# avg는 값이 8.0975로 나와서 Round 사용하여 8.1로 계산되게끔 함.
data_rate_avg = round(data_rate.mean(), 1)
data_rate_max = data_rate.max()
data_rate_min = data_rate.min()

print(f"총 영화 개수: {data_mov_count}")
print(f"평점 평균: {data_rate_avg}")
print(f"최고 평점: {data_rate_max}")
print(f"최저 평점: {data_rate_min}")


# Step 3: 평점이 높은 영화 찾기

data_rate_max = data_rate.max()

# np.where를 통해 "조건을 만족하는 데이터의 위치" 찾기 가능
top_idx = np.where(data_rate == data_rate_max)[0]

print("최고 평점 영화 목록:")

for i in top_idx:
    title = data_array[i, 1]          
    rate = data_array[i, rt_idx]      

    print(f"{title} - 평점: {rate}")