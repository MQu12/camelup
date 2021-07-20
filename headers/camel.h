
struct camel{

	int id;
	int position;
	int stack_position = 0;
	int total_movement = 0;

	camel(int _id, int _position, int _stack_position=0, int _total_movement=0);
	virtual int direction() = 0;

};