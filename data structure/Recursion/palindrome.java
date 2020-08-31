/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Raj
 */
// Java program for power set
import java.util.*;
import java.lang.*;
import java.io.*;

class palindrome
{
    // A recursive function that check a str
    // is pallindrome or not.
    static boolean isPalRec(String str, int s, int e)
    {
        // if there is only one character
        if(s==e)
            return true;
        // If first and last characters do not match
        if((str.charAt(s)) != (str.charAt(e)))
            return false;
        // If there are more than two characters, check 
        // if middle substring is also plindrome or not.
        if(s < e + 1)
            return isPalRec(str, s + 1, e - 1);
        
        return true;
    }
    static boolean isPalindrome(String str)
    {
        int n = str.length();
        // An empty string is consigered as palindrome
        if(n==0)
            return true;
        return isPalRec(str, 0, n-1);
    }
    
    // Driver Code
    public static void main(String args[])
    {
        String str = "heheh";
        
        if(isPalindrome(str))
            System.out.println("Yes");
        else
            System.out.println("No");
    }
}