import pandas as pd

data = pd.read_csv("dataset/Student Data.csv")
print(data.head())
print(data.columns)
print(data.shape)
print(data.info())
print(data.isnull().sum())

data['Teacher_Quality'] = data['Teacher_Quality'].fillna(
    data['Teacher_Quality'].mode()[0]
)

data['Parental_Education_Level'] = data['Parental_Education_Level'].fillna(
    data['Parental_Education_Level'].mode()[0]

)

data['Distance_from_Home'] = data['Distance_from_Home'].fillna(
    data['Distance_from_Home'].mode()[0]

)

print(data.isnull().sum())

data = pd.get_dummies(data,drop_first=True)

print(data.head())
print(data.dtypes)

x = data.drop('Exam_Score', axis=1)
y = data['Exam_Score']

print("x shape:",x.shape)
print("y shape:",y.shape)

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42
)

print("x_train:", x_train.shape)
print("x_test:", x_test.shape)
print("y_train:", y_train.shape)
print("y_test:",y_test.shape)

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
print(y_pred[:10])

from sklearn.metrics import mean_absolute_error

mae = mean_absolute_error(y_test, y_pred)

print("MAE:", mae)

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

mae = mean_absolute_error(y_test, y_pred)

rmse = mean_squared_error(y_test, y_pred) ** 0.5

r2 = r2_score(y_test, y_pred)

print("MAE:", mae)
print("RMSE:", rmse)
print("R2 Score:", r2)

import joblib

joblib.dump(model, "student_model.pkl")

print("Model saved successfully!")

