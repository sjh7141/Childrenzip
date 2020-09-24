import pandas as pd
import json
import random
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

"""
    json 파일로부터 추천 알고리즘에 사용할 컬럼만 추출
"""
def load_from_data(file_path):
    with open(file_path, "r") as json_file:
        data =  json.load(json_file)
        df = pd.DataFrame(data=data)
        df = pd.DataFrame(data=data,index=list(df['id']))
        return df.loc[:,['school_bus','general','infants','disabled','disabled_integration','after_school','after-school_inclusion','extension','holiday','all_day','part_time','office','public','private','family','corporate','cooperation','welfare','has_extension_class','language','culture','sport','science']]




"""
parse_user_data(columns, users)
    parameter:
        users:                        # 추천 유저의 주변에 사는 유저 목록
            pandas.dataframe (
                index: int
                columns: [User Id, Kindergarten Id, Weight]
                data: [User Id, Kindergarten Id, Weight]
            )
        columns:                      # 추천 유저의 주변 어린이집 ID 목록 
            list: Kindergarten Id List
        
    return:
        pandas.dataframe (            # db 유저 가중치 쿼리를 행렬화하여 반환
            index: User Id
            columns: Kindergarten Id
            data: weight
        )
"""
def parse_user_data(users, columns):            
    user_list = set(users['user_id'])    
    df = pd.DataFrame(data=[[0]*len(columns) for i in range(len(user_list))], columns=columns, index=user_list)

    users_sum = users.groupby(["user_id", "kindergarten_id"]).sum()    
    for id in users_sum.index:
        df.loc[id[0],id[1]] += users_sum.loc[id,][0]
    return df
    




"""
get_preference(kindergarten_df, user_df):
    parameter:
        kindergarten_df:
            pandas.dataframe (  # kindergarten_df에는 모든 어린이집 정보가 아닌, 유저의 주소 근처 어린이집 또는 검색 시 입력한 주소 근처 어린이집만 저장
                index: Kindergarten Id
                columns: Recommend Feature
                data: boolean
            )

        user_df:
            pandas.dataframe (  # user_df에는 모든 유저가 아닌 추천해줄 유저의 행만 전달.
                index: User Id
                columns: Kindergarten Id 
                data: Weight
            )
            
    return:
        pandas.dataframe (      # 어린이집 선호도를 바탕으로 각 어린이집 피쳐에 선호도를 계산하여 반환        
            index: User Id
            columns: Kindergarten Feature
            data: Weight
        )        
"""
def get_preference(kindergarten_df, user_df):
    data = [0] * len(kindergarten_df.keys())
    for i,key in enumerate(kindergarten_df):
        for j,value in enumerate(kindergarten_df[key]):            
            data[i] += value * user_df[j]
    return pd.DataFrame(columns=list(kindergarten_df.keys()), data=[data])






"""
recommend(kindergarten,preference,n):
    parameter:
        kindergarten:                   # kindergarten_df에는 모든 어린이집 정보가 아닌, 유저의 주소 근처 어린이집 또는 검색 시 입력한 주소 근처 어린이집만 저장
            pandas.dataframe (
                index: Kindergarten Id
                columns: Recommend Feature
                data: boolean
            )
        preference:                     # 사용자가 선호하는 어린이집 피쳐 정보
            pandas.dataframe (
                index: User Id
                columns: Kindergarten Feature
                data: Weight
            )
        n:Int                           # 반환할 데이터의 최대 개수
        
    return:
        list: Kindergarten Id List      # 유사도가 높은 어린이집의 ID를 유사도 값을 기준으로 n개 반환
"""
def recommend(kindergarten,preference,n):
    data = list(*cosine_similarity(preference,kindergarten))
    df = pd.DataFrame(data=[data], columns=kindergarten.index)
    df = pd.DataFrame([[*sorted(data, reverse=True)]], columns=sorted(kindergarten.index, key=lambda x: df[x][0],reverse=True))
    return df.keys()[:n]





"""
user_based_collaborative_filtering(users, user, n):
    parameter:
        users:                          # 추천 유저의 주변에 사는 유저 목록
            pandas.dataframe (
                index: User Id
                columns: Kindergarten Id
                data: weight
            )
        user:                     # 추천 유저
            pandas.dataframe (
                index: User Id
                columns: Kindergarten Id
                data: weight
            )
        n:Int                           # 반환할 데이터의 최대 개수
        
    return:
        list: Kindergarten Id List      # 추천 유저의 선호도와 유사도가 높은 유저의 선호도 차이가 많이나는 어린이집 n개 반환
"""
def user_based_collaborative_filtering(users, user, n):    
    data = list(*cosine_similarity(user,users))    
    df = pd.DataFrame(data=[data], columns=users.index)
    df[df[df.keys()] > 0.99] = 0.0
    df = pd.DataFrame([[*sorted(data, reverse=True)]], columns=sorted(users.index, key=lambda x: df[x][0],reverse=True))        
    result = []
    for idx in df.keys()[:n]:
        result.append((user - users.loc[idx,]).idxmin(axis=1)[0])
    return result



"""
    Test Code
"""
kindergarten_df = load_from_data('./bigdata/data/data2.json')
users_data = [[1+(j == i) if j == i or j==i+1 else 0 for j in range(len(kindergarten_df))] for i in range(10)]
users_df = pd.DataFrame(users_data, columns=kindergarten_df.index)

kindergarten_df = int(kindergarten_df)
print(kindergarten_df)
preference_df = get_preference(kindergarten_df,users_df.iloc[0,:])
contents_recommend_df = recommend(kindergarten_df,preference_df,10)

# print(contents_recommend_df)
print(user_based_collaborative_filtering(users_df, users_df.iloc[[0],:], 10))
# parse_user_data(['11110','11111','11112'], pd.DataFrame(
#         [
#             {'user_id': 1, 'kindergarten_id': '11110', 'weight':3 }, 
#             {'user_id': 1, 'kindergarten_id': '11110', 'weight':4 },
#             {'user_id': 1, 'kindergarten_id': '11112', 'weight':5 }, 
#             {'user_id': 1, 'kindergarten_id': '11112', 'weight':6 },
#             {'user_id': 2, 'kindergarten_id': '11112', 'weight':7 },
#         ]
#     )
# )