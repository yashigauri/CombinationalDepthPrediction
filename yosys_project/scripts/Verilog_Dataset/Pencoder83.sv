module priority_encoder_8x3(input [7:0] D, output reg [2:0] Y);
  always @(*) begin
    casex(D)
      8'b1xxxxxxx: Y = 3'b111;
      8'b01xxxxxx: Y = 3'b110;
      8'b001xxxxx: Y = 3'b101;
      8'b0001xxxx: Y = 3'b100;
      8'b00001xxx: Y = 3'b011;
      8'b000001xx: Y = 3'b010;
      8'b0000001x: Y = 3'b001;
      8'b00000001: Y = 3'b000;
      default: Y = 3'b000;
    endcase
  end
endmodule
