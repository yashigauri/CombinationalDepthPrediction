module comparator_4bit(input [3:0] A, input [3:0] B, output GT, output EQ, output LT);
  assign GT = (A > B);
  assign EQ = (A == B);
  assign LT = (A < B);
endmodule
