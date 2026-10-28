# from sklearn.metrics import (confusion_matrix,
# accuracy_score, precision_score, recall_score,
# f1_score)
# cm = confusion_matrix(y, pred, labels=[0, 1])
# print(cm)
# print(accuracy_score(y, pred))
# print(precision_score(y, pred, zero_division=0))
# print(recall_score(y, pred, zero_division=0))
# print(f1_score(y, pred, zero_division=0))

# y = np.array([0]*14 + [1]*6)
# pred = np.zeros(20, dtype=int)
# print(accuracy_score(y, pred))
# print(recall_score(y, pred, zero_division=0))
# print(f1_score(y, pred, zero_division=0))

# from sklearn.metrics import roc_curve, roc_auc_score
# y = np.array([0, 0, 1, 1])
# p = np.array([0.10, 0.40, 0.35, 0.80])
# fpr, tpr, thresholds = roc_curve(y, p)
# print(fpr)
# print(tpr)
# print(roc_auc_score(y, p))

# for t in [0.5, 0.3]:
# pred = (p > t).astype(int)
# tn, fp, fn, tp = confusion_matrix(
# y, pred, labels=[0, 1]).ravel()
# cost = fp + 5 * fn
# print(t, fp, fn, cost)
# # 비용 5:1은 설명용 가정, 실제 업무 근거가 아님

# from sklearn.metrics import mean_absolute_error
# from sklearn.metrics import root_mean_squared_error
# y = [100, 200, 300, 400]
# a = [100, 200, 300, 480]
# b = [130, 230, 330, 430]
# for name, pred in [('A', a), ('B', b)]:
# print(name, mean_absolute_error(y, pred),
# root_mean_squared_error(y, pred))

# from sklearn.model_selection import cross_validate
# scores = cross_validate(
# pipe, X_train, y_train, cv=CLS_FOLDS,
# scoring={'f1': 'f1', 'auc': 'roc_auc'},
# return_train_score=True, error_score='raise',
# n_jobs=1)
# print(scores['test_f1'])
# print(scores['test_f1'].mean())
# # test_f1의 test는 fold 평가12건, 보관test20 아님

# scores = cross_validate(
# build(LinearRegression()), X_train, yr_train,
# cv=REG_FOLDS,
# scoring='neg_root_mean_squared_error',
# n_jobs=1, error_score='raise')
# rmse = -scores['test_score']
# print(rmse)
# print(rmse.mean())  # 단위: ms

# def add_features(X):
# out = X.copy()
# out['log_input_chars'] = np.log1p(out['input_chars'])
# out['chars_per_slot'] = (
# out['input_chars'] / (1.0 + out['allowed_tools']))
# return out
# # 전체 예제에는 열·비음수·무한대 검사도 포함

# features = FunctionTransformer(
# add_features, validate=False)
# pipe = Pipeline([
# ('features', features),
# ('pre', make_pre(engineered=True)),
# ('model', LogisticRegression(C=1, max_iter=1000))])
# pipe.fit(X_train, y_train)
# print(pipe[:-1].transform(X_train).shape)
# print(pipe[:-1].transform(X_valid).shape)

# for name in ['Logistic', 'Logistic_FE']:
# pipe = candidates()[name]
# cv = cross_validate(pipe, X_train, y_train,
# cv=CLS_FOLDS, scoring='f1', n_jobs=1)
# pipe.fit(X_train, y_train)
# print(name, cv['test_score'].mean(),
# f1_score(y_valid, pipe.predict(X_valid)))

# cv = cross_validate(pipe, X_train, y_train,
# cv=CLS_FOLDS, scoring='f1', return_estimator=True)
# for (fit_idx, _), fitted in zip(
# CLS_FOLDS, cv['estimator']):
# values = add_features(X_train.iloc[fit_idx])
# expected = values[NUM + DERIVED].median()
# num = fitted['pre'].named_transformers_['num']
# actual = num['imputer'].statistics_
# assert np.allclose(expected.to_numpy(), actual)

