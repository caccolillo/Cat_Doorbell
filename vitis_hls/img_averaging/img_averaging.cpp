

extern "C" {
	void img_averaging(
	        const unsigned int *in1, // Read-Only Vector 1
	        const unsigned int *in2, // Read-Only Vector 2
	        unsigned int *out,       // Output Result
	        int scale_by_4,          //when 1, scale output by 4
	        int size                 // Size in integer
	        )
	{
#pragma HLS INTERFACE m_axi port=in1 bundle=aximm1
#pragma HLS INTERFACE m_axi port=in2 bundle=aximm2
#pragma HLS INTERFACE m_axi port=out bundle=aximm1
           int sum;
	    for(int i = 0; i < size; ++i)
	    {
	        sum = in1[i] + in2[i];
	        scale_by_4 ? sum/4 : sum;
	    }
	}
}
