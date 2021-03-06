`include "src/defines.v"
`timescale 1ns/100ps

module tb_cosecant;

// -------------------------------------------------------- parameters
localparam T = 2;
integer min1 = `DATA_WIDTH'd0;
integer max1 = `DATA_WIDTH'd90;
integer unsigned num1 = 0;

// -------------------------------------------------------- IO
reg     clk;
reg     reset_n;
reg     en_cosecant;
reg     [1:0]                    quadrant;
reg     [`DATA_WIDTH-1 : 0]      data_in;
wire    [(`DATA_WIDTH*2)-1 : 0]  data_out;

// -------------------------------------------------------- module instantiation
cosecant_LUT DUT_cosecantLUT(
    .clk         (clk           ),
    .reset_n     (reset_n       ),
    .en_cosecant (en_cosecant   ),
    .quadrant    (quadrant      ),
    .data_in     (data_in       ),
	.data_out    (data_out      )
);

// -------------------------------------------------------- clk generator
always begin
    #(T/2) clk = 1'b0;
    #(T/2) clk = 1'b1;
end

// -------------------------------------------------------- main loop
initial begin
    // --------------------------------------- reset module
    $display("-----------------------------------------------------------------\n");
    repeat(2) @(posedge clk) begin
        reset_n = 1'b0;
        reset_n = 1'b1;
    end
    
    // --------------------------------------- check for all input values
    $display("-----------------------------------------------------------------\n");
    repeat(91) begin
        @(posedge clk) begin
            reset_n = 1'b1;
            en_cosecant = 1'b1;
            quadrant = 1'b0;
            data_in = num1;
        end
        #T $monitor("Input angle [%3d] | Sign [%1b] | Cosecant DFPU value = %16h",data_in,data_out[63],data_out);
        num1 = num1 + 1;
    end
    @(posedge clk)  reset_n = 1'b0;
    @(posedge clk)  reset_n = 1'b1;
    
    // --------------------------------------- send 20 random -ve inputs
    $display("-----------------------------------------------------------------\n");
    repeat(20) begin
        @(posedge clk) begin
            reset_n = 1'b1;
            en_cosecant = 1'b1;
            quadrant = 1'b0; 
            data_in = min1 + {$random} % (max1-min1);
        end
        #T $display("Input angle [%3d] | Sign [%1b] | Cosecant DFPU value = %16h",data_in,data_out[63],data_out);
    end
    
    $display("-----------------------------------------------------------------\n");
    $finish;
end

// -------------------------------------------------------- dump vcd
initial begin
    $dumpfile("bin/tb_cosecant.vcd");
    $dumpvars(0,DUT_cosecantLUT);
end

// -------------------------------------------------------- end of module

endmodule
