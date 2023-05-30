import psycopg2
from statistics import mean, median, variance
from collections import Counter

monday = ['GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE', 'PINK', 'BLUE', 'YELLOW', 'ORANGE', 'CREAM', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'GREEN']
tuesday = ['ARSH', 'BROWN', 'GREEN', 'BROWN', 'BLUE', 'BLUE', 'BLEW', 'PINK', 'PINK', 'ORANGE', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'WHITE', 'BLUE', 'BLUE', 'BLUE']
wednesday = ['GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE', 'PINK', 'RED', 'YELLOW', 'ORANGE', 'RED', 'ORANGE', 'RED', 'BLUE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'WHITE', 'WHITE']
thursday = ['BLUE', 'BLUE', 'GREEN', 'WHITE', 'BLUE', 'BROWN', 'PINK', 'YELLOW', 'ORANGE', 'CREAM', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'GREEN']
friday = ['GREEN', 'WHITE', 'GREEN', 'BROWN', 'BLUE', 'BLUE', 'BLACK', 'WHITE', 'ORANGE', 'RED', 'RED', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'WHITE']

#adding all the colors to one list
colors = monday + tuesday + wednesday + thursday + friday

# 1. Calculate the mean color
mean_color = mean(colors)
print(f'Mean color: {mean_color}')

# 2. Calculate the color mostly worn throughout the week
color_count = Counter(colors)
most_common_color = color_count.most_common(1)[0][0]
print("Most Worn Color:", most_common_color)

# 3. Calculate the median color
sorted_colors = sorted(colors)
mid_index = len(sorted_colors) // 2
median_color = sorted_colors[mid_index]
print("Median Color:", median_color)

# 4. Calculate the variance of the colors
color_variance = variance(colors)
print("Color Variance:", color_variance)

# 5. Calculate the probability of choosing red
red_count = color_count['RED']
total_colors = len(colors)
red_probability = red_count / total_colors
print("Probability of choosing Red:", red_probability)

# 6. Save the colors and their frequencies in PostgreSQL database
conn = psycopg2.connect(database="your_database_name", user="your_username", password="your_password", host="your_host", port="your_port")
cur = conn.cursor()

for color, frequency in color_count.items():
    cur.execute("INSERT INTO colors (color, frequency) VALUES (%s, %s)", (color, frequency))

conn.commit()
cur.close()
conn.close()

# 7. Recursive searching algorithm to search for a number entered by the user in a list of numbers
def recursive_search(number, num_list):
    if not num_list:
        return False
    if num_list[0] == number:
        return True
    return recursive_search(number, num_list[1:])

user_input = int(input("Enter a number to search: "))
result = recursive_search(user_input, [1, 2, 3, 4, 5, 6, 7, 8, 9])

if result:
    print("Number found!")
else:
    print("Number not found!")

# Generate random 4-digit number of 0s and 1s
binary_number = ""
for _ in range(4):
    binary_number += str(random.randint(0, 1))

# Convert binary number to base 10
decimal_number = int(binary_number, 2)

print("Binary number:", binary_number)
print("Decimal number:", decimal_number)



# fibonacci
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        while len(fib_sequence) < n:
            next_number = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_number)
        return fib_sequence

fibonacci_sequence = fibonacci(50)
sum_fibonacci = sum(fibonacci_sequence)

print("Fibonacci sequence:", fibonacci_sequence)
print("Sum of the first 50 Fibonacci numbers:", sum_fibonacci)



