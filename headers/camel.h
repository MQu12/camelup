#ifndef CAMEL
#define CAMEL

#include<string>
#include<iostream>

struct camel{

	int id;
	int position;
	int stack_position = 0;
	int total_movement = 0;

	camel(int _id, int _position, int _stack_position=0, int _total_movement=0);
	~camel(){}
	virtual int direction() = 0;
	virtual std::string camel_type() const = 0;
	std::string print_wrap();

	friend std::ostream& operator<<(std::ostream& os, const camel& c);

};

#endif