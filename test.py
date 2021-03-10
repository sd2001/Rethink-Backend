import json   
       
# Data to be written   
dictionary ={   
  "id": "04",   
  "name": "sunil",   
  "depatment": "HR"
}   
       
# Serializing json    
json_object = json.dumps(dictionary, indent = 4)   
print(json_object)
print(type(json_object))