import javax.crypto.Cipher;
import javax.crypto.SecretKey;
import javax.crypto.spec.SecretKeySpec;
import java.util.Base64;
import java.util.Scanner;

public class DES {

    // Method to create a DES key from a string
    public static SecretKey getKeyFromString(String keyStr) throws Exception {
        if (keyStr.length() != 8) {
            throw new IllegalArgumentException("Key must be exactly 8 characters long.");
        }
        byte[] keyBytes = keyStr.getBytes();
        return new SecretKeySpec(keyBytes, "DES");
    }

    // Encrypt the plain text using DES
    public static String encrypt(String plainText, SecretKey key) throws Exception {
        Cipher cipher = Cipher.getInstance("DES/ECB/PKCS5Padding");
        cipher.init(Cipher.ENCRYPT_MODE, key);
        byte[] encrypted = cipher.doFinal(plainText.getBytes());
        return Base64.getEncoder().encodeToString(encrypted);
    }

    // Decrypt the cipher text using DES
    public static String decrypt(String encryptedText, SecretKey key) throws Exception {
        Cipher cipher = Cipher.getInstance("DES/ECB/PKCS5Padding");
        cipher.init(Cipher.DECRYPT_MODE, key);
        byte[] decodedBytes = Base64.getDecoder().decode(encryptedText);
        byte[] decrypted = cipher.doFinal(decodedBytes);
        return new String(decrypted);
    }

    public static void main(String[] args) {
        try {
            Scanner scanner = new Scanner(System.in);

            System.out.print("Enter 8-character DES key: ");
            String keyStr = scanner.nextLine();
            SecretKey key = getKeyFromString(keyStr);

            System.out.print("Enter a message to encrypt: ");
            String message = scanner.nextLine();

            String encrypted = encrypt(message, key);
            System.out.println("Encrypted message: " + encrypted);

            String decrypted = decrypt(encrypted, key);
            System.out.println("Decrypted message: " + decrypted);

        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}













//DES uses a 56-bit key + 8 bits for parity, making a total of 64 bits, which is exactly 8 bytes.//

