# """실습 01: 실제 실패 6건인 손계산 예제입니다. 아직 모델을 학습하지 않습니다."""
# from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
# # 행은 실제, 열은 예측입니다. 1은 좋은 결과가 아니라 관심 클래스인 '실패'입니다.
# y = [0]*14 + [1]*6
# pred = [0]*10 + [1]*4 + [0]*4 + [1]*2
# print("혼동행렬(행 실제 / 열 예측, 성공0·실패1)")
# print(confusion_matrix(y, pred, labels=[0, 1]))
# # TODO B01: 네 지표 함수에 실제값 y와 예측값 pred를 순서대로 넣으세요. zero_division=0은 분모가 0일 때 0으로 표시하는 정책입니다.
# acc = precision = recall = f1 = 0.0
# # TODO 끝
# print(f"Accuracy={acc:.3f}, Precision={precision:.3f}, Recall={recall:.3f}, F1={f1:.3f}")
# print("실제 실패 6건 중 발견: 2건")


"""실습 01: 실제 실패 6건인 손계산 예제입니다. 아직 모델을 학습하지 않습니다."""
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
# 행은 실제, 열은 예측입니다. 1은 좋은 결과가 아니라 관심 클래스인 '실패'입니다.
y = [0]*14 + [1]*6 #0이 14개, 1이 6개
pred = [0]*10 + [1]*4 + [0]*4 + [1]*2 #0이 10개, 1이 4개, 0이 4개, 1이 2개 여기서 표기되는 0은 성공이고, 1은 실패의 의미로 표기
print("혼동행렬(행 실제 / 열 예측, 성공0·실패1)")
print(confusion_matrix(y, pred, labels=[0, 1])) # print 함수 안 주어진 (y, Pred)가 밑에 제공될 함수 안에도 적용 될거라는 힌트
# TODO B01: 네 지표 함수에 실제값 y와 예측값 pred를 순서대로 넣으세요. zero_division=0은 분모가 0일 때 0으로 표시하는 정책입니다.
## acc = precision = recall = f1 = 0 # 예측값과 실제값을 넣으라는 힌트를 찾아 acc 값 + precision 값 + recall 값을 적용

acc = accuracy_score(y, pred) # 1. 정확도(Accuracy): 전체 데이터(20건) 중 맞춘 데이터(성공 10건 + 실패 2건 = 12건)의 비율 ➡️ 12/20 = 0.600

## precision = recall = f1 = 0 # 윗줄 accuracy와 마찬가지로 실제값을 넣으라는 힌트에 precision 값 + recall 값 적용

precision = precision_score(y, pred, zero_division=0) # 2. 정밀도(Precision): 모델이 '실패'라고 예측한 것(총 6건) 중 진짜 실제 실패(2건)의 비율 ➡️ 2/6 = 0.333
                                                      # (zero_division=0: 혹시나 모델이 실패를 0건 예측하여 분모가 0이 될 때 에러 대신 0으로 처리함)
## recall = f1 = 0

recall = recall_score(y, pred, zero_division=0) # 3. 재현율(Recall): 실제 '실패'인 데이터(총 6건) 중 모델이 놓치지 않고 찾아낸 실패(2건)의 비율 ➡️ 2/6 = 0.333

## f1 = 0  

f1 = f1_score(y, pred, zero_division=0) # 4. F1-Score: 정밀도와 재현율의 균형을 보는 조화평균 지표 (두 값이 모두 높아야 높게 나옴) ➡️ 0.333

# TODO 끝
print(f"Accuracy={acc:.3f}, Precision={precision:.3f}, Recall={recall:.3f}, F1={f1:.3f}")
print("실제 실패 6건 중 발견: 2건")

""" 출력 표기 값
    혼동행렬(행 실제 / 열 예측, 성공0·실패1)
    [[10  4]
    [ 4  2]]
    Accuracy=0.600, Precision=0.333, Recall=0.333, F1=0.333
    실제 실패 6건 중 발견: 2건 """
