# Spring Test Writer

One fine Saturday evening as I was eating my Mee Hoon Kuay at Old Airport Road Food Centre, I randomly recalled the 1195 lines of uncovered test cases for which I had to write test cases for in my current sprint.

Then, a brilliant idea came to mind (if I say so myself, lol).

I could come up with a script to generate the test files and test methods to speed up the test writing process.

Even better if the automatically generated test cases could cover 100% lines of the test method without any fault!

And so the 'Spring Test Writer' was born.

## Overview

1. Generate test files and classes
1. Declare variables
1. Generate test methods
1. Implement test methods

## Generate Test Files

Steps:

1. Scan repository in 'src' folder for classes '.java' files
1. Create test file in 'test' folder with the same package path
    - e.g. found 'src/com/example/Hello world.java' so created 'test/com/example/HelloWorldTest.java'
1. Annotate class with '@RunWith(SpringJUnit4ClassRunner.class)'
1. If test file already exists, then skip file creation

## Declare Variables

Steps

1. Generate imports
1. Generate member variables
    
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

Steps:
1. Scan for non-private methods and create a test method
    - e.g. found 'public void getName()', so generate 'public void getNameTest()' method in test file
    - Annotate test method with '@Test'

## Implement Test Methods

Steps:
1. 