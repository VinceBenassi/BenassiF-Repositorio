import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#import seaborn as sns


url = ('/home/francob/Documentos/status.csv')
data = pd.read_csv(url)

print(data.shape, '\n')
print(data.img_name.unique())
print(data.info)