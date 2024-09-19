import os
import pandas as pd

def load_and_read_csv(csv_filename):
    return pd.read_csv(csv_filename)

def reorder_columns(df):
    df['PTS'] = df['PF']  
    df['PF'] = df['TOV']  
    df['BLK'] = df['STL'] 
    df['STL'] = df['AST'] 
    df['AST'] = df['TRB']
    df['TRB'] = df['DRB']
    df['FT'] = df['eFG%']
    df['G'] = df['Pos']
    df['Pos'] = df['Team']
    df['Team'] = df['Age']
    df['Age'] = df['Player']
    df['Player'] = df['Rk']
    return df.drop(columns=['Rk'])  

def filter_columns(df, columns_to_keep):
    return df[columns_to_keep]

def rename_columns(df, column_name_map):
    return df.rename(columns=column_name_map)

def save_to_csv(df, new_csv_filename):
    df.to_csv(new_csv_filename, index=False)
    print(f"Filtered data saved to {new_csv_filename}")

def main():
    print("Which NBA Season Data do you want to filter: ")
    year = input().strip()

    csv_filename = f"nba_player_stats_{year}.csv"

    if os.path.isfile(csv_filename):
        df = load_and_read_csv(csv_filename)

        df = reorder_columns(df)

        columns_to_keep = ['Player', 'Age', 'Team', 'Pos', 'G', 'FT', 'TRB', 'AST', 'STL', 'BLK', 'PF', 'PTS']  

        df_filtered = filter_columns(df, columns_to_keep)

        new_column_names = { 
            'FT': 'Free_Throws',    
            'AST': 'Assists',      
            'TRB': 'Total_Rebounds',
            'STL': 'Steals',
            'BLK': 'Blocks',
            'PF': 'Fouls',
            'Pos': 'Position',
            'G': 'Games_played',
            'PTS': 'Points'
        }

        df_filtered = rename_columns(df_filtered, new_column_names)

        new_csv_filename = "filtered_nba_player_stats_2024.csv"
        save_to_csv(df_filtered, new_csv_filename)
    else:
        print(f"Error: The file '{csv_filename}' does not exist in the directory.")

if __name__ == "__main__":
    main()
