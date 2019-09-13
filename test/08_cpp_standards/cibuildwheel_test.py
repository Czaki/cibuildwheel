import os
import utils
import sys 

def test_cpp11():
    add_env = {"CIBW_SKIP": "cp27-win* cp34-win*"}
    # VC for python 2.7 do not support modern standards
    if utils.platform == "macos":
        add_env["MACOSX_DEPLOYMENT_TARGET"] = "10.9"
    project_dir = os.path.join(os.path.dirname(__file__), "cpp11")
    # this test checks if c++11 standard is supported.

    utils.cibuildwheel_run(project_dir, add_env=add_env)


def test_cpp14():
    add_env = {"CIBW_SKIP": "cp27-win*  cp35-win* *manylinux1*"}
    # VC for python 2.7 do not support modern standards
    # manylinux1 docker image do not support compilers with standards newer than c++11
    if utils.platform == "macos":
        add_env["MACOSX_DEPLOYMENT_TARGET"] = "10.9"
    project_dir = os.path.join(os.path.dirname(__file__), "cpp14")
    # this test checks if c++14 standard is supported.

    utils.cibuildwheel_run(project_dir, add_env=add_env)

def test_cpp17():
    # python 2.7 use `register` keyword which is forbidden in c++17 standard 
    # manylinux1 docker image do not support compilers with standards newer than c++11
    add_env = {"CIBW_SKIP": "cp27*  cp35-win* *manylinux1*"}
    if utils.platform == "macos":
        add_env["MACOSX_DEPLOYMENT_TARGET"] = "10.13"

    project_dir = os.path.join(os.path.dirname(__file__), "cpp17")
    # this test checks if c++17 standard is supported.

    utils.cibuildwheel_run(project_dir, add_env=add_env)

