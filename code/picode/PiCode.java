package picode;

public class PiCode {
	public static void main(String[] args) {
		if (args.length < 2) {
			System.out.println("Usage: java picode/PiCode [-encode|-decode] [plaintext|ciphertext]");
			System.exit(1);
		}
		
		String mode = args[0];
		String text = args[1];
		
		PiCoder code = new PiCoder();
		if (mode.equals("-encode")) {
			try {
				System.out.println("Ciphertext: " + code.encode(text));
			} catch (Exception exception) {
				System.out.println("Invalid plaintext");
			}
		} else if (mode.equals("-decode")) {
			try {
				System.out.println("Plaintext: " + code.decode(text));
			} catch (Exception exception) {
				System.out.println("Invalid ciphertext");
			}
		} else {
			System.out.println("Invalid mode");
		}
	}
}
