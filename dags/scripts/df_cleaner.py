import pandas as pd
import json


class DataFrameCleaner:
    def __init__(self):
        self.df = pd.DataFrame()
        self.config = self._get_cleaning_config()

    def clean(self, df: pd.DataFrame) -> pd.DataFrame:
        self.df = df.copy()
        self._drop_empty_columns()
        self._cast_columns_to_string()
        self._cast_id_columns_to_string()
        self._ensure_seconds_in_columns()
        self._cast_columns_to_datetime()
        self._cast_timestamp_columns_to_datetime()
        return self.df

    def _get_cleaning_config(self) -> dict:
        with open("dags/scripts/config/data_cleaning_config.json", "r") as f:
            config = json.load(f)
        return config

    def _drop_empty_columns(self):
        self.df = self.df.dropna(axis=1, how="all")

    def _cast_columns_to_string(self):
        for col in self.config.get("columns_cast_to_string", []):
            if col in self.df.columns:
                self.df[col] = self.df[col].astype(str)

    def _cast_id_columns_to_string(self):
        for col in self.config.get("id_columns_cast_to_string", []):
            if col in self.df.columns:
                self.df[col] = self.df[col].apply(
                    lambda x: "{:.0f}".format(x) if isinstance(x, float) else x
                )

    def _ensure_seconds_in_columns(self):
        for col in self.config.get("ensure_seconds_in_columns", []):
            if col in self.df.columns:
                self.df[col] = self.df[col].apply(
                    lambda x: (
                        x + ":00" if isinstance(x, str) and x.count(":") == 1 else x
                    )
                )

    def _cast_columns_to_datetime(self):
        for col in self.config.get("columns_cast_to_datetime", []):
            if col in self.df.columns:
                self.df[col] = pd.to_datetime(self.df[col])

    def _cast_timestamp_columns_to_datetime(self):
        for col in self.config.get("timestamp_columns_cast_to_datetime", []):
            if col in self.df.columns:
                self.df[col] = pd.to_datetime(self.df[col], unit="s")
