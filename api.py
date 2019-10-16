from flask import Flask, request
from flask_restful import Resource, Api
import pandas as pd
import numpy as np
import random


app = Flask(__name__)
api = Api(app)

class recommendation(Resource):
    def get(self, name):

    
        dataset = pd.read_csv('out.csv', header = None, error_bad_lines=False)

        transactions = []
        for i in range(0, 19):
            transactions.append([str(dataset.values[i,j]) for j in range(0, 2)])

        cleanedList = []
        for i in range(19):
            if(name in transactions[i]):
                recc = transactions[i]
                recc.remove(name)
                cleanedList = [x for x in recc if str(x) != 'nan']
                # print(cleanedList)
                break
    

        return {'data': cleanedList}

api.add_resource(recommendation, '/<name>')

if __name__ == '__main__':
     app.run(host='0.0.0.0')
     