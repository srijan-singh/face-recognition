# CMake generated Testfile for 
# Source directory: /home/srijan/face_recognition/cmake-3.2.2
# Build directory: /home/srijan/face_recognition/cmake-3.2.2
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
include("/home/srijan/face_recognition/cmake-3.2.2/Tests/EnforceConfig.cmake")
add_test(SystemInformationNew "/home/srijan/face_recognition/cmake-3.2.2/bin/cmake" "--system-information" "-G" "Unix Makefiles")
subdirs(Utilities/KWIML)
subdirs(Source/kwsys)
subdirs(Utilities/cmzlib)
subdirs(Utilities/cmcurl)
subdirs(Utilities/cmcompress)
subdirs(Utilities/cmbzip2)
subdirs(Utilities/cmliblzma)
subdirs(Utilities/cmlibarchive)
subdirs(Utilities/cmexpat)
subdirs(Utilities/cmjsoncpp)
subdirs(Source)
subdirs(Utilities)
subdirs(Tests)
subdirs(Auxiliary)
