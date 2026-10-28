# """실습 03: 같은 회귀 문제에서도 주 지표에 따라 후보의 순서가 달라집니다."""
# from sklearn.metrics import mean_absolute_error, root_mean_squared_error
# y = [100, 200, 300, 400]  # 실제 실행시간(ms)
# predictions = {"A": [100, 200, 300, 480], "B": [130, 230, 330, 430]}
# for name, pred in predictions.items():
#     mae = mean_absolute_error(y, pred)
#     # TODO B03: 같은 y·pred로 RMSE를 계산하세요. 함수 이름의 root는 제곱근을 뜻합니다.
#     rmse = 0.0
#     # TODO 끝
#     print(f"{name}: MAE={mae:.1f}ms, RMSE={rmse:.1f}ms")
# print("실행시간 단위 ms를 함께 적으세요. 교차검증은 06번에서 이어집니다.")

"""실습 03: 같은 회귀 문제에서도 주 지표에 따라 후보의 순서가 달라집니다."""
from sklearn.metrics import mean_absolute_error, root_mean_squared_error
y = [100, 200, 300, 400]  # 실제 실행시간(ms)
predictions = {"A": [100, 200, 300, 400], "B": [130, 230, 330, 430]}
for name, pred in predictions.items():
    mae = mean_absolute_error(y, pred) #위에서 선행 제공된 mean_absolute_error에 선행 제공된 y 값 + predict을 받아 mae = mean_absolute_error를 받쳐 실행되게 한다
     # MAE 계산: 실제값(y)과 예측값(pred)의 절대 오차 평균을 구합니다.
        # 모든 오차를 동등하게 반영하므로, 대다수 예측이 정확한 A 모델이 더 유리하게 나옵니다.
    
    # TODO B03: 같은 y·pred로 RMSE를 계산하세요. 함수 이름의 root는 제곱근을 뜻합니다.
    rmse = root_mean_squared_error(y, pred) #mae와 같은 사례로 import root_mean_squared_error에서 값을 받아서 실행하고 결과값이 나오게 된다
    # RMSE 계산: 오차를 제곱하여 평균낸 후 제곱근(Root)을 구합니다.
        # 오차가 클수록 패널티가 제곱으로 커지므로, 한 번에 큰 오차(80ms)를 낸 A 모델보다 균일하게 틀린 B 모델이 더 유리하게 나옵니다
    # TODO 끝
    print(f"{name}: MAE={mae:.1f}ms, RMSE={rmse:.1f}ms")
print("실행시간 단위 ms를 함께 적으세요. 교차검증은 06번에서 이어집니다.")

""" 출력 결과 물
     A : MAE=20.0ms. RMSE=40.0ms
     B : MAE=30.0ms. RMSE=30.0ms
     실행시간 단위 ms를 함께 적으세요. 교차검증은 06번에서 이어집니다. """