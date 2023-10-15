## 10.11

#### Missing Values

- DROP
  
  ```python
  cols_with_missing_values = [col for col in X_train if X_train[col].isnull().any()]
  # 选出带NaN的列名，any()返回一个布尔值，用于使整个语句作为判断条件
  reduced_X_train = X_train.drop(cols_with_missing_values)
  # 使用drop方法丢弃具有缺失值的列
  ```

- IMPUTATE
  
  ```python
  imputation = SimpleImputer() # 使用代名称，方便后续重复使用
  imputated_X_train = pd.DataFrame(imputation.fit_transform(X_train)) # 拟合(fit)填充对象
  imputated_X_valid = pd.DataFrame(imputation.transform(X_valid)) # 使用之前的拟合结果，保证填充一致
  ```

#### Categorical Variables

```python
s = (X_train.dtypes == 'object') # 通过判断X_train的data type是否为object，创建一个布尔Series
object_cols = list(s[s].index) # s[s]会选择布尔Series中True的元素，index选中索引，list创建包含索引的列表
print(object_cols)
```

- DROP
  
  ```python
  drop_X_train = X_train.select_dtypes(exclude['object'])
  # 排除数据类型为object的列，将剩余的存储下来
  ```

- Ordinal Encoding
  
  ```python
  from sklearn.preprocessing import OrdinalEncoder
  ordinal_encoder = OrdinalEncoder()
  X_train[object_cols] = ordinal_encoder.fit_transform(X_train[object_cols])
  ```

- One-Hot-Encoding
  
  ```python
  from sklearn.preprocessing import OneHotEncoder
  
  OH_encoder = OneHotEncoder(handle_unknown='ignore', sparse=False) # 设置处理未知类型的方式和不生成稀疏矩阵
  OH_cols_train = pd.DataFrame(OH_encoder.fit_transform(X_train[object_cols]))
  OH_cols_valid = pd.DataFrame(OH_encoder.transform(X_valid[object_cols]))
  
  OH_cols_train.index = X_train.index
  OH_cols_valid.index = X_valid.index # 保持索引一致
  
  num_X_train = X_train.drop(object_cols, axis=1)
  num_X_valid = X_valid.drop(object_cols, axis=1) # 删去原分类列
  
  OH_X_train = pd.concat([num_X_train, OH_cols_train], axis=1)
  OH_X_valid = pd.concat([num_X_valid, OH_cols_valid], axis=1) # 合并独热编码与原数据集
  
  OH_X_train.columns = OH_X_train.columns.astype(str)
  OH_X_valid.columns = OH_X_valid.columns.astype(str) # 确保每一列的列名的数据类型为str
  
  
  
  ```

    # 怎么会这么长！>^<。
    ```

## 10.12

#### Pipelines

```python
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder

# step1. preprocess data
# create transformers for numerical and categorical data respectively
numerical_transformer = SimpleImputer(strategy = 'constant')
# use SimpleImputer and use constant number which normal is zero
categorical_transformer = Pipeline(
    steps[
        ('imputer',SimpleImputer(strategy = 'most_frequent')),
        ('onehot',OneHotEncoder(handle_unknown = 'ignore'))
])
# steps of Pipeline includes three parts,first is transformer's name
# second is transformer

# Bundle proprecessing for numerical and categorical data
preprocessor = ColumnTransformer(
    transformers = [
        ('num',numerical_transformer,numerical_cols),
        ('cat',categorical_transformer,categorical_cols)
])

# step2. Define the model
from sklearn.ensemble import RandonForestRegressor
model = RandomForestRegressor(n_estimators = 100,random_state = 0)

# step3. create and evaluate the Pipeline
# Bundle preprocessing data and modeling
my_pipeline = Pipeline(
    steps = [
        ('preprocessing',preprocessing),
        ('model',model)
])
my_pipeline.fit(X_train,y_train)
preds = my_pipeline(X_test)

from sklearn.metrics import mean_absolute_error
score = mean_absolute_error(y_valid,preds)

# 怎么比前面一个还长！:(
```

#### Cross-Validation

- [[Featuring Engineering]]
- [[cross-validation]]

#### XGBoost

- [[xgboost]]
  
  ```python
  from xgboost import XGBRegressor
  model = XGBRegressor(n_estimators = 100,learning_rate = 0.05)
  model.fit(X_train,y_train,
          early_stopping_rounds = 5,
          eval_set = [(X_valid,y_valid)],
          verbose = False
         )
  ```

#### data leakage

[[data leakage]]
