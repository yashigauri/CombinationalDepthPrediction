module booth_multiplier_16bit(input [15:0] A, input [15:0] B, output reg [31:0] Product);
  reg [15:0] Q, M;
  reg Q_1;
  reg [31:0] ACC;
  integer i;
  
  always @(*) begin
    ACC = 32'b0;
    Q = B;
    M = A;
    Q_1 = 0;
    
    for (i = 0; i < 16; i = i + 1) begin
      case ({Q[0], Q_1})
        2'b01: ACC = ACC + {M, 16'b0};
        2'b10: ACC = ACC - {M, 16'b0};
      endcase
      {ACC, Q, Q_1} = {ACC[31], ACC, Q};
    end
    Product = ACC;
  end
endmodule
