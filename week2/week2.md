# MLFLOW 시작하기

MLFLOW란 머신러닝의 생애주기를 위한 오픈 소스 플랫폼의 일종이다.

![](https://i.imgur.com/ikG24ea.png)

ML 프로젝트는 기본적으로 저 위의 그림처럼

1. 데이터 준비
2. 데이터 분석
3. Feature 엔지니어링
4. 모델 학습
5. 모델 Validation
6. 배포
7. 모니터링

의 라이프사이클로 돌아가는데 MLFLOW는 이 사이클 전반에 대해 관리를 편하게 해 주는 툴이라고 보면 된다.


## 설치하기

설치는 그냥 `pip install mlflow`로 해주면 되고, import도 `import mlflow`로 간단하게 하면 된다.


## 실험 UI로 실행

실험에 대한 결과는 mlflow ui로 확인 가능하다.
터미널에

```bash
mlflow ui
```

를 입력해주면 웹브라우저에서 `http://127.0.0.1:5000`에서 실험 결과를 확인 가능하다.


## mlrun & mlflow ui

mlflow 실험 추적은 기본적으로 mlflow ui에 의존하기 때문에 mlflow ui가 실행되지 않으면 5000번 포트에서도 실험 결과를 확인할 수 없다.
또한 mlrun 디렉토리(깃허브에는 올리지 않았지만)을 삭제하면 실험 추적이 되지 않는다.


# First ML Project With MLFLOW

`week2/1-MLProject` 디렉토리의 ipynb파일을 확인해보자.
여기서는 아이리스 데이터를 이용한 간단한 ML 프로젝트를 로깅하는 것을 보여주고 있는데, 파라미터를 입력하고 이를 적합시킨 후 accuracy까지 측정한 후 mlflow ui에서 이를 로깅하는 코드가 존재한다.

기본적으로

```python

mlflow.set_tracking_uri(uri="http://127.0.0.1:5000")

## New Mlflow experiment
mlflow.set_experiment("MLFLOW Quickstart")

## Start the MLflow run
with mlflow.start_run():
    mlflow.log_params(params)

    ## Log accuracy metrics
    mlflow.log_metric("accuracy", accuracy)
    mlflow.set_tag("Training Info", "Basic LR model for iris data")

    ## Infer the model signature
    signature = infer_signature(X_train, lr.predict(X_train))

    ## Log the model
    model_info = mlflow.sklearn.log_model(
        sk_model = lr,
        artifact_path = "iris_model",
        signature = signature,
        input_example = X_train,
        registered_model_name = "tracking-quickstart",
    )
```
형태의 코드로 실험을 로깅할 수 있다.


여기서 좀 더 눈여겨 볼 것은 파라미터를 바꿔서 적합시킨 후 다시 로깅할 수 있는데, mlflow ui에서 두 실험을 모두 확인해볼 수 있다.
또한 실험 두 개의 체크박스를 클릭 후 `Compare`를 누르면 두 실험의 결과를 비교하고, 이를 바탕으로 더 나은 파라미터를 고를 수 있다는 것이다.




