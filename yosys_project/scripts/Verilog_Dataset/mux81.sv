module mux_8x1(input [7:0] D, input [2:0] S, output Y);
  assign Y = D[S];
endmodule

