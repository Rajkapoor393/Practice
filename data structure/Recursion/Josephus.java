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


class Josephus 
{
    static int josep(int n, int k)
    {
        if(n == 1)
            return 1;
        else
            /* The position returned by Josephus (n-1, k)
               is adjusted because the recursive call 
               josephus(n-1, k) considers the origional
               position k%n + 1 as position 1
            */
            return (josep(n-1, k) + k-1) % n +1;
    }
    
    // Driver program to test above function
    public static void main(String[] args)
    {
        int n = 14;
        int k = 2;
        
        System.out.println("The chosen place is " + josep(n, k));
    }
}
