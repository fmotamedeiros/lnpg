public class Fatorial {

	public static void main(String[] args) {
		System.out.println(new Fatorial().getFatorialRecursivo(5));
	}
	
	public int getFatorial(int n) {
		int fatorial = 1;
		for (int i = 1; i <= n; i++) {
			fatorial = fatorial * i;
		}
		return fatorial;
	}
	
	public int getFatorialRecursivo(int n) {
		if (n == 1) {
			return 1;
		}
		return n * getFatorialRecursivo(n-1);
	}
	
}
