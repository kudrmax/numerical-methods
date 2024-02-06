cmake_minimum_required(VERSION 3.24)
project(numerical-methods)

set(CMAKE_CXX_STANDARD 17)

file(GLOB_RECURSE my_src machine_values.cpp)
add_executable(${PROJECT_NAME} ${my_src})