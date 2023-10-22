cmake_minimum_required(VERSION 3.10)
project(SortAlgorithnmTest)
set(CMAKE_CXX_STANDARD 14)

find_package(GTest REQUIRED)

add_executable(SortAlgorithnmTest main.cc sort.cc)

target_link_libraries(SortAlgorithnmTest GTest::gtest)
target_include_directories(SortAlgorithnmTest PUBLIC ${GTest_INCLUDE_DIRS})

enable_testing()
