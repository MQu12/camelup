#include <vector>
#include "camel.h"
#include "racing_camel.h"
#include "crazy_camel.h"
#include <iostream>

std::vector<camel*> create_camel_vector(){

	std::vector<camel*> camel_vector;
	camel_vector.push_back(new racing_camel(0,0));
	camel_vector.push_back(new crazy_camel(0,0));

	return camel_vector;

}
void print_camel_vec(std::vector<camel*> camel_vector){

	std::cout<<"Let's see those camels then"<<std::endl;

	for(auto camel : camel_vector){

		if(camel->direction()==1)
			std::cout<<"Racing camel ";
		else if(camel->direction()==-1)
			std::cout<<"Crazy camel ";
		else
			std::cout<<"Unidentified camel";
		std::cout<<camel->id<<", dir: "<<camel->direction()<<std::endl;

	}

}

int main(){

	std::vector<camel*> camel_vector = create_camel_vector();

	print_camel_vec(camel_vector);

	return 0;
}