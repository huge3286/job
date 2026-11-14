add_executable(group_assignment main.cc)
target_compile_features(group_assignment PRIVATE cxx_std_11)
target_compile_options(group_assignment PRIVATE $<$<CXX_COMPILER_ID:MSVC>:/utf-8>)

if(BUILD_TESTING)
    add_test(NAME group_assignment COMMAND group_assignment)
endif()
