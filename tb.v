module tb;

reg clk = 0;
reg rst = 1;

wire [3:0] count;

top uut (
    .clk(clk),
    .rst(rst),
    .count(count)
);

always #5 clk = ~clk;

initial begin
    #10 rst = 0;
    #100 $finish;
end

endmodule