cmake_minimum_required(VERSION 3.16)

project(CalculatorApp VERSION 0.1 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(Qt6 REQUIRED COMPONENTS REQUIRED)

qt_add_executable(CalculatorApp
    main.cpp
    # আপনার গিটহাবের অন্য কোনো .cpp বা .h ফাইল থাকলে সেগুলোর নাম এখানে নিচে নিচে লিখে দিন
)

target_link_libraries(CalculatorApp PRIVATE Qt6::Core)
