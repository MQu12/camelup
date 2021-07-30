#ifndef RACING_CAMEL
#define RACING_CAMEL

#include <string>
#include <iostream>
#include "camel.h"

struct racing_camel: public camel{

public:
	racing_camel(int _id, int _position, int _stack_position=0, int _total_movement=0):camel(_id,_position,_stack_position,_total_movement){}
	racing_camel(const racing_camel& c): camel(c){}
	~racing_camel(){}
	camel* copy() const{
		return new racing_camel(*this);
	}
	int direction();
	std::string camel_type() const;

};

#endif