from flask_main import *
import arrow 

import nose



def test_regular():
	'''
	Tests creating certain memos
	'''
    db.collections.insertOne(
    {
    "_id": {
        "$oid": "5a012b6674fece54caaa988b"
    },
    "text": "Do Laundry",
    "date": "2016-02-10"
    }
    assert get_memos("Do Laundry") == "_id": {"$oid": "5a012b6674fece54caaa988b"}
    
    
    
    db.collections.insertOne(
  {
    "_id": {
        "$oid": "5a012d5474fece634399a5f8"
    },
    "text": "new years",
    "date": "2015-01-01"
}
    assert get_memos("new years") == "_id": {"$oid": "5a012d5474fece634399a5f8"}
   
   
   {
    "_id": {
        "$oid": "5a012daa74fece634399a5f9"
    },
    
    "text": "christmas",
    "date": "2005-02-12"
}
    
    assert get_memos("christmas") == "_id": {"$oid": "5a012daa74fece634399a5f9"}

    
    
    
    
    