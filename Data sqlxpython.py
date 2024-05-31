import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user ="root",
    password = "2003",
    database = "mydatabase"
)

my_cursor = mydb.cursor()

def create_record():
    name = input("Enter name:")
    age = int(input("Enter age:"))
    address = input("Enter address:")
    sql = "INSERT INTO users (name,age,address) VALUES (%s,%s,%s)"
    val = (name,age,address)
    my_cursor.execute(sql,val)
    mydb.commit()
    print("Record Inserted Successfully!")
    
def read_records():
    sql = "SELECT * FROM users"
    my_cursor.execute(sql)
    result = my_cursor.fetchall()
    for row in result:
        print(row)
        
def update_record():
    user_id = int(input("Enter UserID to update:"))
    field = input("Enter the field to update(name, age,address):").strip().lower()
    new_value = input(f"Enter the new value for {field} :")
    if field not in ['name','age','address']:
        print("Invalid Field")
        return
    sql = f"UPDATE users SET {field} = %s WHERE id = %s"
    val = (new_value, user_id)
    
    my_cursor.execute(sql,val)
    mydb.commit()
    print("Record updated Successfully")

def delete_record():
    user_id = int(input("Enter userID  to Delete:"))
    sql = "DELETE FROM users WHERE id =%s"
    val = (user_id,)
    my_cursor.execute(sql,val)
    mydb.commit()
    print("Record deleted Successfully")
    
    
def main():
    while True:
        print("\nMenu:")
        print("1. Create Record")
        print("2. Read Records")
        print("3. Update Record")
        print("4. Delete Record")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            create_record()
        elif choice == '2':
            read_records()
        elif choice == '3':
            update_record()
        elif choice == '4':
            delete_record()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()