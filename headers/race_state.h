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
	std::vector<int> camels_moved_this_leg;
	std::vector<int> camels_to_move;

	int n_racing_camels;
	int n_crazy_camels;

	void set_stack();

public:
	race_state();
	~race_state();
	race_state(int n_racing_camels, int n_crazy_camels, int n_crazy_dice, int track_length=16,int leg_length=5,int min_roll=1,int max_roll=3);
	race_state(std::vector<camel*> camel_vec);
	race_state(const race_state &r);

	race_state deepcopy() const;
	void reset_leg();
	void move_camel_to(int camel_no, int final_pos);
	int pick_crazy_camel() const;
	void mark_camel_moved(int camel_no);

	int get_number_of_camel_types(std::string camel_type) const;
	int get_leader() const;
	int get_last_place() const;

	bool get_game_end() const{return game_end;}
	int get_n_crazy_camels() const{return n_crazy_camels;}
	int get_n_racing_camels() const{return n_racing_camels;}
	int get_n_crazy_dice() const{return n_crazy_dice;}
	int get_leg_length() const{return leg_length;}
	int get_min_roll() const{return min_roll;}
	int get_max_roll() const{return max_roll;}
	int get_leg_num() const{return leg_num;}
	int get_num_moves() const{return num_moves;}
	int get_track_length() const{return track_length;}
	std::vector<int> get_camels_to_move() const{return camels_to_move;}	
	std::vector<int> get_camels_moved_this_leg() const{return camels_moved_this_leg;}
	std::vector<int> get_leg_winners() const{return leg_winners;}
	std::vector<camel*> get_camel_list() const{return camel_vec;}

	friend std::ostream& operator<<(std::ostream& os, const race_state& r);

};

#endif