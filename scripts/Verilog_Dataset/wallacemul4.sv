module wallace_multiplier_4bit(input [3:0] A, input [3:0] B, output [7:0] Product);
  wire [3:0] pp0, pp1, pp2, pp3;
  wire [5:0] s1, c1, s2, c2;
  wire [7:0] s3, c3;

  assign pp0 = A & {4{B[0]}};
  assign pp1 = A & {4{B[1]}};
  assign pp2 = A & {4{B[2]}};
  assign pp3 = A & {4{B[3]}};

  assign s1[0] = pp0[1] ^ pp1[0];
  assign c1[0] = pp0[1] & pp1[0];
  
  assign s1[1] = pp0[2] ^ pp1[1] ^ pp2[0];
  assign c1[1] = (pp0[2] & pp1[1]) | (pp1[1] & pp2[0]) | (pp0[2] & pp2[0]);

  assign s1[2] = pp0[3] ^ pp1[2] ^ pp2[1] ^ pp3[0];
  assign c1[2] = (pp0[3] & pp1[2]) | (pp1[2] & pp2[1]) | (pp2[1] & pp3[0]) | (pp0[3] & pp2[1]) | (pp1[2] & pp3[0]) | (pp0[3] & pp3[0]);

  assign s1[3] = pp1[3] ^ pp2[2] ^ pp3[1];
  assign c1[3] = (pp1[3] & pp2[2]) | (pp2[2] & pp3[1]) | (pp1[3] & pp3[1]);

  assign s1[4] = pp2[3] ^ pp3[2];
  assign c1[4] = pp2[3] & pp3[2];

  assign s1[5] = pp3[3];

  assign {c3, s3} = {1'b0, s1} + {c1, 1'b0};

  assign Product = {c3, s3};
endmodule
