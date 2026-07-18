cmake_minimum_required(VERSION 3.20)
project(leetcode CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

option(ENABLE_CLANG_TIDY "Run clang-tidy as part of the build" OFF)
if(ENABLE_CLANG_TIDY)
    find_program(CLANG_TIDY_EXE clang-tidy REQUIRED)
    message(STATUS "clang-tidy enabled: ${CLANG_TIDY_EXE}")
endif()

include(FetchContent)
FetchContent_Declare(
    Catch2
    GIT_REPOSITORY  https://github.com/catchorg/Catch2.git
    GIT_TAG         v3.5.4
)
FetchContent_MakeAvailable(Catch2)

enable_testing()

file(GLOB TEST_SOURCES CONFIGURE_DEPENDS ${CMAKE_CURRENT_SOURCE_DIR}/tests/*_test.cpp)

if(NOT TEST_SOURCES)
    message(WARNING "No tests found in ${CMAKE_CURRENT_SOURCE_DIR}/tests")
endif()

foreach(test_src ${TEST_SOURCES})
    get_filename_component(file_name ${test_src} NAME_WE)
    string(REPLACE "_test" "" problem_name ${file_name})

    add_executable(${problem_name} ${test_src})
    target_link_libraries(${problem_name} PRIVATE Catch2::Catch2WithMain)
    target_include_directories(${problem_name} PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/solutions)

    if(MSVC)
        target_compile_options(${problem_name} PRIVATE /W4)
    else()
        target_compile_options(${problem_name} PRIVATE -Wall -Wextra)
    endif()

    add_test(NAME ${problem_name} COMMAND ${problem_name})


    if(ENABLE_CLANG_TIDY)
        set_target_properties(${problem_name} PROPERTIES CXX_CLANG_TIDY "${CLANG_TIDY_EXE}")
    endif()
endforeach()
