/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Raj
 */
class nto1 
{
    static int fun(int n)
    {
        if (n==0)
            return n;
        System.out.println(n);
        return (fun(n-1));
    }
    
    public static void main(String[] args)
    {
        int n =5;
        System.out.println(fun(n));
    }
}
