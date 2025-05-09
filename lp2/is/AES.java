import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;
import java.util.Base64;
import java.util.Scanner;

public class AES {

    // Method to encrypt data using AES
    public static String encrypt(String data, String key) throws Exception {
        // Create a new AES key
        SecretKeySpec secretKey = new SecretKeySpec(key.getBytes(), "AES");

        // Create a cipher instance for AES encryption
        Cipher cipher = Cipher.getInstance("AES");

        // Initialize the cipher in encryption mode
        cipher.init(Cipher.ENCRYPT_MODE, secretKey);

        // Encrypt the data
        byte[] encryptedData = cipher.doFinal(data.getBytes());

        // Return the encrypted data as a Base64 encoded string
        return Base64.getEncoder().encodeToString(encryptedData);
    }

    // Method to decrypt data using AES
    public static String decrypt(String encryptedData, String key) throws Exception {
        // Create a new AES key
        SecretKeySpec secretKey = new SecretKeySpec(key.getBytes(), "AES");

        // Create a cipher instance for AES decryption
        Cipher cipher = Cipher.getInstance("AES");

        // Initialize the cipher in decryption mode
        cipher.init(Cipher.DECRYPT_MODE, secretKey);

        // Decode the encrypted data from Base64 format
        byte[] decodedData = Base64.getDecoder().decode(encryptedData);

        // Decrypt the data
        byte[] decryptedData = cipher.doFinal(decodedData);

        // Return the decrypted data as a string
        return new String(decryptedData);
    }

    public static void main(String[] args) {
        // Create a Scanner object to take user input
        Scanner scanner = new Scanner(System.in);

        try {
            // Take user input for the key and message
            System.out.print("Enter a 16-character AES key (128 bits): ");
            String key = scanner.nextLine();

            if (key.length() != 16) {
                System.out.println("Key must be exactly 16 characters long.");
                return;
            }

            System.out.print("Enter the message to encrypt: ");
            String data = scanner.nextLine();

            // Encrypt the data
            String encryptedData = encrypt(data, key);
            System.out.println("Encrypted Data (Base64): " + encryptedData);

            // Decrypt the data
            String decryptedData = decrypt(encryptedData, key);
            System.out.println("Decrypted Data: " + decryptedData);
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            scanner.close();
        }
    }
}

