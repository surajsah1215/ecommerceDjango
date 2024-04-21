
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import pandas as pd

class ProductRecommender:
    def __init__(self, products):
        self.products = products
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.tf_idf_matrix = self.vectorizer.fit_transform(products['description'])

    def get_recommendations(self, product_id, num_recommendations=5):
        product_idx = self.products.index[products['id'] == product_id].tolist()[0]
        cosine_similarities = linear_kernel(self.tf_idf_matrix[product_idx], self.tf_idf_matrix).flatten()
        related_product_indices = cosine_similarities.argsort()[:-num_recommendations-1:-1]
        return self.products.iloc[related_product_indices]
    
    def get_recommendations_for_user(self, user_id):
        # Placeholder implementation
        # Replace this with your actual recommendation logic
        return self.products.sample(user_id)

# Dummy data
products_data = {
    'id': [1, 2, 3, 4, 5],
    'name': ['Product 1', 'Product 2', 'Product 3', 'Product 4', 'Product 5'],
    'description': ['Description 1', 'Description 2', 'Description 3', 'Description 4', 'Description 5']
}
products = pd.DataFrame(products_data)

recommender = ProductRecommender(products)
