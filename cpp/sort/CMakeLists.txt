cmake_minimum_required(VERSION 3.16)
project(SortAlgorithmTest LANGUAGES CXX)

enable_testing()
find_package(GTest REQUIRED)

add_executable(SortAlgorithmTest main.cc sort.cc)
target_compile_features(SortAlgorithmTest PRIVATE cxx_std_17)
target_compile_options(SortAlgorithmTest PRIVATE $<$<CXX_COMPILER_ID:MSVC>:/utf-8>)
target_link_libraries(SortAlgorithmTest PRIVATE GTest::gtest_main)

include(GoogleTest)
gtest_discover_tests(SortAlgorithmTest)
