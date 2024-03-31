from collections import Counter
from dash import dash_table
import pandas as pd

def dezena_frequency_table(selected_buttons: list):
    # Adjusted to directly use the uploaded file's path for demonstration
    df = pd.read_csv('/mnt/data/sorteios-secundario.csv')  # Use the correct path here
    
    matches = []
    
    # Convert selected_buttons to a Counter for easy counting
    selected_counter = Counter(selected_buttons)
    
    # Iterate over DataFrame rows
    for index, row in df.iterrows():
        # Extract numbers from the row based on the provided column names
        row_numbers = [row['1ª'], row['2ª'], row['3ª'], row['4ª'], row['5ª'], row['6ª']]
        row_counter = Counter(row_numbers)
        
        # Calculate matches considering repetitions
        match_count = sum(min(selected_counter[num], row_counter[num]) for num in selected_counter)
        
        # Calculate the actual matching numbers considering repetitions
        matching_numbers = list((selected_counter & row_counter).elements())
        
        # Append match count, Conc., and matching numbers if there are matches
        if match_count > 0:
            matches.append((row['Conc.'], match_count, matching_numbers))
    
    # Convert matches to DataFrame
    matches_df = pd.DataFrame(matches, columns=['Conc.', 'MatchCount', 'MatchingNumbers'])
    
    # Convert matching numbers list to a string for display
    matches_df['MatchingNumbers'] = matches_df['MatchingNumbers'].apply(lambda x: ', '.join(map(str, x)))
    
    # Sort by MatchCount in descending order
    sorted_matches_df = matches_df.sort_values(by='MatchCount', ascending=False)
    
    # Return as a Dash DataTable
    return dash_table.DataTable(
        id='table',
        columns=[{"name": i, "id": i} for i in sorted_matches_df.columns],
        data=sorted_matches_df.to_dict('records'),
    )
    
    
