from flask import Flask, jsonify
import tfidf_adder

app = Flask(__name__)

@app.route('/<query>', methods=['GET'])
def search_result(query):
    # Call the search_documents function from tfidf_adder to get results and their indices
    results, indices = tfidf_adder.document_search_main(query)

    # Filter out None results
    filtered_results = [(result[0], result[1], idx) for result, idx in zip(results, indices) if result is not None]

    # Convert the results into a list of dictionaries with appropriate keys
    new_results = [{"score": str(score), "title": title, "index": str(idx)} for score, title, idx in filtered_results]

    # Return the results as JSON
    return jsonify(new_results)

if __name__ == '__main__':
    app.run(debug=True)
