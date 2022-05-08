public class leet11 {
    public static void main(String[] args) {
        int[] test1 = {1,8,6,2,5,4,8,3,7};
        int[] test2 = {1,1};
        int[] test3 = {1,2,1};
        int[] test4 = {6,4,3,1,4,6,99,62,1,2,6};


        System.out.println(maxArea(test1));
        System.out.println(maxArea(test2));
        System.out.println(maxArea(test3));
        System.out.println(maxArea(test4));
    }

    /**
     * Working method with exponential time complexity
     * @param height
     * @return
     */
    // public int maxArea(int[] height) {
    //     int area = 0;
    //     for (int i = 0; i < height.length; i++) {
    //         int h = height[i];
    //         for (int j = 0; j < height.length; j++) {
    //             int area1 = h * Math.abs(j - i);
    //             if (height[j] >= h && area1 > area) {
    //                 area = area1;
    //             }
    //         }
    //     }
    //     return area;
    // }
    
    /**
     * Recursive method WIP
     * @param height
     * @return
     */
    public static int maxArea(int[] height) {
        return Math.max(Math.min(height[0], height[height.length-1]) * (height.length-1), recur(height, 0, height.length-1));
    }

    public static int recur(int[] height, int left, int right){
        if(left < height.length -1 && right > 0 && (height[left+1] > height[left] || height[right-1] > height[right]))
            return Math.max(Math.min(height[left], height[right]) * (right-left), Math.max(recur(height, left+1, right), recur(height, left, right-1)));
        return Math.min(height[left], height[right]) * (right-left);
    }

    /**
     * Grid creation?
     */
}