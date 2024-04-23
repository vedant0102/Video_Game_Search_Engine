from flask import Flask, jsonify, redirect, url_for, request, render_template
import tfidf_adder

app = Flask(__name__)

@app.route('/<query>', methods=['GET'])
def search_result(query):
    results = tfidf_adder.search_documents(query)
    filtered_results = [result for result in results if result[0] != 0]
    print(jsonify(results))
    return jsonify(results)
    link_component = ''.join(f'<div><a href={result[1]}>{result[1].split("/")[-1]}</a></div>' for result in filtered_results)
    return link_component

if __name__ == '__main__':
    app.run(debug=True)