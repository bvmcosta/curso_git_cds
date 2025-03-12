import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit

def load_data():

    return pd.read_csv('data/processed/bikes_completed.csv')

def main():

    df = load_data()

    print(df)


if __name__ == '__main__':

    main()

