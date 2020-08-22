/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Raj
 */
class factorial 
{
    
    static int fact(int n)
    {
        if(n == 0)
            return 1;
        else
            return n*fact(n-1);
    }
    public static void main(String args[])
    {
        int n =5;
       // fact(n); 
        System.out.println("The factorial of "+ n + " is " + fact(n));
    }
}

