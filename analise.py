import pandas as pd
import sqlite3

df = pd.read_csv('dataset/diabetes.csv')

cnn = sqlite3.connect('database/dbprojeto01.db')
df.to_sql('diabetes', cnn)

# comandos SQL

%load_ext sql
%sql sqlite: // /database/dbprojeto01.db

% % sql

SELECT Age, Glucose, Outcome FROM diabetes WHERE Glucose > 190

% % sql

INSERT INTO pacientes(Pregnancies,
                      Glucose,
                      BloodPressure,
                      SkinThickness,
                      Insulin,
                      BMI,
                      DiabetesPedigreeFunction,
                      Age,
                      Outcome)
SELECT Pregnancies,
Glucose,
BloodPressure,
SkinThickness,
Insulin,
BMI,
DiabetesPedigreeFunction,
Age,
Outcome
FROM diabetes WHERE Age > 50

% % sql

ALTER TABLE pacientes
ADD Perfil VARCHAR(10)

% % sql

UPDATE pacientes
SET Perfil = 'Normal'
WHERE BMI < 30

% % sql

UPDATE pacientes
SET Perfil = 'Obeso'
WHERE BMI >= 30

# back 2 python

query = cnn.execute("SELECT * FROM pacientes")
cols = [coluna[0] for coluna in query.description]
resultado = pd.DataFrame.from_records(data=query.fetchall(), columns=cols)
resultado.to_csv('dataset/pacientes.csv', index=False)
