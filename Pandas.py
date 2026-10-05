import numpy as np
import pandas as pd

np.random.seed(42)
data = np.random.randint(1,101,10)
tab = pd.Series(data)

print(f"NumPy Array: {data}\n")
print(f"Pandas Table:\n{tab}\n")