#ifndef CRAZY_CAMEL
#define CRAZY_CAMEL

#include <string>
#include <iostream>
#include "camel.h"

struct crazy_camel: public camel{

public:
	crazy_camel(int _id, int _position, int _stack_position=0, int _total_movement=0):camel(_id,_position,_stack_position,_total_movement){

	}
	~crazy_camel(){
		
	}
	int direction();
	std::string camel_type() const;

};

#endif