from flask import Flask, request, jsonify
from fashion_model import process_outfit
from trend_api import get_latest_trends

app = Flask(__name__)

# Endpoint to upload image and rate the outfit
@app.route('/rate-outfit', methods=['POST'])
def rate_outfit():
    if 'image' not in request.files:
        return jsonify({"error": "No image file provided"}), 400
    
    image_file = request.files['image']
    processed_outfit = process_outfit(image_file)

    trends = get_latest_trends()  # Get current fashion trends
    
    rating = compare_outfit_with_trends(processed_outfit, trends)
    
    return jsonify({"rating": rating})

# Dummy function to compare outfit and trends
def compare_outfit_with_trends(outfit, trends):
    # You can enhance this with a proper scoring algorithm
    score = 85  # Dummy score for now
    return score

if __name__ == '__main__':
    app.run(debug=True)
