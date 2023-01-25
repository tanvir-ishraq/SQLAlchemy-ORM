from sqlalchemy.orm import sessionmaker
import db
import random

#new session
Session = sessionmaker(bind=db.engine)
session =  Session()

#
for t in range(0, 10):
    item_id = random.randomint(0,1000)
    price = random.randint(20,50)

    tr=db.transactions(t, '2021/01/20', item_id, price)
    session.add(tr)

#save
session.commit()
