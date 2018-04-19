sol.png : Grafica.py step.txt gauss.txt
	python3 Grafica.py
step.txt : step
	./step>step.txt
step :EcuaciondeOnda.cpp
	c++ EcuaciondeOnda.cpp -o step
step.txt : gauss
	./gauss>gauss.txt
gauss :Gaussiana.cpp
	c++ Gaussiana.cpp -o gauss


