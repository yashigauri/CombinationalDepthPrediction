module comparator_8bit(input [7:0] A, input [7:0] B, output GT, output EQ, output LT);
  assign GT = (A > B);
  assign EQ = (A == B);
  assign LT = (A < B);
endmodule

