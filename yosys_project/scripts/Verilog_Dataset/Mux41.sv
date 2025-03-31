module mux_4x1(input [3:0] D, input [1:0] S, output Y);
  assign Y = (S == 2'b00) ? D[0] :
             (S == 2'b01) ? D[1] :
             (S == 2'b10) ? D[2] : D[3];
endmodule

