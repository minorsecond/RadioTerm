cmake_minimum_required(VERSION 3.17)
project(RadioTerm)

set(CMAKE_CXX_STANDARD 20)
set(LIBPROC_SRC "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/libproc.h")

set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTOUIC ON)
set(CMAKE_INCLUDE_CURRENT_DIR ON)

find_package(Qt5 COMPONENTS Core Widgets REQUIRED)
find_package(Boost COMPONENTS filesystem)
#find_package(Catch2 REQUIRED)

set(ICON_NAME "icon.icns")
set(ICON_PATH ${PROJECT_SOURCE_DIR}/res/${ICON_NAME})
set(radioterm_ICON ${ICON_PATH})
set_source_files_properties(${radioterm_ICON} PROPERTIES MACOSX_PACKAGE_LOCATION Resources)
file(COPY ${ICON_PATH} DESTINATION "RadioTerm.app/Contents/Resources")

add_executable(RadioTerm MACOSX_BUNDLE ${ICON_PATH} src/main.cpp src/mainwindow.cpp src/mainwindow.h src/user_settings.cpp src/user_settings.h)

set_target_properties(RadioTerm PROPERTIES MACOSX_BUNDLE_ICONFILE ${ICON_NAME})
target_link_libraries(RadioTerm Qt5::Core Qt5::Widgets SQLite3 Boost::filesystem)

#include(CTest)
#include(Catch)
#catch_discover_tests(functions_test)
#add_test(NAME functions_test COMMAND functions_test)