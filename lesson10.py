import pandas as pd

# Step 1: Open the prepared dataset

df =pd.read_parquet
# Step 2: Select Episode 1
episode = df[df['episode'] == 1].copy()

# Step 3: Put dialogue in the correct order

episode= episode.sort_values('line_idx')
# Step 4: Join dialogue into one script

script = ' '.join(episode['text'].dropna().astype(str))
# Step 5: Display the results
print(script[:500])