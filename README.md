# Final Project

## Introduction
This project is a Command Line Interface (CLI) application for managing inventory items, categories, and suppliers. It allows users to list, find, create, update, and delete records in an SQLite database.

## Features
- **Manage Items**: Add, update, delete, list, and find items by name or ID.
- **Manage Categories**: Add, delete, and list categories.
- **Manage Suppliers**: Add, update, delete, and list suppliers with contact and address details.
- **Filter Items**: Filter items by category or supplier.

## Usage
1. **Run the CLI:**
    ```sh
    python lib/cli.py
    ```

2. **Navigate through the menu options:**
    - **Items Menu**
        1. List Items
        2. Find Item by Name
        3. Find Item by ID
        4. Add Item
        5. Update Item
        6. Delete Item
        7. Filter Items by Category or Supplier
        8. Back to Main Menu
    - **Categories Menu**
        1. List Categories
        2. Add Category
        3. Delete Category
        4. Back to Main Menu
    - **Suppliers Menu**
        1. List Suppliers
        2. Add Supplier
        3. Update Supplier
        4. Delete Supplier
        5. Back to Main Menu
    - **Exit Program**

## Database Schema
The project uses an SQLite database with three main tables:
- **Items**: Stores item details like name, quantity, price, category_id, and supplier_id.
- **Categories**: Stores category details like name and description.
- **Suppliers**: Stores supplier details including name, contact, and address.

## Classes and Methods
### Supplier
- **Attributes**: `id`, `name`, `contact`, `address`
- **Methods**:
    - `create_table()`, `drop_table()`, `save()`, `create()`, `get_all()`, `find_by_id()`, `find_by_name()`, `update()`, `delete()`, `instance_from_db()`

### Item
- **Attributes**: `id`, `name`, `quantity`, `price`, `category_id`, `supplier_id`
- **Methods**:
    - Similar to `Supplier` with item-specific operations

### Category
- **Attributes**: `id`, `name`, `description`
- **Methods**:
    - Similar to `Supplier` with category-specific operations

## Contributing
1. **Fork the repository**
2. **Create a feature branch:**
    ```sh
    git checkout -b feature/your-feature
    ```
3. **Commit your changes:**
    ```sh
    git commit -m 'Add some feature'
    ```
4. **Push to the branch:**
    ```sh
    git push origin feature/your-feature
    ```
5. **Open a pull request**

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE.md) file for details.

## Project by:TEDDY KIPLAGAT
