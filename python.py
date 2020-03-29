#mysql connect program.
import mysql.connector

crudyoutube= mysql.connector.connect(host="localhost", user="root",passwd="")
print("crudyoutube")
if (crudyoutube):
	print("sucessful")
else:
	print("unsucessful")