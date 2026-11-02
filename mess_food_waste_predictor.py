# AI Mess Food Waste Predictor
# This simple project uses a basic AI search technique: Hill Climbing.
# It does not need a dataset, machine learning, or extra libraries.

print("=" * 45)
print("       AI MESS FOOD WASTE PREDICTOR")
print("=" * 45)

# Ask how many students are expected for the meal.
students = int(input("How many students are expected? "))

# Ask how much food one serving needs, in grams.
serving_size = float(input("Food per student in grams (example: 300): "))

# Hill climbing starts with a simple guess for the number of servings.
current_servings = max(1, students)

# This score is better when prepared food is close to the target amount.
def score(servings):
    prepared_food = servings * serving_size
    target_food = students * serving_size * 1.03  # Keep a 3% safety buffer.
    return -abs(prepared_food - target_food)

# Try nearby serving counts and keep a choice when it improves the score.
step = max(1, students // 20)

while step >= 1:
    improved = False

    # Check a little less food and a little more food.
    for change in (-step, step):
        new_servings = current_servings + change

        # The number of servings cannot be less than one.
        if new_servings < 1:
            continue

        if score(new_servings) > score(current_servings):
            current_servings = new_servings
            improved = True

    # If neither choice was better, search with a smaller step.
    if not improved:
        step //= 2

# Show the recommendation.
recommended_servings = current_servings
recommended_food = recommended_servings * serving_size

print("\n--- AI Recommendation ---")
print(f"Expected students: {students}")
print(f"Food per serving: {serving_size:.0f} grams")
print(f"Recommended servings to prepare: {recommended_servings}")
print(f"Approximate total food: {recommended_food:.0f} grams")
print(f"Safety buffer: {recommended_servings - students} servings")

print("\nAI approach: Hill Climbing Search")
print("The program checks nearby preparation amounts and keeps")
print("a better option until it finds a suitable recommendation.")
print("\nNote: This is a simple planning demonstration, not a")
print("prediction trained on real consumption data.")
