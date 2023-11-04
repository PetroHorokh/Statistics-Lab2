import func
import const

print("Task1")

allocation = []
allocation_test = []

for i in range(12):
    allocation_test.append(func.allocation())

for el in allocation_test:
    print(el)

for i in range(const.n):
    allocation.append(func.allocation())

print("Task2")
func.correlation_field(allocation)

print("Task3")
print(f"selective_average_x: {func.selective_average_x(allocation)}")
print(f"selective_average_y: {func.selective_average_y(allocation)}")
print(f"sample_variance_x: {func.sample_variance_x(allocation)}")
print(f"sample_variance_y: {func.sample_variance_y(allocation)}")
print(
    f"sample_standard_deviation_of_a_random_variable_x: {func.sample_standard_deviation_of_a_random_variable_x(allocation)}")
print(
    f"sample_standard_deviation_of_a_random_variable_y: {func.sample_standard_deviation_of_a_random_variable_y(allocation)}")
print(f"sample_correlation_coefficient: {func.sample_correlation_coefficient(allocation)}")

print("Task4")
func.significance_hypothesis_testing(allocation)
