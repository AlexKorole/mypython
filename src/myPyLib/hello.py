import numpy as np
import pandas as pd

def SayHello(name):
    print("Hello ", name)

def CheckPandas():
    s = pd.Series([1, 3, 5, np.nan, 6, 8])
    print(s)