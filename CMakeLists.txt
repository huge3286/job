cmake_minimum_required(VERSION 3.16)
project(JobPractice LANGUAGES CXX)

include(CTest)
add_subdirectory(cpp/hello)
add_subdirectory(cpp/group_assignment)

if(BUILD_TESTING)
    add_subdirectory(cpp/sort)
endif()
