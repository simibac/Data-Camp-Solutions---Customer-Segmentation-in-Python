# Create a groupby object and pass the monthly cohort and cohort index as a list
grouping = online.groupby(["CohortMonth", "CohortIndex"]) 

# Calculate the average of the unit price column
cohort_data = grouping["UnitPrice"].mean()

# Reset the index of cohort_data
cohort_data = cohort_data.reset_index()

# Create a pivot 
average_quantity = cohort_data.pivot(index="CohortMonth", columns="CohortIndex", values="UnitPrice")
print(average_quantity.round(1))