import java.util.Arrays;

public class InterviewFrames {
    public static void main(String[] args) {
        int[] frames = new int[(int) (Math.random() * 20) + 1];
        //int[] frames = new int[20];
        for (int i = 0; i < frames.length; i++) {
            frames[i] = i + 1;
        }
        System.out.println("Given Frames: " + frames.length);
        System.out.println("Frames: " + Arrays.toString(frames));
        int[] arr = populate(frames);
        System.out.println("Populated: " + Arrays.toString(arr));
        System.out.println("Count: " + Arrays.toString(count(arr, frames.length)));
    }

    public static int[] populate(int[] frames) {
        int[] arr = new int[20];
        int rep = arr.length / frames.length;
        int ext = arr.length % frames.length;
        int plot = 0;
        int start = 0;
        if (ext != 0) {
            plot = (arr.length - ext) / ext;
            start = plot - rep;
        }
        int framePoint = 0;
        int j = 0;
        for (int i = 1; i <= arr.length; i++) {
            if (ext != 0 && (i - 1 - start) % plot == 0) {
                arr[i - 1] = arr[i - 2];
            } else {
                arr[i - 1] = frames[j / rep];
                j++;
            }
            if (j % rep == 0.0 && framePoint < frames.length - 1)
                framePoint++;
        }
        return arr;
    }

    public static int[] count(int[] arr, int frames) {
        int[] count = new int[frames];
        for (int i : arr) {
            count[i - 1]++;
        }
        return count;
    }
}
