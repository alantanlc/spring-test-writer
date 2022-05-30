# Spring Test Writer

One fine Saturday evening as I was eating my Mee Hoon Kuay at Old Airport Road Food Centre, I randomly recalled the 1195 lines of uncovered test cases for which I had to write test cases for in my current sprint.

Then, a brilliant idea came to mind (if I say so myself, lol).

Write a script to scan for java classes and generate test files and methods. A bonus if the automatically generated test cases could run and provide 100% covereage without any correction.

## How To Run

Virtualenv

```
$ virtualenv env
$ source env/bin/activate
```

Pip

```
$ pip install -r requirements.txt
```

Run

```
$ python generate.py --src /home/userid/projects/helloworld/src
```

## Components

1. FileScanner: Scans for `.java` files from a given directory
1. ClassFileParser: Parses `.java` file content into a `ClassFile` Object
1. TestFileGenerator: Generates test file from a `ClassFile` object

## FileScanner

Scan for `.java` files from a given directory

## ClassFileParser

1. Load content of `.java` file
1. Identify package
1. Identify class name
1. Scan for member variables
1. Scan for methods

### Identify package

1. `package` code must be the first non-empty line in content
1. line begins with the keyword `package`, followed by the package path and ends with a semicolon

### Identify class name

TODO

### Scan for member variables

TODO

### Scan for methods

TODO

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
