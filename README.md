# MLFlow で何個まで experiments を作れるか実験

## 普通に実行

```sh
pipenv install
pipenv shell
python create_experiments 1000
mlflow ui
```

## SQLite を使う

```sh
pipenv install
pipenv shell
python create_experiments 1000 --use_sqlite
mlflow ui
```
