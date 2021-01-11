import os
import pandas as pd
excels = [
    pd.read_excel('./' + fname)
    for fname in os.listdir('./')
    if '.xlsx' in fname
]
df = pd.concat(excels)
df.to_excel('./结果文件.xlsx', index=False)
