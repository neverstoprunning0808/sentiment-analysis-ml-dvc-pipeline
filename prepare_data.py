from omegaconf import OmegaConf
import pandas as pd
from sklearn.model_selection import train_test_split

def prepare_data(config):
    print("Preparing data....")
    df = pd.read_csv(config.data.csv_file_path)
    df["labels"] = pd.factorize(df["sentiment"])[0]
    print(df.head())
    
    test_ratio = config.data.test_set_ratio
    X = df["review"]
    y = df["labels"]

    train_df, test_df = train_test_split(df, test_size=test_ratio, stratify=df['labels'], random_state=42)

    train_df.to_csv(config.data.train_csv_save_path, index=False)
    test_df.to_csv(config.data.test_csv_save_path, index=False)


if __name__ == "__main__":
    config = OmegaConf.load("./params.yaml")
    prepare_data(config)
