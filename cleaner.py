import pandas as pd
from sklearn.preprocessing import OneHotEncoder

class DataCleaner:
    def __init__(self, df):
        self.df = df

    def clean(self, fill_missing='mean', drop_duplicates=True, encode_categorical=True):
        df = self.df.copy()

        if fill_missing == 'mean':
            df = df.fillna(df.mean(numeric_only=True))
        elif fill_missing == 'zero':
            df = df.fillna(0)

        if drop_duplicates:
            df = df.drop_duplicates()

        if encode_categorical:
            categorical_cols = df.select_dtypes(include='object').columns
            if len(categorical_cols) > 0:
                encoder = OneHotEncoder(sparse=False, drop='first')
                encoded = encoder.fit_transform(df[categorical_cols])
                encoded_df = pd.DataFrame(
                    encoded,
                    columns=encoder.get_feature_names_out(categorical_cols),
                    index=df.index
                )
                df = df.drop(columns=categorical_cols)
                df = pd.concat([df, encoded_df], axis=1)

        return df
