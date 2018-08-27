public class Fibonacci {
	public static void main(String args[]) {
		for (int i = 0; i <= 15; i++) {
			System.out.println("(" + i + ")" + getFibonacci(i));
		}
	}

	public static int getFibonacci(int n) {
		if (n == 0) {
			return 0;
		} else {
			if (n == 1) {
				return 1;
			} else {
				return getFibonacci(n - 1) + getFibonacci(n - 2);
			}
		}
	}

}
