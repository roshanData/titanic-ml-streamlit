import pandas as pd
	rain = pd.read_csv('train.csv')

# Fill missing age with median
train['Age'].fillna(train['Age'].median(), inplace=True)
# Convert 'Sex' to numeric
train['Sex'] = train['Sex'].map({'male': 0, 'female': 1})
# Fill Embarked and convert to numeric
train['Embarked'].fillna('S', inplace=True)
train['Embarked'] = train['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})

# Feature engineering: FamilySize
train['FamilySize'] = train['SibSp'] + train['Parch'] + 1

# Save cleaned data
train.to_csv('train_clean.csv', index=False)