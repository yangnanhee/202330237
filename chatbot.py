import pandas as pd
import Levenshtein

# CSV 파일 경로 설정
file_path = '/mnt/data/ChatbotData.csv'
# CSV 파일 로드
data = pd.read_csv(file_path)

# 레벤슈타인 거리를 계산하는 함수
def levenshtein_distance(str1, str2):
    return Levenshtein.distance(str1, str2)

# 가장 유사한 질문을 찾는 함수
def find_most_similar_question(input_question, data):
    # 각 질문에 대해 레벤슈타인 거리를 계산
    distances = data['Q'].apply(lambda x: levenshtein_distance(input_question, x))
    # 최소 거리를 가진 질문의 인덱스를 찾음
    min_index = distances.idxmin()
    # 해당 인덱스와 답변을 반환
    return min_index, data.loc[min_index, 'A']

# 입력된 질문에 대해 가장 유사한 질문의 답변을 출력하는 함수
def chatbot_response(input_question, data):
    # 가장 유사한 질문을 찾아서 그에 해당하는 답변을 반환
    index, answer = find_most_similar_question(input_question, data)
    return answer

# 예시 사용
input_question = "안녕하세요"
response = chatbot_response(input_question, data)
print(response)
