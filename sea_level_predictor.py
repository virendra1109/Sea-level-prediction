import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Step 1: Read the data from the CSV file
df = pd.read_csv('epa-sea-level.csv')

# Step 2: Create a scatter plot
def draw_plot():
    plt.figure(figsize=(10, 6))
    
    # Scatter plot using 'Year' as the x-axis and 'CSIRO Adjusted Sea Level' as the y-axis
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Original Data')
    
    # Step 3: Perform linear regression on all the data
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Predict sea level through 2050 based on the whole dataset
    years_extended = pd.Series([i for i in range(1880, 2051)])
    sea_levels_predicted = intercept + slope * years_extended
    plt.plot(years_extended, sea_levels_predicted, color='red', label='Best Fit Line 1880-2050')
    
    # Step 4: Perform linear regression on data from year 2000
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    
    # Predict sea level through 2050 based on data from 2000 onwards
    recent_years_extended = pd.Series([i for i in range(2000, 2051)])
    recent_sea_levels_predicted = intercept_recent + slope_recent * recent_years_extended
    plt.plot(recent_years_extended, recent_sea_levels_predicted, color='green', label='Best Fit Line 2000-2050')
    
    # Step 5: Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Step 6: Add a legend
    plt.legend()

    # Step 7: Save plot and return it
    plt.savefig('sea_level_plot.png')
    return plt.gca()
