#include <vector>
#include "camel.h"
#include "racing_camel.h"
#include <iostream>

std::vector<camel*> create_camel_vector(){

	std::vector<camel*> camel_vector;
	camel_vector.push_back(new racing_camel(0,0));

	return camel_vector;

}
void print_camel_vec(std::vector<camel*> camel_vector){

	std::cout<<"Let's see those camels then"<<std::endl;

	for(auto camel : camel_vector){

		std::cout<<"Racing camel "<<camel->id<<", dir: "<<camel->direction()<<std::endl;

	}

}

int main(){

	std::vector<camel*> camel_vector = create_camel_vector();

	print_camel_vec(camel_vector);

	return 0;
}