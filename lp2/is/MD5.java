import java.math.BigInteger;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.Scanner;



// Java program to calculate MD5 hash value
public class MD5 {
    public static String getMd5(String input) {
        try {
            // Static getInstance method is called with hashing MD5
            MessageDigest md = MessageDigest.getInstance("MD5");
            // digest() method is called to calculate message digest
            // of an input digest() return array of byte
            byte[] messageDigest = md.digest(input.getBytes());
            // Convert byte array into signum representation
            BigInteger no = new BigInteger(1, messageDigest);
            // Convert message digest into hex value
            String hashtext = no.toString(16);
            while (hashtext.length() < 32) {
                hashtext = "0" + hashtext;
            }
            return hashtext;
        } // For specifying wrong message digest algorithms
        catch (NoSuchAlgorithmException e) {
            throw new RuntimeException(e);
        }
    }

    // Driver code
    public static void main(String args[]) throws NoSuchAlgorithmException {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter The String: ");
        String s = sc.nextLine();
        System.out.println("HashCode Generated by MD5 is: " + getMd5(s));
    }
}



































/* 


MD5 stands for Message-Digest Algorithm 5. It's a cryptographic hash function 
Input: Any length of text or data.

Output: A 128-bit (16-byte) fixed-length hash value, typically represented as a 32-character hexadecimal string.

Deterministic: Same input → always same output.

Fast and easy to implement.// */