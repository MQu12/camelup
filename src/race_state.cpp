#include <vector>
#include <string>
#include <stdlib.h>
#include <bits/stdc++.h>
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
	race_state(5)
{
	set_stack();
	reset_leg();
}
race_state::~race_state(){

	for(camel* c : camel_vec){

		delete c;

	}
	camel_vec.clear();

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
	camel_moved_this_leg.clear();

}

void race_state::set_stack(){

	std::vector<int> positions;

	for(camel* c : camel_vec){

		int camels_on_tile = std::count(positions.begin(), positions.end(), c->position);
		c->stack_position = camels_on_tile;
		positions.push_back	(c->position);

	}

}

int race_state::get_number_of_camel_types(std::string camel_type){

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