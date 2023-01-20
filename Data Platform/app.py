import boto3
from flask import Flask,render_template

app = Flask(__name__)

client = boto3.resource('dynamodb')
a11_table = client.Table('a11')
data = []
for item in a11_table.scan()['Items']:
    #print(item)
    dummy = []
    t = item['payload']['Temperature']
    t = int(t)
    h = item['payload']['Humidity']
    h = int(h)

    dummy.append(t)
    dummy.append(h)
    data.append(dummy)

@app.route('/')
def homepage():
    return render_template('index.html',dashboard_data=data,len = len(data))

if __name__ == "__main__":
    app.run(host = '0.0.0.0')
