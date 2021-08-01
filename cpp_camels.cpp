#include <boost/python.hpp>
#include <Python.h>

//items to export
#include "racing_camel.h"
#include "crazy_camel.h"
#include "race_state.h"
#include "camel.h"

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
    to_python_converter<std::vector<camel*, std::allocator<camel*> >, VecToList<camel*> >();
    //to_python_converter<std::vector<racing_camel*, std::allocator<racing_camel*> >, VecToList<racing_camel*> >();

    class_<camel, boost::noncopyable>("camel", no_init);

    class_<racing_camel, bases<camel>>("racing_camel", init<int,int,int,int>())
        .def(init<racing_camel>())
        .def("direction", &racing_camel::direction)
        .def_readwrite("id", &racing_camel::id)
        .def_readwrite("position", &racing_camel::position)
        .def_readwrite("stack_position", &racing_camel::stack_position)
        .def_readwrite("total_movement", &racing_camel::total_movement)
        .def(self_ns::str(self))
        .def(self_ns::repr(self));

    class_<crazy_camel>("crazy_camel", init<int,int,int,int>())
        .def(init<crazy_camel>())
        .def("direction", &crazy_camel::direction)
        .def_readwrite("id", &crazy_camel::id)
        .def_readwrite("position", &crazy_camel::position)
        .def_readwrite("stack_position", &crazy_camel::stack_position)
        .def_readwrite("total_movement", &crazy_camel::total_movement)
        .def(self_ns::str(self))
        .def(self_ns::repr(self));

    class_<race_state>("race_state",init<>())
        .def(init<std::vector<camel*>>())
        .def(init<int,int,int,int,int,int,int>())
        .def(init<race_state>())
        .def("deepcopy",&race_state::deepcopy)
    	.def("reset_leg", &race_state::reset_leg)
    	.def("get_number_of_camel_types", &race_state::get_number_of_camel_types)
    	.def("move_camel_to",&race_state::move_camel_to)
    	.def("pick_crazy_camel",&race_state::pick_crazy_camel)
    	.def("get_leader",&race_state::get_leader)
    	.def("get_last_place",&race_state::get_last_place)
        .def("mark_camel_moved",&race_state::mark_camel_moved)
        .def("get_game_end" ,&race_state::get_game_end)
        .def("get_n_crazy_camels",&race_state::get_n_crazy_camels)
        .def("get_n_racing_camels",&race_state::get_n_racing_camels)
        .def("get_n_crazy_dice",&race_state::get_n_crazy_dice)
        .def("get_leg_length",&race_state::get_leg_length)
        .def("get_min_roll",&race_state::get_min_roll)
        .def("get_max_roll",&race_state::get_max_roll)
        .def("get_leg_num",&race_state::get_leg_num)
        .def("get_num_moves",&race_state::get_num_moves)
        .def("get_track_length",&race_state::get_track_length)
        .def("get_camels_to_move",&race_state::get_camels_to_move)
        .def("get_camels_moved_this_leg",&race_state::get_camels_moved_this_leg)
        .def("get_leg_winners",&race_state::get_leg_winners)
        .def("get_camel_list",&race_state::get_camel_list)
        .def("getCamel",&race_state::getCamel,return_internal_reference<>())
        .def(self_ns::str(self))
        .def(self_ns::repr(self));

    class_<std::vector<camel*> >("PyVec")
         .def(vector_indexing_suite<std::vector<camel*> >())
    ;

    implicitly_convertible<racing_camel*,camel*>();
    //implicitly_convertible<camel,crazy_camel>();
}