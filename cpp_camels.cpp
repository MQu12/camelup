#include <boost/python.hpp>
#include <Python.h>

//modules to export
#include "racing_camel.h"

BOOST_PYTHON_MODULE(cpp_camels)
{
    using namespace boost::python;

    class_<racing_camel>("racing_camel", init<int,int,int,int>())
        .def("direction", &racing_camel::direction)
        .def_readwrite("id", &racing_camel::id)
        .def_readwrite("position", &racing_camel::position)
        .def_readwrite("stack_position", &racing_camel::stack_position)
        .def_readwrite("total_movement", &racing_camel::total_movement);    
}