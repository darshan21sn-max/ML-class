# Question 1: Array Creation, Reshaping, and Inspection
import numpy as np
a = np.arange(5, 101, 5)
b = a.reshape(4, 5)
print("2D Matrix:")
print(b)
print("Number of dimensions:", b.ndim)
print("Shape of matrix:", b.shape)
print("Total number of elements:", b.size)
print("Data type:", b.dtype)


# Question 2: Matrix Slicing and Sub-array Modification

import numpy as np
a = np.ones((5, 5), dtype=int)
a[1:4, 1:4] = 0
a[2, 2] = 9
print(a)


# Question 3: Element-wise Arithmetic and Aggregations
import numpy as np
prices = np.array([120, 250, 80, 450, 300])
quantities = np.array([4, 2, 10, 1, 3])

revenue = prices * quantities

total_revenue = np.sum(revenue)

average_revenue = np.mean(revenue)

highest_index = np.argmax(revenue)

print("Individual Product Revenue:", revenue)
print("Overall Combined Revenue:", total_revenue)
print("Average Revenue:", average_revenue)
print("Highest Earning Product Index:", highest_index)


# Question 4: Boolean Masking and Data Cleaning
import numpy as np
rainfall = np.array([12.5, -1.0, 0.0, 18.2, -99.0, 5.4, 22.1, 0.0, -1.0, 14.8])
valid_rainfall = rainfall[rainfall >=0]
print("Valid_rainfall:", valid_rainfall)
print("Cleaned Rainfall:", valid_rainfall)
heavy_rainfall = np.where(rainfall> 10.0)
count = len(heavy_rainfall[0])
print("Heavy Rainfall Day Position:", heavy_rainfall[0])
print("Number of Heavy Rainfall Days:", count)


# Question 5: Conditional Array Operations with np.where()

import numpy as np
np.random.seed(10)
scores = np.random.randint(20, 101, 12)
print("Original Scores:", scores)

status = np.where(scores >= 40, "Pass", "Fail")
print("Student Status:", status)

updated_scores = np.where(scores < 40, scores + 5, scores)
print("Updated Scores:", updated_scores)


# Question 6: Row-wise and Column-wise Aggregations
import numpy as np
marks = np.random.randint(50, 101, size=(6,4))
print("Student Marks :", marks)
student_avg = np.mean(marks, axis=1)
student_avg = np.round(student_avg, 2)
print("Average Marks of Each Studens:", student_avg)

highest_marks = np.max(marks, axis=0)
print("Highest marks in each subject:", highest_marks)

filtered_students = marks[student_avg > 75]
print("Students with average greater than 75:", filtered_students)


# Question 7: Feature Scaling via Broadcasting
import numpy as np
houses = np.array([
    [1200, 2, 55],
    [1800, 3, 5],
    [950, 1, 40],
    [2400, 4, 120],
    [1500, 3, 70]
])
x_min = np.min(houses, axis=0)
x_max = np.max(houses, axis=0)
x_norm = (houses - x_min) / (x_max-x_min)
print("Mininum values:", x_min)
print("Maximum values:", x_max)
print("Normalized values:", np.round(x_norm,3))

# Question 8: Combining and Stacking Arrays
import numpy as np
morning_sales = np.array([
    [15, 20],
    [10, 12],
    [25, 30]
])
evening_sales = np.array([
    [18, 22],
    [14, 15],
    [20, 28]
])
full_day_sales = np.hstack((morning_sales, evening_sales))
fourth_branch = np.array([[12,16,15,19]])
final_sales = np.vstack((full_day_sales, fourth_branch))
column_totals = np.sum(final_sales, axis=0)
print("Final 4X4 sales matrix:", final_sales)
print("Total units sold in each column:", column_totals)

# Question 9: Unique Elements and Frequency Distribution
import numpy as np
ratings = np.array(
    [5, 4, 3, 5, 2, 5, 4, 1, 3, 5,
     4, 4, 2, 5, 3, 4, 5, 1, 4, 3]
)

unique_ratings, counts = np.unique(ratings, return_counts=True)
total_responses = len(ratings)
percentages = (counts / total_responses) * 100
print("Customer Rating Frequency Distribution:")

for rating, count, percentage in zip(unique_ratings, counts, percentages):
    print(f"{rating}: {count} responses ({percentage:.1f}%)")


# Question 10: Indirect Sorting and Top-K Selection
import numpy as np
emp_ids = np.array(["E101", "E102", "E103", "E104", "E105", "E106"])
scores = np.array([78, 92, 65, 88, 95, 71])
sorted_indices = np.argsort(scores)[::-1]
sorted_emp_ids = emp_ids[sorted_indices]
sorted_scores = scores[sorted_indices]

top_3_ids = sorted_emp_ids[:3]
top_3_scores = sorted_scores[:3]
print("Sorting Indices:", sorted_indices)
print("\nTop 3 Employees:")

for emp_id, score in zip(top_3_ids, top_3_scores):
    print(f"Employee ID: {emp_id}, Score: {score}")
