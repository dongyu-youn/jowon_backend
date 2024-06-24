import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# 대회별 최대, 최소값 설정
# 대회별 최대, 최소값 설정
aptitude_test_max_min = {
    '언어 예측값': (48, 12),
    '디자인 예측값': (64, 16),
    '건축 예측값': (68, 17),
    '현재 대회 예측값': (40, 10),
    'it 예측값': (64, 16)
}


# 데이터 로드
df = pd.read_excel('jongsulData4.xlsx')

# 특성과 라벨 분리
X = df.drop(columns=aptitude_test_max_min.keys())
y = df[list(aptitude_test_max_min.keys())]

# 학습 데이터와 테스트 데이터 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 데이터 정규화
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 모델 구성
model = keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=[X_train_scaled.shape[1]]),
    layers.Dense(64, activation='relu'),
    layers.Dense(5)  # 출력층
])

# 모델 컴파일
model.compile(optimizer='adam', loss='mse', metrics=['mae'])

# 모델 학습
history = model.fit(X_train_scaled, y_train, epochs=50, validation_split=0.2)

# 모델 저장
model.save('JongsulModel5.h5')
