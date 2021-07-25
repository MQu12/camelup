
PYTHON_VERSION = 3.8
PYTHON_INCLUDE = /usr/include/python$(PYTHON_VERSION)
BOOST_INC = /usr/include
BOOST_LIB = /usr/lib
HEADERS = ./headers

test_classes: test_classes.cpp camel.o racing_camel.o crazy_camel.o race_state.o
	g++ -I$(HEADERS) -static-libgcc -static-libstdc++ test_classes.cpp -o test_classes camel.o racing_camel.o crazy_camel.o
cpp_camels.so: camel.o racing_camel.o cpp_camels.o crazy_camel.o race_state.o
	g++ -shared -W camel.o cpp_camels.o racing_camel.o crazy_camel.o race_state.o -L$(BOOST_LIB) -lboost_python-$(PYTHON_VERSION) -L/usr/lib/python$(PYTHON_VERSION)/config -lpython$(PYTHON_VERSION) -o cpp_camels.so
cpp_camels.o: cpp_camels.cpp
	g++ -I$(PYTHON_INCLUDE) -I$(HEADERS) -I$(BOOST_INC) -fPIC -c cpp_camels.cpp
race_state.o: src/race_state.cpp
	g++ -shared -I$(HEADERS) -fPIC -c -static-libgcc -static-libstdc++ src/race_state.cpp
racing_camel.o: src/racing_camel.cpp
	g++ -shared -I$(HEADERS) -fPIC -c -static-libgcc -static-libstdc++ src/racing_camel.cpp
crazy_camel.o: src/crazy_camel.cpp
	g++ -shared -I$(HEADERS) -fPIC -c -static-libgcc -static-libstdc++ src/crazy_camel.cpp
camel.o: src/camel.cpp
	g++ -shared -I$(HEADERS) -fPIC -c -static-libgcc -static-libstdc++ src/camel.cpp