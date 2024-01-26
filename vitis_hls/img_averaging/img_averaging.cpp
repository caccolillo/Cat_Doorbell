// Includes
#include <stdint.h>
#include <hls_stream.h>
#include "img_averaging.h"

#define DATA_SIZE 921600

// TRIPCOUNT identifier
const int c_size = DATA_SIZE;

static void load_input(uint32_t* in, hls::stream<uint32_t>& inStream, int size) {
mem_rd:
    for (int i = 0; i < size; i++) {
		#pragma HLS LOOP_TRIPCOUNT max=4096 min=4096
        inStream << in[i];
    }
}

static void img_averaging(hls::stream<uint32_t>& in1_stream,
                        hls::stream<uint32_t>& in2_stream,
                        hls::stream<uint32_t>& out_stream,
						int scale_by_4,
                        int size) {
    int sum;
    int out_val;

    // The kernel is operating with vector of NUM_WORDS integers. The + operator performs
    // an element-wise add, resulting in NUM_WORDS parallel additions.
    execute:
    for (int i = 0; i < size; i++) {
		#pragma HLS LOOP_TRIPCOUNT max=4096 min=4096
    	sum = (in1_stream.read() + in2_stream.read());
        out_val = scale_by_4 ? sum/4 : sum;
    	out_stream << out_val;
    }
}


static void store_result(uint32_t* out, hls::stream<uint32_t>& out_stream, int size) {
mem_wr:
    for (int i = 0; i < size; i++) {
		#pragma HLS LOOP_TRIPCOUNT max=4096 min=4096
    	out[i] = out_stream.read();
    }
}

extern "C" {

	/*
		Vector Addition Kernel

		Arguments:
			in1  (input)  		--> Input vector 1
			in2  (input)  		--> Input vector 2
			out  (output) 		--> Output vector
			scale_by_4 (input)  --> When 1, scale output by 4
			size (input)  		--> Number of elements in vector
	*/

	void krnl_img_averaging(uint32_t* in1, uint32_t* in2, uint32_t* out, int scale_by_4, int size) {
		#pragma HLS INTERFACE m_axi port = in1 bundle = gmem0
		#pragma HLS INTERFACE m_axi port = in2 bundle = gmem1
		#pragma HLS INTERFACE m_axi port = out bundle = gmem0

		static hls::stream<uint32_t> in1_stream("input_stream_1");
		static hls::stream<uint32_t> in2_stream("input_stream_2");
		static hls::stream<uint32_t> out_stream("output_stream");

		#pragma HLS dataflow
		// dataflow pragma instruct compiler to run following three APIs in parallel
		load_input(in1, in1_stream, size);
		load_input(in2, in2_stream, size);
		img_averaging(in1_stream, in2_stream, out_stream, scale_by_4, size);
		store_result(out, out_stream, size);
	}
}



