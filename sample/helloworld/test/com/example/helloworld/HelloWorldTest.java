package com.example.helloworld;

@RunWith(SpringJUnit4ClassRuner.class)
public class HelloWorldTest {

    @InjectMocks
    HelloWorld helloWorld;

    @Mock
    HelloWorldService helloWorldService;

    @Before
    public void initMocks() {
        Mockito.initAnnotations(this);
    }

    @Test
    public void getNameByIdTest() throws CacheException {
        helloWorld.getById("id");
    }

}