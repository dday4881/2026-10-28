# """실습 04: 다른 행의 통계나 정답을 사용하지 않는 파생 열 하나를 만듭니다."""
# from pathlib import Path
# import pandas as pd
# import numpy as np
# raw = pd.read_csv(Path(__file__).resolve().parent / "requests.csv")
# # 원본 파일은 덮어쓰지 않습니다. 글자 수만 복사하고 정답·실행시간은 선택하지 않습니다.
# features = raw[["input_chars"]].copy()
# # TODO B04: np.log1p로 글자 수의 로그 변환 열을 추가하세요. 각 행의 값만 사용합니다.
# features["log_input_chars"] = 0.0
# # TODO 끝
# print(features.head().round(3).to_string(index=False))
# print("행/열:", features.shape)
# print("원본 열:", raw.columns.tolist())

"""실습 04: 다른 행의 통계나 정답을 사용하지 않는 5파생 열 하나를 만듭니다."""
from pathlib import Path
import pandas as pd
import numpy as np
raw = pd.read_csv(Path(__file__).resolve().parent / "requests.csv")
# 원본 파일은 덮어쓰지 않습니다. 글자 수만 복사하고 정답·실행시간은 선택하지 않습니다.
features = raw[["input_chars"]].copy()
# TODO B04: np.log1p로 글자 수의 로그 변환 열을 추가하세요. 각 행의 값만 사용합니다.
features["log_input_chars"] = np.log1p(features) #위에 적힌 힌트 np.log1p를 사용하여 값을 적어줘야한다 그냥 np.log1p만 쓰면 출력 값이 <ufunc 'log1p'>라는 문구가 나오기 때문이야
# TODO 끝                               # np.log1p 괄호 안에 수를 하나만 줄 수 있는데 윗줄에 features에 값이 들어간 것을 확인하여 수를 features로 넣은 후 4.615 5.303 ··· 확인 
print(features.head().round(3).to_string(index=False))
print("행/열:", features.shape)
print("원본 열:", raw.columns.tolist())

""" 출력 결과 값
 input_chars  log_input_chars
         100            4.615
         200            5.303
         300            5.707
         400            5.994
         500            6.217
행/열: (20, 2)
원본 열 : ['request_id', 'input_chars', 'task_type', 'failed', 'elapsed_ms'] """