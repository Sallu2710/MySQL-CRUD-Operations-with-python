```markdown
# MySQL CRUD Operations with Python

A Python program to perform CRUD operations on a MySQL database.

## Prerequisites

- Python 3.x
- MySQL Server
- `mysql-connector-python` library

## Installation

1. Install MySQL Server if not already installed. Follow the official [MySQL Installation Guide](https://dev.mysql.com/doc/refman/8.0/en/installing.html) for instructions.

2. Install the `mysql-connector-python` library using pip:

    ```bash
    pip install mysql-connector-python
    ```

3. Clone this repository:

    ```bash
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

## Configuration

1. Update the MySQL connection settings in the `main.py` file with your MySQL server credentials:

    ```python
    mydb = mysql.connector.connect(
      host="localhost",
      user="yourusername",
      password="yourpassword",
      database="yourdatabase"
    )
    ```

## Usage

1. Run the program:

    ```bash
    python main.py
    ```

2. Follow the on-screen menu to create, read, update, or delete records in the `users` table of your MySQL database.

## Example

### Menu:

```
1. Create Record
2. Read Records
3. Update Record
4. Delete Record
5. Exit
```

### Create Record

```
Enter name: John Doe
Enter age: 30
Enter address: 123 Main St
Record inserted successfully.
```

### Read Records

```
(1, 'John Doe', 30, '123 Main St')
(2, 'Jane Smith', 25, '456 Elm St')
```

### Update Record

```
Enter user ID to update: 1
Enter new address: 789 Oak St
Record updated successfully.
```

### Delete Record

```
Enter user ID to delete: 2
Record deleted successfully.
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
