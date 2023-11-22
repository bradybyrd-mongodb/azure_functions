import os
import sys
#base_dir = os.path.dirname(os.path.abspath(__file__))
#sys.path.append(f'{base_dir}/lib')
import azure.functions as func
import logging
import pymongo
from bson.json_util import dumps
database = "hr"
collection = "people"
uri = "mongodb+srv://main_admin:bugsyBoo@m10basicagain-vmwqj.mongodb.net"

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="bbatlas")
def bbatlas(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        dbans = db_check(name)
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully. <br>Database: {dbans}")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
    

def db_check(pram = "none"):
    client = pymongo.MongoClient(uri)
    db = client[database]
    ans = db[collection].find_one({})
    logging.info(f'Found doc {pram} - {dumps(ans)}')
    client.close()
    return dumps(ans)