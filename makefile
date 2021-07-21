
HEADERS = ./headers

test_classes.exe: test_classes.cpp camel.o racing_camel.o
	x86_64-w64-mingw32-g++ -I$(HEADERS) -static-libgcc -static-libstdc++ test_classes.cpp -o test_classes.exe camel.o racing_camel.o
library.dll: camel.o racing_camel.o
	x86_64-w64-mingw32-g++ -shared -Wl,--export-all-symbols camel.o -static-libgcc -static-libstdc++ -o library.dll
racing_camel.o: src/racing_camel.cpp
	x86_64-w64-mingw32-g++ -shared -I$(HEADERS) -fPIC -c -static-libgcc -static-libstdc++ src/racing_camel.cpp
camel.o: src/camel.cpp
	x86_64-w64-mingw32-g++ -shared -I$(HEADERS) -fPIC -c -static-libgcc -static-libstdc++ src/camel.cpp