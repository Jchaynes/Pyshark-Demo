<span style="color:green"><em>Unclassified</em></span>
# Dictionaries
1. Creating a Dictionary:
   * You can create a dictionary by enclosing key-value pairs in curly braces `{}`.
   * Keys are unique and associated with their corresponding values using a colon `:`.
   * Example:
     ```python
     student = {
         "name": "John",
         "age": 20,
         "grade": "A",
         "is_enrolled": True
     }
     ```

2. Accessing Dictionary Values:
   * You can access the values in a dictionary by specifying the corresponding key.
   * Use the square bracket notation `[]` with the key inside to access the value.
   * Example:
     ```python
     student = {
         "name": "John",
         "age": 20,
         "grade": "A",
         "is_enrolled": True
     }
     print(student["name"])        # Output: "John"
     print(student["age"])         # Output: 20
     print(student["is_enrolled"]) # Output: True
     ```

3. Modifying Dictionary Values:
   * Dictionaries are mutable, so you can update or change their values by specifying the key.
   * Assign a new value to the key using the square bracket notation `[]`.
   * Example:
     ```python
     student = {
         "name": "John",
         "age": 20,
         "grade": "A",
         "is_enrolled": True
     }
     student["grade"] = "B"
     print(student)  # Output: {"name": "John", "age": 20, "grade": "B", "is_enrolled": True}
     ```

4. Iterating over a Dictionary:
   * You can iterate over a dictionary using a `for` loop to access its keys, values, or both.
   * Use the `.keys()`, `.values()`, or `.items()` methods respectively.
   * Example:
     ```python
     student = {
         "name": "John",
         "age": 20,
         "grade": "A",
         "is_enrolled": True
     }
     
     # Iterate over keys
     for key in student.keys():
         print(key)
     
     # Iterate over values
     for value in student.values():
         print(value)
     
     # Iterate over key-value pairs
     for key, value in student.items():
         print(key, ":", value)
     ```

The examples above demonstrate the process of creating dictionaries, accessing their values using keys, modifying values, and iterating over dictionaries to access keys, values, or key-value pairs. Dictionaries in Python provide a powerful way to store and manage data using key-value associations.
<span style="color:green"><em>Unclassified</em></span>