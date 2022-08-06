cmake_minimum_required(VERSION 3.0)

# Settings:
set(CTEST_DASHBOARD_ROOT                "/home/srijan/face_recognition/cmake-3.2.2/Tests/CTestTest")
set(CTEST_SITE                          "LAPTOP-VARR4O69")
set(CTEST_BUILD_NAME                    "CTestTest-Linux-g++-Depends")

set(CTEST_SOURCE_DIRECTORY              "/home/srijan/face_recognition/cmake-3.2.2/Tests/CTestTestBadGenerator")
set(CTEST_BINARY_DIRECTORY              "/home/srijan/face_recognition/cmake-3.2.2/Tests/CTestTestBadGenerator")
set(CTEST_CVS_COMMAND                   "CVSCOMMAND-NOTFOUND")
set(CTEST_CMAKE_GENERATOR               "Bad Generator")
set(CTEST_CMAKE_GENERATOR_PLATFORM      "")
set(CTEST_CMAKE_GENERATOR_TOOLSET       "")
set(CTEST_BUILD_CONFIGURATION           "$ENV{CMAKE_CONFIG_TYPE}")
set(CTEST_COVERAGE_COMMAND              "/usr/bin/gcov")
set(CTEST_NOTES_FILES                   "${CTEST_SCRIPT_DIRECTORY}/${CTEST_SCRIPT_NAME}")

CTEST_START(Experimental)
CTEST_CONFIGURE(BUILD "${CTEST_BINARY_DIRECTORY}" RETURN_VALUE res)
CTEST_BUILD(BUILD "${CTEST_BINARY_DIRECTORY}" RETURN_VALUE res)
CTEST_TEST(BUILD "${CTEST_BINARY_DIRECTORY}" RETURN_VALUE res)
