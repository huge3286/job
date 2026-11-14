cmake_minimum_required(VERSION 3.16)
project(HelloWorldProject LANGUAGES CXX)

add_executable(HelloWorld main.cpp hello.cpp)
target_compile_features(HelloWorld PRIVATE cxx_std_11)
