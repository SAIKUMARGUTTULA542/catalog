from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import dept, Base, students, User

engine = create_engine('sqlite:///dept.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

user1 = User(name="saikumar", email="saikumarguttula542@gmail.com")
session.add(user1)
session.commit()
# Menu for cse
dept1 = dept(Deptname="cse", user_id=1)

session.add(dept1)
session.commit()

student1 = students(name="sai", dept=dept1, user_id=1)

session.add(student1)
session.commit()
student2 = students(name="Gopi", dept=dept1, user_id=1)

session.add(student2)
session.commit()

dept2 = dept(Deptname="ece", user_id=1)

session.add(dept2)
session.commit()


student1 = students(name="sairam",  dept=dept2, user_id=1)

session.add(student1)
session.commit()
student2 = students(name="Gopal", dept=dept1, user_id=1)

session.add(student2)
session.commit()
print ("added menu items!")
