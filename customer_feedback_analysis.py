def calculate_positive_feedback_percentage(ratings):
    if len(ratings) == 0:
        return "No ratings available."
    
    positive_count = 0
    for rating in ratings:
        if rating >= 4:
            positive_count += 1
    
    percentage = (positive_count / len(ratings)) * 100
    return percentage

# User input
ratings_input = input("Enter customer ratings separated by spaces (1-5): ")
ratings = ratings_input.split()  # Split the input string into a list
ratings = [int(rating) for rating in ratings]  # Convert each rating to an integer

positive_feedback_percentage = calculate_positive_feedback_percentage(ratings)
print("Positive Feedback: {:.2f}%".format(positive_feedback_percentage))