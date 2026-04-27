`default_nettype none

module tt_um_adder (
    input  wire [7:0] ui_in,
    output wire [7:0] uo_out,
    input  wire [7:0] uio_in,
    output wire [7:0] uio_out,
    output wire [7:0] uio_oe,
    input  wire       ena,
    input  wire       clk,
    input  wire       rst_n
);

    wire [3:0] a = ui_in[3:0];
    wire [3:0] b = ui_in[7:4];

    wire [4:0] sum = a + b;

    // ✅ Enable-controlled output
    assign uo_out = ena ? {3'b000, sum} : 8'b0;

    assign uio_out = 8'b0;
    assign uio_oe  = 8'b0;

    wire _unused = &{clk, rst_n, uio_in, 1'b0};

endmodule
