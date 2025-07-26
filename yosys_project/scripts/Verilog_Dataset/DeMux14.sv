module demux_1x4(input D, input [1:0] S, output reg [3:0] Y);
  always @(*) begin
    Y = 4'b0000;
    Y[S] = D;
  end
endmodule

