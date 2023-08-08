from flask import Flask

app=Flask(__name__)

stores=[
    {
        "name":"My store",
        "items":[
            {
                "name":"chair",
                "price": 550
            }
        ]
    }
]