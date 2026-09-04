import pandas as pd

new_york_state_df = pd.read_csv('new_york_state_df.csv')
east_coast_states_df = pd.read_csv('east_coast_states_df.csv')
midwest_states_df = pd.read_csv('midwest_states_df.csv')
west_coast_states_df = pd.read_csv('west_coast_states_df.csv')

print('\n new york state df:\n', new_york_state_df)
print('\n east coast states df:\n', east_coast_states_df)
print('\n midwest states df:\n', midwest_states_df)
print('\n west coast states df:\n', west_coast_states_df)

print(new_york_state_df[new_york_state_df['scholarships_available'] == 'Yes'])