# Spring Test Writer

One fine Saturday evening as I was eating my Mee Hoon Kuay at Old Airport Road Food Centre, I randomly recalled the 1195 lines of uncovered test cases for which I had to write test cases for in my current sprint.

Then, a brilliant idea came to mind (if I say so myself, lol).

Write a script to scan for java classes and generate test files and methods. A bonus if the automatically generated test cases could run and provide 100% coverage without any correction.

## How To Run

Virtualenv

```shell
$ virtualenv env
$ source env/bin/activate
```

Pip

```shell
$ pip install -r requirements.txt
```

Run

```shell
$ python generate.py --src /home/userid/projects/helloworld/src
```

## Components

1. FileScanner: Scans for `.java` files from a given directory
1. ClassFileParser: Parses `.java` file content into a `ClassFile` Object
1. TestFileGenerator: Generates test file in `.java` format from a `ClassFile` object

## FileScanner

Recursively scan for `.java` files from a given root directory and return the list of class files.

## ClassFileParser

Reads and parses the content of a class file into a `ClassFile` object.

1. Read content of `.java` file
1. Identify package
1. Identify class name
1. Scan for member variables
1. Scan for methods

### Identify package

1. `package` code must be the first non-empty line in content
1. Line begins with the keyword `package`, followed by the package path and ends with a semicolon

### Identify class name

Find the first line that follows the syntax:

```java
[<access_modifier> ][<other_keywords> ]class <class_name> {
```

e.g.

```java
public class HelloWorld {
public abstract class Hello {
public interface HelloInterface {
public class HelloWorld extends Hello {
public class HelloWorld implements HelloInterface {
public class HelloWorld extends Hello implements HelloInterface {
public static class HelloWorld<Hello, World> {
```

Extraction steps:

1. Replace string `, ` with `,`
1. Split string by consecutive spaces into a list
1. The element after the ```class``` element should be the __class name__

Additional Notes:

- If the class is an `abstract` class or an `interface`, then the test file cannot be generated since it cannot be instantiated.

### Scan for member variables

Member variables generally follow the syntax:

```java
[<access_modifier> ][<other_keywords> ]<data_type> <variable_name>[ = <RHS>];
```

e.g.

```java
Object object;
int i = 0;
private String name;
protected Map<String, Object> map = new HashMap<>();
public static final int JANUARY = 1;
```

Extraction steps:

1. Replace string `, ` with `,`
1. Split string by consecutive spaces into a list
1. Remove keywords from list: `public`, `private`, `protected`, `static`, `final`
1. First element should be the __data type__
1. Second element should be the __variable name__. Trim trailing `;` from __variable name__

### Scan for methods

Methods generally follow the syntax:

```java
[<access_modifier> ][<other_keywords> ]<return_data_type> <method_name>([<parameters>])[;|( {)]
```

e.g.

```java
void getName()
protected Person getByName(String firstName, String lastName) throws Exception
public abstract void getAddress();
private final int getDays()
public static final Map<String, Object> setName(String name)
```

Extraction steps:

1. Replace string `, ` with `,`
1. Split string by consecutive spaces into a list
1. Remove keywords from list: `public`, `private`, `protected`, `static`, `abstract`
1. First element should be the __return_data_type__
1. Split second element by the first `(`
    1. First element should be the __method_name__
    1. Trim second element by trailing `)`
        1. Split remaining line by `,`

Additional Notes:

- If the method is `abstract`, then the test method cannot be generated since the method cannot be invoked.

## TestFileGenerator

1. Create test file
1. Generate code

### Create test file

TODO

### Generate code

1. Generate package code
1. Generate imports
1. Generate `@RunWith(SpringJUnit4ClassRunner.class)` annotation
1. Generate class
1. Generate member variables
1. Generate test methods
    
### Generate Imports

1. Assert methods
1. Mockito methods and annotations

### Generate Member Variables

1. Declare test class variable
1. If test class has member variables, then:
    - Declare member variables of test class and annotate with ‘@Mock’
    - Annotate test class variable with ‘@InjectMocks’
    - Implement ‘initMocks()’ method and annotate with ‘@Before’

## Generate Test Methods

1. Scan for non-private methods and create a test method
    - e.g. found 'public void getName()', so generate 'public void getNameTest()' method in test file
    - Annotate test method with '@Test'
