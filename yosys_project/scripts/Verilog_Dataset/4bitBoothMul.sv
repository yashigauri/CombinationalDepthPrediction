module booth_multiplier(input [3:0] A, input [3:0] B, output reg [7:0] Product);
  reg [3:0] Q, M;
  reg Q_1;
  reg [7:0] ACC;
  integer i;
  
  always @(*) begin
    ACC = 8'b00000000;
    Q = B;
    M = A;
    Q_1 = 0;
    
    for (i = 0; i < 4; i = i + 1) begin
      case ({Q[0], Q_1})
        2'b01: ACC = ACC + {M, 4'b0000};
        2'b10: ACC = ACC - {M, 4'b0000};
      endcase
      {ACC, Q, Q_1} = {ACC[7], ACC, Q};
    end
    Product = ACC;
  end
endmodule
