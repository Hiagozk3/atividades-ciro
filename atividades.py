import pandas as pd

url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
df = pd.read_csv(url)

# Questão 1
df["Survived"] == 1
df[df['Survived'] == 1]

print(df[df['Survived'] == 1])

# Questão 2
df["Pclass"] == 1
df["Age"] < 18

df[
    (df['Pclass'] == 1) &
    (df['Age'] < 18)
]

print(
    df[
        (df['Pclass'] == 1) &
            (df['Age'] < 18)
        ][['Name', 'Age', 'Pclass']]
    )

# Questão 3
print(
    len(
        df[df["Survived"] == 1]
    )
)

print(
    len(
        df[df["Pclass"] == 1]
    )
)

print(
    len(
        df[
            (df["Survived"] == 1) &
            (df["Pclass"] == 1)
        ]
    )
)

S = len(df[df["Survived"] == 1])
C = len(df[df["Pclass"] == 1])
intersecao = len(
    df[
        (df["Survived"] == 1) &
        (df["Pclass"] == 1)
    ]
)

S + C - intersecao
print(S + C - intersecao)