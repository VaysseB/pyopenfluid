#
# CMake environment variable for PyOpenFLUID
#
# Author : Bastien VAYSSE <bastien.vaysse@supagro.inra.fr>
#


# =============================================================================
# =============================  NO NEEDS OF DATAS ============================

ADD_TEST(Version_TEST
         ${PYTHON_EXECUTABLE}
         ${CMAKE_CURRENT_SOURCE_DIR}/Version_TEST.py)
SET_TESTS_PROPERTIES(Version_TEST PROPERTIES
                     WILL_FAIL FALSE
                     ENVIRONMENT "PYTHONPATH=${PY_DIR}")




ADD_TEST(BeginPeriodDate_TEST
         ${PYTHON_EXECUTABLE}
         ${CMAKE_CURRENT_SOURCE_DIR}/BeginPeriodDate_TEST.py)
SET_TESTS_PROPERTIES(BeginPeriodDate_TEST PROPERTIES
                     WILL_FAIL FALSE
                     ENVIRONMENT "PYTHONPATH=${PY_DIR}")




ADD_TEST(EndPeriodDate_TEST
         ${PYTHON_EXECUTABLE}
         ${CMAKE_CURRENT_SOURCE_DIR}/EndPeriodDate_TEST.py)
SET_TESTS_PROPERTIES(EndPeriodDate_TEST PROPERTIES
                     WILL_FAIL FALSE
                     ENVIRONMENT "PYTHONPATH=${PY_DIR}")




ADD_TEST(DefaultDeltaT_TEST
         ${PYTHON_EXECUTABLE}
         ${CMAKE_CURRENT_SOURCE_DIR}/DefaultDeltaT_TEST.py)
SET_TESTS_PROPERTIES(DefaultDeltaT_TEST PROPERTIES
                     WILL_FAIL FALSE
                     ENVIRONMENT "PYTHONPATH=${PY_DIR}")




ADD_TEST(ExtraFunctionsPaths_TEST
         ${PYTHON_EXECUTABLE}
         ${CMAKE_CURRENT_SOURCE_DIR}/ExtraFunctionsPaths_TEST.py)
SET_TESTS_PROPERTIES(ExtraFunctionsPaths_TEST PROPERTIES
                     WILL_FAIL FALSE
                     ENVIRONMENT "PYTHONPATH=${PY_DIR}")




ADD_TEST(ExtraObserversPaths_TEST
         ${PYTHON_EXECUTABLE}
         ${CMAKE_CURRENT_SOURCE_DIR}/ExtraObserversPaths_TEST.py)
SET_TESTS_PROPERTIES(ExtraObserversPaths_TEST PROPERTIES
                     WILL_FAIL FALSE
                     ENVIRONMENT "PYTHONPATH=${PY_DIR}")




ADD_TEST(ModelGlobalParameter_TEST
         ${PYTHON_EXECUTABLE}
         ${CMAKE_CURRENT_SOURCE_DIR}/ModelGlobalParameter_TEST.py)
SET_TESTS_PROPERTIES(ModelGlobalParameter_TEST PROPERTIES
                     WILL_FAIL FALSE
                     ENVIRONMENT "PYTHONPATH=${PY_DIR}")




ADD_TEST(OutputDir_TEST
         ${PYTHON_EXECUTABLE}
         ${CMAKE_CURRENT_SOURCE_DIR}/OutputDir_TEST.py)
SET_TESTS_PROPERTIES(OutputDir_TEST PROPERTIES
                     WILL_FAIL FALSE
                     ENVIRONMENT "PYTHONPATH=${PY_DIR}")




ADD_TEST(PrintSimulationInfo_TEST
         ${PYTHON_EXECUTABLE}
         ${CMAKE_CURRENT_SOURCE_DIR}/PrintSimulationInfo_TEST.py)
SET_TESTS_PROPERTIES(PrintSimulationInfo_TEST PROPERTIES
                     WILL_FAIL FALSE
                     ENVIRONMENT "PYTHONPATH=${PY_DIR}")




ADD_TEST(Observer_TEST
         "${PYTHON_EXECUTABLE}"
         "${CMAKE_CURRENT_SOURCE_DIR}/Observer_TEST.py")
SET_TESTS_PROPERTIES(Observer_TEST PROPERTIES
                     WILL_FAIL FALSE
                     ENVIRONMENT "PYTHONPATH=${PY_DIR}")




ADD_TEST(ObserverParameter_TEST
         "${PYTHON_EXECUTABLE}"
         "${CMAKE_CURRENT_SOURCE_DIR}/ObserverParameter_TEST.py")
SET_TESTS_PROPERTIES(ObserverParameter_TEST PROPERTIES
                     WILL_FAIL FALSE
                     ENVIRONMENT "PYTHONPATH=${PY_DIR}")




ADD_TEST(Functions_TEST
         "${PYTHON_EXECUTABLE}"
         "${CMAKE_CURRENT_SOURCE_DIR}/Functions_TEST.py")
SET_TESTS_PROPERTIES(Functions_TEST PROPERTIES
                     WILL_FAIL FALSE
                     ENVIRONMENT "PYTHONPATH=${PY_DIR}")




ADD_TEST(FunctionsParameter_TEST
         "${PYTHON_EXECUTABLE}"
         "${CMAKE_CURRENT_SOURCE_DIR}/FunctionsParameter_TEST.py")
SET_TESTS_PROPERTIES(FunctionsParameter_TEST PROPERTIES
                     WILL_FAIL FALSE
                     ENVIRONMENT "PYTHONPATH=${PY_DIR}")




ADD_TEST(Units_TEST
         "${PYTHON_EXECUTABLE}"
         "${CMAKE_CURRENT_SOURCE_DIR}/Units_TEST.py")
SET_TESTS_PROPERTIES(Units_TEST PROPERTIES
                     WILL_FAIL FALSE
                     ENVIRONMENT "PYTHONPATH=${PY_DIR}")




ADD_TEST(UnitsParentsChildren_TEST
         "${PYTHON_EXECUTABLE}"
         "${CMAKE_CURRENT_SOURCE_DIR}/UnitsParentsChildren_TEST.py")
SET_TESTS_PROPERTIES(UnitsParentsChildren_TEST PROPERTIES
                     WILL_FAIL FALSE
                     ENVIRONMENT "PYTHONPATH=${PY_DIR}")




ADD_TEST(UnitsFromsTos_TEST
         "${PYTHON_EXECUTABLE}"
         "${CMAKE_CURRENT_SOURCE_DIR}/UnitsFromsTos_TEST.py")
SET_TESTS_PROPERTIES(UnitsFromsTos_TEST PROPERTIES
                     WILL_FAIL FALSE
                     ENVIRONMENT "PYTHONPATH=${PY_DIR}")




ADD_TEST(InputData_TEST
         "${PYTHON_EXECUTABLE}"
         "${CMAKE_CURRENT_SOURCE_DIR}/InputData_TEST.py")
SET_TESTS_PROPERTIES(InputData_TEST PROPERTIES
                     WILL_FAIL FALSE
                     ENVIRONMENT "PYTHONPATH=${PY_DIR}")




ADD_TEST(UnitsIDsClasses_TEST
         "${PYTHON_EXECUTABLE}"
         "${CMAKE_CURRENT_SOURCE_DIR}/UnitsIDsClasses_TEST.py")
SET_TESTS_PROPERTIES(UnitsIDsClasses_TEST PROPERTIES
                     WILL_FAIL FALSE
                     ENVIRONMENT "PYTHONPATH=${PY_DIR}")




SET(DATASETTEST_NAME "cmd_dataset")
FILE(MAKE_DIRECTORY "${TEST_PATH}/${DATASETTEST_NAME}")
ADD_TEST(Dataset_TEST
         "${PYTHON_EXECUTABLE}"
         "${CMAKE_CURRENT_SOURCE_DIR}/Dataset_TEST.py"
         "--dataset" "${TEST_PATH}/${DATASETTEST_NAME}/IN")
SET_TESTS_PROPERTIES(Dataset_TEST PROPERTIES
                     WILL_FAIL FALSE
                     ENVIRONMENT "PYTHONPATH=${PY_DIR}")




SET(PROJECTTEST_NAME "cmd_project")
ADD_TEST(Project_TEST
         "${PYTHON_EXECUTABLE}"
         "${CMAKE_CURRENT_SOURCE_DIR}/Project_TEST.py"
         "--project" "${TEST_PATH}/${PROJECTTEST_NAME}")
SET_TESTS_PROPERTIES(Project_TEST PROPERTIES
                     WILL_FAIL FALSE
                     ENVIRONMENT "PYTHONPATH=${PY_DIR}")



# =============================================================================
# =========================  NEEDS DATASET OR PROJECT =========================

ADD_TEST(GeneratorParameter_TEST
         "${PYTHON_EXECUTABLE}"
         "${CMAKE_CURRENT_SOURCE_DIR}/GeneratorParameter_TEST.py"
         "--dataset" "${TEST_PATH}/${PROJECT_NAME_1}/IN")
SET_TESTS_PROPERTIES(GeneratorParameter_TEST PROPERTIES
                     WILL_FAIL FALSE
                     ENVIRONMENT "PYTHONPATH=${PY_DIR}")




ADD_TEST(ModelItems_TEST
         "${PYTHON_EXECUTABLE}"
         "${CMAKE_CURRENT_SOURCE_DIR}/ModelItems_TEST.py"
         "--dataset" "${TEST_PATH}/${PROJECT_NAME_1}/IN")
SET_TESTS_PROPERTIES(ModelItems_TEST PROPERTIES
                     WILL_FAIL FALSE
                     ENVIRONMENT "PYTHONPATH=${PY_DIR}")




ADD_TEST(RunProject_TEST
         "${PYTHON_EXECUTABLE}"
         "${CMAKE_CURRENT_SOURCE_DIR}/RunProject_TEST.py"
         "--project" "${TEST_PATH}/${RUNPROJECT_NAME}")
SET_TESTS_PROPERTIES(RunProject_TEST PROPERTIES
                     DEPENDS RunSimulation_TEST
                     WILL_FAIL FALSE
                     ENVIRONMENT "PYTHONPATH=${PY_DIR}")




ADD_TEST(RunSimulation_TEST
         "${PYTHON_EXECUTABLE}"
         "${CMAKE_CURRENT_SOURCE_DIR}/RunSimulation_TEST.py"
         "--project" "${TEST_PATH}/${RUNSIMULATION_NAME}")
SET_TESTS_PROPERTIES(RunSimulation_TEST PROPERTIES
                     WILL_FAIL FALSE
                     ENVIRONMENT "PYTHONPATH=${PY_DIR}")
