import pandas as pd
from scripts.postgres_helper import upload_overwrite_table
from scripts.df_cleaner import DataFrameCleaner


def clean_and_upload_to_postgres(**kwargs):
    file_name = kwargs.get("file_name")
    table_name = file_name.split(".")[0]

    raw_df = pd.read_csv(
        f"dags/scripts/data_examples/{file_name}",
        escapechar="\\",
    )

    df_cleaner = DataFrameCleaner()
    cleaned_df = df_cleaner.clean(raw_df)

    upload_overwrite_table(cleaned_df, table_name)
