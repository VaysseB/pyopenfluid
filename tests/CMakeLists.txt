#
# CMake environment variable for PyOpenFLUID
#
# Author : Bastien VAYSSE <bastien.vaysse@supagro.inra.fr>
#

SET(PY_DIR "${PYTHON_OUTPUT_SRC_PATH}:${CMAKE_CURRENT_SOURCE_DIR}")
SET(TEST_PATH "${TEST_OUTPUT_PATH}")

# macro - create a copy of openfluid projet path
MACRO(CreateOFRepository SOURCE FINALPATH FINALNAME)
  IF(EXISTS "${FINALPATH}/${FINALNAME}" AND IS_DIRECTORY "${FINALPATH}/${FINALNAME}")
    FILE(REMOVE_RECURSE "${FINALPATH}/${FINALNAME}")
  ENDIF(EXISTS "${FINALPATH}/${FINALNAME}" AND IS_DIRECTORY "${FINALPATH}/${FINALNAME}")
  FILE(COPY "${SOURCE}" DESTINATION "${FINALPATH}")
  GET_FILENAME_COMPONENT(SOURCENAME ${SOURCE} NAME CACHE)
  FILE(RENAME "${FINALPATH}/${SOURCENAME}"
       "${FINALPATH}/${FINALNAME}")
  FILE(MAKE_DIRECTORY "${FINALPATH}/${FINALNAME}")
  FILE(MAKE_DIRECTORY "${FINALPATH}/${FINALNAME}/IN")
  FILE(MAKE_DIRECTORY "${FINALPATH}/${FINALNAME}/OUT")
ENDMACRO(CreateOFRepository)

# output projects path
SET(PROJECT_NAME_1        "project_1")
SET(RUNSIMULATION_NAME    "cmd_runsimulation")
SET(RUNPROJECT_NAME       "cmd_runproject")

# input projects path (use read-only)
CreateOFRepository("${OPENFLUID_TESTS_PROJECT_1}" "${TEST_PATH}" "${PROJECT_NAME_1}")
CreateOFRepository("${OPENFLUID_TESTS_PROJECT_1}" "${TEST_PATH}" "${RUNSIMULATION_NAME}")
CreateOFRepository("${OPENFLUID_TESTS_PROJECT_1}" "${TEST_PATH}" "${RUNPROJECT_NAME}")

##
ADD_TEST(TestOfTestUnit
         ${PYTHON_EXECUTABLE}
         "${CMAKE_CURRENT_SOURCE_DIR}/TestOfTestUnit.py")
SET_TESTS_PROPERTIES(TestOfTestUnit PROPERTIES
                     WILL_FAIL TRUE
                     ENVIRONMENT "PYTHONPATH=${PY_DIR}")

#
ADD_SUBDIRECTORY(scripts)
