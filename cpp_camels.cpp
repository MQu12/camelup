#include <boost/python.hpp>
#include <Python.h>

//items to export
#include "racing_camel.h"
#include "crazy_camel.h"
#include "race_state.h"

template<class T>
struct VecToList
{
    static PyObject* convert(const std::vector<T>& vec)
    {
        boost::python::list* l = new boost::python::list();
        for(size_t i = 0; i < vec.size(); i++) {
            l->append(vec[i]);
        }

        return l->ptr();
    }
};

BOOST_PYTHON_MODULE(cpp_camels)
{
    using namespace boost::python;

    to_python_converter<std::vector<int, std::allocator<int> >, VecToList<int> >();

    class_<racing_camel>("racing_camel", init<int,int,int,int>())
        .def("direction", &racing_camel::direction)
        .def_readwrite("id", &racing_camel::id)
        .def_readwrite("position", &racing_camel::position)
        .def_readwrite("stack_position", &racing_camel::stack_position)
        .def_readwrite("total_movement", &racing_camel::total_movement);

    class_<crazy_camel>("crazy_camel", init<int,int,int,int>())
        .def("direction", &crazy_camel::direction)
        .def_readwrite("id", &crazy_camel::id)
        .def_readwrite("position", &crazy_camel::position)
        .def_readwrite("stack_position", &crazy_camel::stack_position)
        .def_readwrite("total_movement", &crazy_camel::total_movement); 

    class_<race_state>("race_state",init<>())
    	.def("reset_leg", &race_state::reset_leg)
    	.def("get_number_of_camel_types", &race_state::get_number_of_camel_types)
    	.def("move_camel_to",&race_state::move_camel_to)
    	.def("pick_crazy_camel",&race_state::pick_crazy_camel)
    	.def("get_leader",&race_state::get_leader)
    	.def("get_last_place",&race_state::get_last_place)
    	.def("print_wrap",&race_state::print_wrap)
        .def("get_game_end" ,&race_state::get_game_end)
        .def("get_n_crazy_camels",&race_state::get_n_crazy_camels)
        .def("get_n_racing_camels",&race_state::get_n_racing_camels)
        .def("get_n_crazy_dice",&race_state::get_n_crazy_dice)
        .def("get_camels_to_move",&race_state::get_camels_to_move)
        .def(self_ns::str(self));
}