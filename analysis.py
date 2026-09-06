import pandas as pd

new_york_state_df = pd.read_csv('new_york_state_df.csv')
east_coast_states_df = pd.read_csv('east_coast_states_df.csv')
midwest_states_df = pd.read_csv('midwest_states_df.csv')
west_coast_states_df = pd.read_csv('west_coast_states_df.csv')

print('\n new york state df:\n', new_york_state_df)
print('\n east coast states df:\n', east_coast_states_df)
print('\n midwest states df:\n', midwest_states_df)
print('\n west coast states df:\n', west_coast_states_df)

print(new_york_state_df[new_york_state_df['review_score'] <= 4.0])
print("\n camps in east coast states with scholarships",east_coast_states_df[(east_coast_states_df['scholarships_available'] == 'Yes') & (east_coast_states_df['category'] == 'Sports')])

# exploratory analysis (calculations, etc.....)
def avg_age(midwest_states_df):
    try:
        return (midwest_states_df['min_age'].astype(float) + midwest_states_df['max_age'].astype(float)) / 2
    except Exception as e:
        print(f'error - cannot create new column or perform calculations at this time - {type(e)}')

midwest_states_df['avg_age'] = avg_age(midwest_states_df)
print(midwest_states_df[['camp_name','avg_age', 'city', 'state_abbr']].head(20))


def rating(x):
    try:
        if x >= 4.50:
            return "Yes"
        elif x >= 3.70 and x < 4.50: 
            return "Highly Likely"
        elif x >= 3.00 and x < 3.7: 
            return "Maybe"
        elif x >= 2.00 and x < 3.00: 
            return "Unlikely"
        elif x < 2.00:
            return "No"
    except Exception as e:
        print(f'error - unable to determine pass/fail score per review_score {type(e)}')

west_coast_states_df['recommended?'] = west_coast_states_df.apply(lambda x: rating(x['review_score']), axis="columns")
print('\n',west_coast_states_df[['camp_name','city', 'state_abbr', 'review_score', 'recommended?']].head(20))