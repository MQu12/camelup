#ifndef RACE_STATE
#define RACE_STATE

#include <vector>
#include <string>
#include "camel.h"

class race_state{

private:
	bool game_end = false;
	int track_length = 16;
	int leg_length = 5;
	int min_roll = 1;
	int max_roll = 3;
	int n_crazy_dice = 1;
	int leg_num = 0;
	int num_moves = 0;
	std::vector<camel*> camel_vec;
	std::vector<int> leg_winners;
	std::vector<int> camel_moved_this_leg;
	std::vector<int> camels_to_move;

	int n_racing_camels;
	int n_crazy_camels;

	void set_stack();

public:
	race_state();
	~race_state();
	race_state(int n_racing_camels, int n_crazy_camels, int n_crazy_dice, int track_length=16,int leg_length=5,int min_roll=1,int max_roll=3);
	race_state(std::vector<camel*> camel_vec);

	void reset_leg();
	int get_number_of_camel_types(std::string camel_type);
	void move_camel_to(int camel_no, int final_pos);
	int pick_crazy_camel();
	int get_leader();
	int get_last_place();
	std::string print_wrap();

	bool get_game_end() const{return game_end;}
	int get_n_crazy_camels() const{return n_crazy_camels;}
	int get_n_racing_camels() const{return n_racing_camels;}
	int get_n_crazy_dice() const{return n_crazy_dice;}
	std::vector<int> get_camels_to_move() const{return camels_to_move;}	

	friend std::ostream& operator<<(std::ostream& os, const race_state& r);

};

#endif