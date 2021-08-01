#include <vector>
#include <string>
#include <stdlib.h>
#include <bits/stdc++.h>
#include <stdexcept>
#include <algorithm>
#include "race_state.h"
#include "camel.h"
#include "racing_camel.h"
#include "crazy_camel.h"

race_state::race_state(int n_racing_camels, int n_crazy_camels, int n_crazy_dice, int track_length,int leg_length,int min_roll,int max_roll) :
	n_racing_camels(n_racing_camels),
	n_crazy_dice(n_crazy_dice),
	track_length(track_length),
	leg_length(leg_length),
	min_roll(min_roll),
	max_roll(max_roll)
{
	for(int i=0; i<n_racing_camels; i++){
		int start_pos = rand()%3 + 1;
		camel_vec.push_back(
			new racing_camel(i,start_pos)
		);
	}
	for(int i=0; i<n_crazy_camels; i++){
		int start_pos = rand()%3 + 1;
		camel_vec.push_back(
			new crazy_camel(i,track_length-start_pos)
		);
	}

	set_stack();
	reset_leg();

}
race_state::race_state(std::vector<camel*> camel_vec): camel_vec(camel_vec){
	
	n_racing_camels = get_number_of_camel_types("racing");
	n_crazy_camels = get_number_of_camel_types("crazy");

	set_stack();
	reset_leg();

}
race_state::race_state():
	race_state(5,2,1){}
race_state::race_state(const race_state &r){

	//deep copy camel list
	for(camel* c : r.camel_vec){
		camel_vec.push_back( c->copy() );
	}

	game_end = r.game_end;
	track_length = r.track_length;
	leg_length = r.leg_length;
	min_roll = r.min_roll;
	max_roll = r.max_roll;
	n_crazy_dice = r.n_crazy_dice;
	leg_num = r.leg_num;
	num_moves = r.num_moves;
	n_racing_camels = r.n_racing_camels;
	n_crazy_camels = r.n_crazy_camels;

	leg_winners = std::vector<int>(r.leg_winners);
	camels_moved_this_leg = std::vector<int>(r.camels_moved_this_leg);
	camels_to_move = std::vector<int>(r.camels_to_move);

}
race_state::~race_state(){

	for(camel* c : camel_vec){

		delete c;

	}
	camel_vec.clear();

}
race_state race_state::deepcopy() const{

	return race_state(*this);

}

void race_state::reset_leg(){

	if (leg_num > 0){
		leg_winners.push_back(get_leader());
	}
	
	for(int i=0; i<n_racing_camels; i++){
		camels_to_move.push_back(i);
	}
	for(int i=0; i<n_crazy_dice; i++){
		camels_to_move.push_back(-1);
	}
	leg_num++;
	camels_moved_this_leg.clear();

}

void race_state::set_stack(){

	std::vector<int> positions;

	for(camel* c : camel_vec){

		int camels_on_tile = std::count(positions.begin(), positions.end(), c->position);
		c->stack_position = camels_on_tile;
		positions.push_back	(c->position);

	}

}

int race_state::get_number_of_camel_types(std::string camel_type) const{

	int count = 0;
	for(camel* c : camel_vec){
		if(c->camel_type()==camel_type)
			count++;
	}

	return count;

}

void race_state::move_camel_to(int camel_no, int final_pos){

	int target_camel_stack_pos = camel_vec[camel_no]->stack_position;
	int init_camel_pos = camel_vec[camel_no]->position;

	std::vector<int> camels_in_stack;
	int camels_at_destination = 0;

	camel_vec[camel_no]->total_movement += (final_pos-init_camel_pos);

	for(int i=0; i<camel_vec.size(); i++){

		camel* c = camel_vec[i];

		if(c->position == init_camel_pos && c->stack_position >= target_camel_stack_pos)
			camels_in_stack.push_back(i);

		if(c->position == final_pos)
			camels_at_destination++;

	}

	for(int camel_id : camels_in_stack){
		camel_vec[camel_id]->position = final_pos;
		camel_vec[camel_id]->stack_position += (camels_at_destination - target_camel_stack_pos);
	}

	if(final_pos >= track_length)
		game_end = true;

	num_moves++;

}

int race_state::pick_crazy_camel() const{

	std::vector<crazy_camel*> crazy_camel_vec;

	for(int i=n_racing_camels; i<camel_vec.size(); i++)
		crazy_camel_vec.push_back((crazy_camel*) camel_vec[i]);

	// check if either crazy camel is carrying any racing camels
	std::vector<bool> crazy_camels_carrying;
	for(int i=0; i<n_crazy_camels; i++)
		crazy_camels_carrying.push_back(false);

	for(int i=0; i<n_racing_camels;i++){
		// camels not in a stack cannot be being carried
		if (camel_vec[i]->stack_position == 0)
			continue;
		for(int j=0; j<crazy_camel_vec.size();j++){
			if(crazy_camels_carrying[j])
				continue;
			else if(crazy_camel_vec[j]->position == camel_vec[i]->position && crazy_camel_vec[j]->stack_position + 1 == camel_vec[i]->stack_position)
				crazy_camels_carrying[j] = true;
		}
	}

	int sum_carrying = 0;
	for(bool carrying : crazy_camels_carrying){
		sum_carrying += carrying;
	}
	// if only one is carrying, return it
	if (sum_carrying == 1){
		for(int i=0; i<crazy_camels_carrying.size(); i++){
			if(crazy_camels_carrying[i])
				return i;
		}
		throw std::invalid_argument( "Sum of crazy camels carrying == 1, but can't find camel which carrying." ); 
	}
	// if others exist, pick one at random
	else if(sum_carrying > 1){
		std::vector<int> carrying_camels_id;
		for(int i=0; i<n_crazy_camels; i++){
			crazy_camels_carrying.push_back(i);
		}
		int rand_id = rand()%sum_carrying;
		return carrying_camels_id[rand_id];
	}

	// determine which (if any) crazy camels are directly on top of another
	std::vector<int> crazy_id_carried_by_crazy;
	for(crazy_camel* crazy1 : crazy_camel_vec)
		for(crazy_camel* crazy2 : crazy_camel_vec)
			if(crazy1->position == crazy2->position && crazy1->stack_position == crazy2->stack_position + 1)
				crazy_id_carried_by_crazy.push_back(crazy1->id);

	int n_crazies_carrying_crazies = crazy_id_carried_by_crazy.size();
	// if only one crazy camel sits directly atop another, return it
	if(n_crazies_carrying_crazies == 1)
		return crazy_id_carried_by_crazy[0];
	// if more than once, pick one at random
	else if(n_crazies_carrying_crazies > 1){
		int rand_id = rand()%n_crazies_carrying_crazies;
		return crazy_id_carried_by_crazy[rand_id];
	}

	// otherwise, pick one at random
	int rand_id = rand()%n_crazy_camels;
	return rand_id;

}
int race_state::get_leader() const{

	int largest_forward = 0;
	int largest_upward = 0;
	int leading_camel_id = 0;

	for(camel* c : camel_vec){

		if (c->camel_type() != "racing")
			continue;
		else if(c->position > largest_forward || (c->position == largest_forward && c->stack_position > largest_upward)){
			largest_forward = c->position;
			largest_upward = c->stack_position;
			leading_camel_id = c->id;
		}
		else
			continue;

	}

	return leading_camel_id;
}

int race_state::get_last_place() const{

	int furthest_back = 100000000;
	int lowest_down = 100000000;
	int trailing_camel_id = 0;

	for(camel* c : camel_vec){

		if (c->camel_type() != "racing")
			continue;
		else if(c->position < furthest_back || (c->position == furthest_back && c->stack_position < lowest_down)){
			furthest_back = c->position;
			lowest_down = c->stack_position;
			trailing_camel_id = c->id;
		}
		else
			continue;

	}
	return trailing_camel_id;
}

std::ostream& operator<<(std::ostream& os, const race_state& r){

	os << "State after " << r.num_moves << " moves " << std::endl
	   << "Leg " << r.leg_num << std::endl;

	for(camel* c : r.camel_vec){
		os << *c << std::endl;
	}
	
	return os;

}

void race_state::mark_camel_moved(int camel_no){

	camels_moved_this_leg.push_back(camel_no);
	camels_to_move.erase(std::remove(camels_to_move.begin(), camels_to_move.end(), camel_no), camels_to_move.end());

}