module barrel_shifter_4bit(input [3:0] A, input [1:0] Shift, input Dir, output reg [3:0] Y);
  always @(*) begin
    case(Shift)
      2'b00: Y = A;
      2'b01: Y = Dir ? A << 1 : A >> 1;
      2'b10: Y = Dir ? A << 2 : A >> 2;
      2'b11: Y = Dir ? A << 3 : A >> 3;
    endcase
  end
endmodule
