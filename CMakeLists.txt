cmake_minimum_required(VERSION 3.5)

project(main CXX)


add_subdirectory("./B")

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -Wall")

set(SOURCES_LIST "./C/main.cpp")


add_executable(main ${SOURCES_LIST}) 

add_custom_target(preparing
	WORKING_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}/A"
	COMMAND python3 ./preparing.py)

add_dependencies(main preparing)

target_link_libraries(main mylib)

target_include_directories(main PUBLIC "./")

