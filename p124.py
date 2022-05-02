from flask import Flask, jsonify, request
app=Flask(__name__)
tasks=[
    {
        "Contact":9987644456,
        "Name":u"Raju",
        "done":False,
        "id":1
    },
    {
        "Contact":99876543222,
        "Name":u"Rahul",
        "done":False,
        "id":2
    },

]
@app.route("/")
def hello_world():
    return "hello world"
@app.route("/add-data",methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"ERROR",
            "message":"please provide the data"
    
        },400)
    task={
         "id":tasks[-1]["id"]+1,
        "Name":request.json["Name"],
        "Contact":request.json.get("Contact",""),
        "done":False
    }
    tasks.append(task)
    return jsonify({
            "status":"SUCCESS",
            "message":"task added successfully :)"
    })
@app.route("/get-data")
def get_task():
    return jsonify({
        "data":tasks
    })
if (__name__=="__main__"):
    app.run(debug=True)
    