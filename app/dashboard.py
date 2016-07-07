from app import app, mysql

def loadSubscribers():
	conn = mysql.connect()
	cursor = conn.cursor()
	cursor.execute("SELECT id, name, email, phone_num FROM SUBSCRIBERS")
	data = cursor.fetchall()	
	cursor.close ()
  	conn.close ()
	print data
	return data

def deleteSubscribers(id):
	conn = mysql.connect()
	cursor = conn.cursor()
	cursor.execute("DELETE FROM SUBSCRIBERS WHERE ID=%s", [id])
	cursor.close()
	conn.commit()
	conn.close()
	return True
