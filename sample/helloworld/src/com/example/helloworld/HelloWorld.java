package com.example.helloworld;

@Component
public class HelloWorld {

    HelloWorldService helloWorldService;

    private String name;

    public String getName() {
        return name;
    }

    public String getNameById(String id) throws CacheException {
        return helloWorldService.get(id);
    }

}