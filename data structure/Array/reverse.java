/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Raj
 */

import java.io.*;

public class reverse 
{
    static void reverse_(int arr[], int n)
    {
        for(int i = 0; i< n/2; i++)
        {
            int temp = arr[i];
            arr[i] = arr[n-i-1];
            arr[n-i-1] = temp;
            
        }
    }
    public static void main (String[] args)
    {
        int arr[] = new int[] { 2,8,7,10, 5};
        int n = arr.length;
        
        reverse_(arr, n );
        for (int i = 0 ; i < n; i++)
            System.out.println(arr[i]+ " ");
    }
}
