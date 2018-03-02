cmake_minimum_required(VERSION 3.5)

project(mylib CXX)

add_library(mylib STATIC lib.cpp)

target_compile_options(mylib PUBLIC -std=c++11 -w -Wall)


