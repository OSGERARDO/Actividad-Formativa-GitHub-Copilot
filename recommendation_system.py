# Simple recommendation system
# This script recommends products to users based on their preferences.
# It uses a very basic scoring approach: products matching the user's
# preferred categories or tags get a higher score.

# Sample product catalog. Each product has a name, category, and tags.
products = [
    {
        "id": 1,
        "name": "Wireless Headphones",
        "category": "electronics",
        "tags": ["music", "tech", "travel"],
    },
    {
        "id": 2,
        "name": "Running Shoes",
        "category": "sports",
        "tags": ["fitness", "outdoor", "health"],
    },
    {
        "id": 3,
        "name": "Smartwatch",
        "category": "electronics",
        "tags": ["fitness", "tech", "health"],
    },
    {
        "id": 4,
        "name": "Cookbook",
        "category": "books",
        "tags": ["cooking", "education", "home"],
    },
    {
        "id": 5,
        "name": "Action Camera",
        "category": "electronics",
        "tags": ["travel", "outdoor", "tech"],
    },
    {
        "id": 6,
        "name": "Yoga Mat",
        "category": "sports",
        "tags": ["fitness", "health", "home"],
    },
]

# Sample user preferences.
# Each user has a list of interests that act as the basis for recommendations.
users = {
    "Ana": ["music", "travel", "fitness"],
    "Luis": ["tech", "gaming", "electronics"],
    "Maria": ["health", "home", "cooking"],
}


def recommend_products(user_name, user_preferences, product_list, limit=3):
    """
    Return the top recommended products for a user.

    The function compares the user's interests with each product's tags.
    A product gets a score for every matching interest and is then sorted
    from highest to lowest score.
    """
    if user_name not in user_preferences:
        raise ValueError(f"User '{user_name}' not found in the sample data.")

    # Convert the user's interests into a set for faster matching.
    preferences = set(user_preferences[user_name])
    scored_products = []

    # Check every product and calculate a score.
    for product in product_list:
        score = 0

        # Give a higher score when the product matches the user's interests.
        for tag in product["tags"]:
            if tag in preferences:
                score += 2

        # Additional point for matching the main category.
        if product["category"] in preferences:
            score += 1

        # Only keep products that actually match something.
        if score > 0:
            scored_products.append((product["name"], score))

    # Sort products by score, from best to worst.
    recommended = sorted(scored_products, key=lambda item: item[1], reverse=True)
    return recommended[:limit]


# Example usage: display recommendations for each user.
if __name__ == "__main__":
    print("Recommendation system demo\n")

    for user_name in users:
        recommendations = recommend_products(user_name, users, products)
        print(f"Recommendations for {user_name}:")

        if not recommendations:
            print("No recommendations found.")
        else:
            for index, (product_name, score) in enumerate(recommendations, start=1):
                print(f"  {index}. {product_name} (score: {score})")

        print()
