# Convert object_id to id 
def convert_objectid(document: dict) -> dict:
    document["id"] = str(document["_id"])
    del document["_id"]
    return document
