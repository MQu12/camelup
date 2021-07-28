#include "camel.h"
#include <string>
#include <iostream>

camel::camel(int _id, int _position, int _stack_position, int _total_movement){

	this->id = _id;
	this->position = _position;
	this-> stack_position = _stack_position;
	this-> total_movement = _total_movement;

}
std::string camel::print_wrap(){

	std::string output = this->camel_type() + " no " + std::to_string(id) + " at " + std::to_string(position) + ", y = " + std::to_string(stack_position); 
	return output;
	
}

std::ostream& operator<<(std::ostream& os, const camel& c){

	os << c.camel_type() << " no " << c.id << " at " << c.position << ", y = " << c.stack_position; 
	return os;

}