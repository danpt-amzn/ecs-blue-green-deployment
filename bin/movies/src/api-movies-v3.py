from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal
from flask import Flask
from flask import jsonify
from flask import request
from boto3.dynamodb.conditions import Key, Attr
from multiprocessing import Pool
from multiprocessing import cpu_count


def f(x):
    while True:
        x*x

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

app = Flask(__name__)

@app.route("/")
def hello():
    return "Basic API Container using Python Flask"

@app.route("/Default1")
def Year():
   dynamodb = boto3.resource('dynamodb', region_name='eu-west-1')
   table = dynamodb.Table('Movies')
   print("Movies from 1985")
   response = table.query(
      KeyConditionExpression=Key('year').eq(1985)
   )
   print(json.dumps(response, cls=DecimalEncoder))
   for i in response['Items']:
    print(i['year'], ":", i['title'])
    
   for i in response[u'Items']:
    print(json.dumps(i, cls=DecimalEncoder))

   
   js = json.dumps(response, cls=DecimalEncoder)
   
   return jsonify(js)
   
@app.route("/Query")
def Query():
   dynamodb = boto3.resource('dynamodb', region_name='eu-west-1')
   table = dynamodb.Table('Movies')
   print("Movies from 1985")
   year = request.args.get('year')
   print(year)
   year_int = int(year)
   response = table.query(
      KeyConditionExpression=Key('year').eq(year_int)
   )
   
   js = json.dumps(response, cls=DecimalEncoder)
   
   return(js)

@app.route("/Query-name")
def Queryname():
   dynamodb = boto3.resource('dynamodb', region_name='eu-west-1')
   table = dynamodb.Table('Movies')
   print("Movies from 1985")
   title = request.args.get('title')
   response = table.query(
      IndexName='title-index',
      KeyConditionExpression=Key('title').eq(title)
   )
   js = json.dumps(response, cls=DecimalEncoder)
   return(js)

@app.route("/Scan")
def Scan():
   dynamodb = boto3.resource('dynamodb', region_name='eu-west-1')
   table = dynamodb.Table('Movies')
   fe = Key('year').between(1900, 2018)
   #pe = "#yr, title, info.rating, info.actors, info.directors, info.genres, info.plot"
   pe = "#yr, title, info"
   # Expression Attribute Names for Projection Expression only.
   ean = { "#yr": "year", }
   esk = None
   response = table.scan(FilterExpression=fe,ProjectionExpression=pe,ExpressionAttributeNames=ean)
   for i in response['Items']:
       print(json.dumps(i, cls=DecimalEncoder))

   while 'LastEvaluatedKey' in response:
       response = table.scan(
           ProjectionExpression=pe,
           FilterExpression=fe,
           ExpressionAttributeNames= ean,
           ExclusiveStartKey=response['LastEvaluatedKey']
           )

       for i in response['Items']:
           print(json.dumps(i, cls=DecimalEncoder))
           
   js = json.dumps(response, cls=DecimalEncoder)       
   return(js)
   
@app.route("/Hammer")
def Hammer():
   processes = cpu_count()
   print ('-' * 20)
   print ('Running load on CPU')
   print ('Utilizing %d cores' % processes)
   print ('-' * 20)
   pool = Pool(processes) 
   pool.map(f, range(processes))
   dynamodb = boto3.resource('dynamodb', region_name='eu-west-1')
   table = dynamodb.Table('Movies')
   response = table.query(
      KeyConditionExpression=Key('year').eq(1985)
   )   
   js = json.dumps(response, cls=DecimalEncoder)
   return(js)
    
if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0')
   
    



