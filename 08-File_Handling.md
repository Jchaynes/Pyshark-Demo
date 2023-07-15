<span style="color:green"><em>Unclassified</em></span>
File handling refers to the process of working with files in a computer's file system using a programming language. It involves tasks such as reading data from files, writing data to files, and manipulating file contents.

In Python, file handling is achieved through built-in functions and methods provided by the file object. Here's a brief explanation of the basic file handling operations:

1. Opening a File:
   * To work with a file, you need to open it using the `open()` function, which returns a file object.
   * You specify the file's name or path and the mode in which you want to open the file (e.g., read mode, write mode, append mode).
   * Example:
     ```python
     file = open("example.txt", "r")  # Open the file in read mode
     ```

2. Reading from a File:
   * Once a file is opened in read mode, you can read its contents using methods such as `read()`, `readline()`, or `readlines()`.
   * `read()` reads the entire content of the file as a string.
   * `readline()` reads a single line from the file.
   * `readlines()` reads all lines of the file and returns them as a list of strings.
   * Example:
     ```python
     content = file.read()  # Read the entire content of the file
     print(content)
     ```

3. Writing to a File:
   * When a file is opened in write mode, you can write data to it using the `write()` method.
   * If the file doesn't exist, it will be created. If it already exists, its contents will be overwritten.
   * Example:
     ```python
     file = open("example.txt", "w")  # Open the file in write mode
     file.write("Hello, World!")     # Write data to the file
     file.close()                    # Close the file
     ```

4. Appending to a File:
   * Opening a file in append mode allows you to add data to the end of the file without overwriting its existing contents.
   * Example:
     ```python
     file = open("example.txt", "a")  # Open the file in append mode
     file.write("Appended text")      # Append data to the file
     file.close()                     # Close the file
     ```

5. Closing a File:
   * It's important to close the file after you're done working with it using the `close()` method.
   * Closing the file ensures that any changes are saved, and the system resources associated with the file are released.
   * Example:
     ```python
     file.close()  # Close the file
     ```

# Error handling and exceptions
It's important to handle files properly by opening them, performing the required operations, and closing them to ensure efficient and safe file manipulation.

Exceptions and error handling in Python are mechanisms that allow you to handle and respond to runtime errors and exceptional situations that may occur during the execution of a program. When it comes to file access, exceptions can occur if there are issues with opening, reading, or writing to a file. Using context managers is a recommended approach to handle file-related exceptions.


1. Exceptions:
   * Exceptions are objects that represent errors or exceptional conditions that occur during program execution.
   * When an exception occurs, it disrupts the normal flow of the program and raises an error.
   * Examples of file-related exceptions include `FileNotFoundError` (when a file does not exist), `PermissionError` (when there is a permission issue), or `IOError` (general input/output error).
   * Python provides a range of built-in exception types, and you can also create custom exceptions.
   * Exceptions can be caught and handled using try-except blocks.

2. Error Handling with try-except:
   * To handle exceptions, you can use a try-except block.
   * The code that may raise an exception is placed inside the try block, and the except block defines the code to be executed if an exception of the specified type occurs.
   * Multiple except blocks can be used to handle different types of exceptions.
   * Example:
     ```python
     try:
         file = open("example.txt", "r")
         content = file.read()
         print(content)
     except FileNotFoundError:
         print("File not found!")
     except IOError as e:
         print("Error occurred:", str(e))
     finally:
         file.close()  # Ensure the file is closed, even if an exception occurs
     ```

3. Using Context Managers (with statement):
   * Context managers provide a convenient way to manage resources, such as file objects, by automatically handling their opening and closing.
   * The `with` statement is used with context managers, ensuring that the resources are properly managed and automatically closed even if an exception occurs.
   * Example:
     ```python
     try:
         with open("example.txt", "r") as file:
             content = file.read()
             print(content)
     except FileNotFoundError:
         print("File not found!")
     except IOError as e:
         print("Error occurred:", str(e))
     ```

   * In the above example, the file is opened and accessed within the `with` statement. The file object is automatically closed at the end of the block, ensuring proper resource management.

Using context managers with the `with` statement simplifies error handling and ensures that file resources are properly managed. It eliminates the need to manually close the file and provides a cleaner and more concise way to handle file-related exceptions.
<span style="color:green"><em>Unclassified</em></span>s