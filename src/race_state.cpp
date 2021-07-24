#include <vector>
#include <string>
#include <stdlib.h>
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
	max_roll(max_roll),
	n_crazy_dice(n_crazy_dice)
{

	for(int i=0; i<n_racing_camels; i++){
		int start_pos = rand()%3 + 1;
		camel_vec.append(
			new racing_camel(i,start_pos);
		);
	}
	for(int i=0; i<n_crazy_camels; i++){
		int start_pos = rand()%3 + 1;
		camel_vec.append(
			new crazy_camel(i,track_length-start_pos);
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

void race_state::reset_leg(){

	if (leg_num > 0){
		leg_winners.append(get_leader());
	}
	vector<int> camels_to_move;
	for(int i=0; i<n_racing_camels; i++){
		camels_to_move.append(i);
	}
	for(int i=0; i<n_crazy_dice; i++){
		camels_to_move.append(-1);
	}
	leg_num++;
	camel_moved_this_leg.clear();

}

void race_state::set_stack(){

	
}