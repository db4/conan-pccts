project(PackageTest C)
cmake_minimum_required(VERSION 2.8.12)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

set(g_file ${PROJECT_SOURCE_DIR}/calc.g)
file(TO_NATIVE_PATH ${g_file} g_file)

add_custom_command(OUTPUT
                       ${PROJECT_BINARY_DIR}/calc.c
                       ${PROJECT_BINARY_DIR}/err.c
                       ${PROJECT_BINARY_DIR}/parser.dlg
                       ${PROJECT_BINARY_DIR}/tokens.h
                   COMMAND antlr
                   ARGS -o ${PROJECT_BINARY_DIR} ${g_file}
                   MAIN_DEPENDENCY ${g_file})

file(TO_NATIVE_PATH ${PROJECT_BINARY_DIR}/parser.dlg dlg_file)
file(TO_NATIVE_PATH ${PROJECT_BINARY_DIR}/scan.c scan_file)

add_custom_command(OUTPUT
                       ${PROJECT_BINARY_DIR}/scan.c
                       ${PROJECT_BINARY_DIR}/mode.h
                   COMMAND dlg
                   ARGS -i ${dlg_file} ${scan_file}
                   MAIN_DEPENDENCY ${dlg_file})

add_executable(calc
    ${PROJECT_BINARY_DIR}/calc.c
    ${PROJECT_BINARY_DIR}/err.c
    ${PROJECT_BINARY_DIR}/scan.c
)
