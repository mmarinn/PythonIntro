from AnalysisRequest import AnalysisRequest
from AnalysisValidator import AnalysisValidator
from flask import request, Flask
import requests

app = Flask(__name__)


def main(name):
    print(f'Hi, {name}')
    analysis_request = AnalysisRequest(100, "matheus")
    analysis_validator = AnalysisValidator()

    buyer_name = analysis_validator.validate(analysis_request)
    print(buyer_name)


@app.route('/users/<user_id>', methods=['GET'])
def user(user_id):
    if request.method == 'GET':
        response = requests.get("https://swapi.dev/api/planets/1/")

        return response.text


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
