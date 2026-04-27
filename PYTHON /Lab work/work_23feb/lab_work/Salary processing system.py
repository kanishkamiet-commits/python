# -------------------------------------------------------
# Salary Processing System
# -------------------------------------------------------
salaries = [18000, 25000, 52000, 61000, 45000, 70000, 30000]

minimum_wage = 20000


 # Filter salaries >= minimum wage
valid_salaries = []
for s in salaries:
    if s >= minimum_wage:
        valid_salaries.append(s)

    # Add 5% bonus for salaries > 50000
for i in range(len(valid_salaries)):
    if valid_salaries[i] > 50000:
        valid_salaries[i] += valid_salaries[i] * 0.05
   
   # Sort descending
valid_salaries.sort(reverse=True)


    # Display top 3 salaries
print("Top Highest Salaries:")
for i in range(min(3, len(valid_salaries))):
    print(valid_salaries[i])
    





'''output:
Top Highest Salaries:
61500.0
52500.0
45000.0
'''
