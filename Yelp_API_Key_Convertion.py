import json as js

Key = {"Key":"sOALqJIhxQavR6qU2YJG72vmcsSu7PDKe616pq6znE7pY5nb5vTiw-G7oJNGB93NxD3fXPhjPVUg-pg1OkmpcuLmNpVr-OgjRFMaMhwF0EhWLbJvLkfaWn0iP31-ZHYx"}
with open("YELP_Api_Key.json","w") as d:
    js.dump(Key,d)
