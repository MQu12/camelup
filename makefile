#all: function.o library.so
#	x86_64-w64-mingw32-g++ -shared -c -fPIC simulate_leg.cpp -static-libgcc -static-libstdc++ -o simulate_leg.o
#	x86_64-w64-mingw32-g++ -shared -static-libgcc -static-libstdc++ -Wl,-soname,library.so -o library.dll simulate_leg.o

# location of the Boost Python include files and library
HEADERS = ./headers
# compile mesh classes
library.dll: camel.o racing_camel.o
	x86_64-w64-mingw32-g++ -shared -Wl,--export-all-symbols camel.o -static-libgcc -static-libstdc++ -o library.dll
camel.o: src/camel.cpp
	x86_64-w64-mingw32-g++ -shared -I$(HEADERS) -fPIC -c -static-libgcc -static-libstdc++ src/camel.cpp
racing_camel.o: src/racing_camel.cpp
	x86_64-w64-mingw32-g++ -shared -I$(HEADERS) -fPIC -c -static-libgcc -static-libstdc++ src/racing_camel.cpp