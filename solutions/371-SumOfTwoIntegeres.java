class Solution {
    public int getSum(int a, int b) {
        while (b != 0){
            int tmp = (a & b) << 1;
            System.out.println(tmp);
        }
        return tmp;
    }
}