import argparse
import pandas as pd
import mlflow


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument(

        "--input-data",
        dest="input_data",
        type=str
    )
    args = parser.parse_args()
    input = args.input_data
    df = pd.read_csv(input.path)
    
    mlflow.log_param("dataset", df.head())

