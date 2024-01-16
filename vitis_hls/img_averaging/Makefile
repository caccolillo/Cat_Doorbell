clean :
	rm -f *.log
	rm -f *.zip
	rm -f ./python_utils/*.txt
	rm -r ./img_averaging_prj

build : 
	python3 ./python_utils/create_data.py
	./prj.sh

gui : 
	$(shell /home/caccolillo/Documents/Xilinx/Vitis_HLS/2022.2/bin/vitis_hls)