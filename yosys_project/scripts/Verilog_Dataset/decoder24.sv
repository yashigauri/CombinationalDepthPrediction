module decoder_2x4(input [1:0] A, output reg [3:0] Y);
  always @(*) begin
    Y = 4'b0000;
    Y[A] = 1'b1;
  end
endmodule
